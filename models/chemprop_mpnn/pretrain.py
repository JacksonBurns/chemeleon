from typing import Iterable

import torch
import zarr
from chemprop.data import Datum
from chemprop.featurizers import SimpleMoleculeMolGraphFeaturizer
from chemprop.models import MPNN
from chemprop.nn import Aggregation, ChempropMetric, MessagePassing, Predictor
from fastprop.data import standard_scale
from lightning import pytorch as pl
from rdkit.Chem import MolFromSmiles
from torch import distributed


class WinsorizeStdevN(torch.nn.Module):
    def __init__(self, n: float) -> None:
        super().__init__()
        self.n = n

    def forward(self, batch: torch.Tensor):
        return torch.clamp(batch, min=-self.n, max=self.n)

    def extra_repr(self) -> str:
        return f"n={self.n}"


# mock the default chemprop dataset class to load y's incrementally
class ChemPropZarrDataset(torch.utils.data.Dataset):
    def __init__(self, smiles: list[str], zarr_store: str):
        self.smiles = smiles
        self.len = len(smiles)
        self.z = zarr.open_array(zarr_store)
        assert self.z.shape[0] == len(smiles), "Mismatched smiles and feature sizes"
        self.molgraph_generator = SimpleMoleculeMolGraphFeaturizer()

    def __len__(self):
        return self.len

    def __getitem__(self, idx: int):
        mg = self.molgraph_generator(MolFromSmiles(self.smiles[idx]))
        return Datum(mg, None, None, self.z[idx, :], 1.0, None, None)


class MaskedDescriptorsMPNN(MPNN):
    def __init__(
        self,
        message_passing: MessagePassing,
        agg: Aggregation,
        predictor: Predictor,
        metrics: Iterable[ChempropMetric],
        masking_ratio: float,
        feature_means: torch.Tensor,
        feature_vars: torch.Tensor,
        winsorization_factor: int = 6,
    ):
        super().__init__(message_passing, agg, predictor, False, metrics)
        self.masking_ratio = masking_ratio
        self.register_buffer("feature_means", feature_means)
        self.register_buffer("feature_vars", feature_vars)
        self.winsorization = WinsorizeStdevN(winsorization_factor)

    def validation_step(self, batch, batch_idx=0):
        bmg, V_d, X_d, targets, weights, lt_mask, gt_mask = batch
        targets = standard_scale(targets, self.feature_means, self.feature_vars)
        targets = self.winsorization(targets)
        return super().validation_step(
            (bmg, V_d, X_d, targets, weights, lt_mask, gt_mask), batch_idx
        )

    def test_step(self, batch, batch_idx=0):
        bmg, V_d, X_d, targets, weights, lt_mask, gt_mask = batch
        targets = standard_scale(targets, self.feature_means, self.feature_vars)
        targets = self.winsorization(targets)
        return super().test_step(
            (bmg, V_d, X_d, targets, weights, lt_mask, gt_mask), batch_idx
        )

    def training_step(self, batch, batch_idx):
        # overrides parent method to ranomly mask (evaluate only masked descriptors) during training
        batch_size = self.get_batch_size(batch)
        bmg, V_d, X_d, targets, weights, lt_mask, gt_mask = batch
        targets = standard_scale(targets, self.feature_means, self.feature_vars)
        targets = self.winsorization(targets)
        mask = (torch.rand_like(targets) < self.masking_ratio).bool()
        Z = self.fingerprint(bmg, V_d, X_d)
        preds = self.predictor.train_step(Z)
        l = self.criterion(preds, targets, mask, weights, lt_mask, gt_mask)
        self.log(
            "train/masked_loss",
            self.criterion,
            batch_size=batch_size,
            prog_bar=True,
            on_epoch=True,
            sync_dist=distributed.is_initialized(),
        )
        return l


if __name__ == "__main__":
    import sys
    from pathlib import Path

    from chemprop.data import build_dataloader
    from chemprop.nn import (BondMessagePassing, MeanAggregation,
                             RegressionFFN, metrics)
    from lightning.pytorch import Trainer
    from lightning.pytorch.callbacks.early_stopping import EarlyStopping
    from lightning.pytorch.callbacks.model_checkpoint import ModelCheckpoint
    from lightning.pytorch.loggers import TensorBoardLogger
    from lightning.pytorch.utilities import rank_zero_info
    from tqdm import tqdm

    BATCH_SIZE = 128
    NUM_EPOCHS = 500
    PATIENCE = 50
    HIDDEN_SIZE = 2_048
    DEPTH = 6

    try:
        training_store = Path(sys.argv[1])
        output_dir = Path(sys.argv[2])
        smiles_file = Path(sys.argv[3])
    except:
        print("usage: python pretrain.py TRAINING_STORE OUTPUT_DIR SMILES_FILE")
        exit(1)

    z = zarr.open_array(training_store, mode="r")
    n_features = z.shape[1]
    del z

    with open(smiles_file, "r") as file:
        smiles = [i.strip() for i in tqdm(file.readlines(), "Reading SMILES")]

    # lightning training code from other script
    dataset = ChemPropZarrDataset(
        smiles,
        training_store,
    )
    gen = torch.Generator().manual_seed(1701)
    train_dset, val_dset, test_dset = torch.utils.data.random_split(
        dataset, [0.7, 0.2, 0.1], gen
    )
    train_dataloader = build_dataloader(
        train_dset,
        num_workers=4,
        batch_size=BATCH_SIZE,
        shuffle=True,
        persistent_workers=True,
    )
    val_dataloader = build_dataloader(
        val_dset,
        num_workers=4,
        batch_size=BATCH_SIZE,
        shuffle=False,
        persistent_workers=True,
    )
    test_dataloader = build_dataloader(
        test_dset,
        num_workers=4,
        batch_size=BATCH_SIZE,
        shuffle=False,
        persistent_workers=True,
    )

    cached_means_fpath = f"feature_means_cached_{training_store.stem}.pt"
    cached_vars_fpath = f"feature_vars_cached_{training_store.stem}.pt"
    feature_means = torch.load(
        cached_means_fpath, weights_only=True, map_location="cpu"
    )
    feature_vars = torch.load(cached_vars_fpath, weights_only=True, map_location="cpu")

    model = MaskedDescriptorsMPNN(
        BondMessagePassing(d_h=HIDDEN_SIZE, depth=DEPTH),
        MeanAggregation(),
        predictor=RegressionFFN(
            n_tasks=n_features,
            input_dim=HIDDEN_SIZE,
            hidden_dim=1_024,
        ),
        metrics=[metrics.MSE()],
        masking_ratio=0.15,
        feature_means=feature_means,
        feature_vars=feature_vars,
        winsorization_factor=6,
    )
    rank_zero_info(model)

    tensorboard_logger = TensorBoardLogger(
        output_dir,
        name="tensorboard_logs",
        default_hp_metric=False,
    )
    callbacks = [
        EarlyStopping(
            monitor="val_loss",
            mode="min",
            verbose=False,
            patience=PATIENCE,
        ),
        ModelCheckpoint(
            monitor="val_loss",
            save_top_k=2,
            mode="min",
            dirpath=output_dir / "checkpoints",
        ),
    ]
    callbacks[1].STARTING_VERSION = 0
    trainer = Trainer(
        max_epochs=NUM_EPOCHS,
        logger=tensorboard_logger,
        log_every_n_steps=1,
        enable_checkpointing=True,
        check_val_every_n_epoch=1,
        callbacks=callbacks,
    )
    trainer.fit(model, train_dataloader, val_dataloader)
    ckpt_path = trainer.checkpoint_callback.best_model_path
    print(f"Reloading best model from checkpoint file: {ckpt_path}")
    model = model.__class__.load_from_checkpoint(ckpt_path, map_location="cpu")
    trainer.test(model, test_dataloader)
    torch.save(model, output_dir / "best.pt")
