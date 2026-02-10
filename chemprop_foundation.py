import os
from typing import Iterable

from lightning import pytorch as pl
import torch
from torch import distributed
import zarr

from rdkit.Chem import MolFromSmiles
from chemprop.nn import Aggregation, ChempropMetric, MessagePassing, Predictor
from fastprop.data import standard_scale
from chemprop.featurizers import SimpleMoleculeMolGraphFeaturizer
from chemprop.featurizers.atom import RIGRAtomFeaturizer
from chemprop.featurizers.bond import RIGRBondFeaturizer
from chemprop.data import Datum
from chemprop.models import MPNN


class WinsorizeStdevN(torch.nn.Module):
    def __init__(self, n: float) -> None:
        super().__init__()
        self.n = n

    def forward(self, batch: torch.Tensor):
        return torch.clamp(batch, min=-self.n, max=self.n)

    def extra_repr(self) -> str:
        return f"n={self.n}"

import numpy as np
from chemprop.data.collate import TrainingBatch, BatchMolGraph


# mock the default chemprop dataset class to load y's incrementally
class ChemPropChunkwiseZarrDataset(torch.utils.data.Dataset):
    def __init__(self, smiles: list[str], zarr_store: str):
        self.smiles = np.array(smiles)
        self.z = zarr.open_array(zarr_store)
        assert self.z.shape[0] == len(smiles), "Mismatched smiles and feature sizes"
        self.len = self.z.nchunks
        self.chunksize = self.z.chunks[0]
        self.molgraph_generator = SimpleMoleculeMolGraphFeaturizer(
            atom_featurizer=RIGRAtomFeaturizer(),
            bond_featurizer=RIGRBondFeaturizer(),
        )

    def __len__(self):
        return self.len

    def __getitem__(self, idx: int):
        start_idx = idx * self.chunksize
        stop_idx = start_idx + self.chunksize
        return TrainingBatch(
            BatchMolGraph([self.molgraph_generator(MolFromSmiles(s)) for s in self.smiles[start_idx:stop_idx]]),
            None,
            None,
            self.z[start_idx:stop_idx, :],
            torch.ones((self.chunksize, 1)),
            None,
            None,
        )
        
        
import torch
import os
from torch.utils.data import DataLoader
from tqdm import tqdm

import torch

class BatchedWelford:
    """
    Computes running mean and variance using Welford's online algorithm.
    Optimized for processing batches of data.
    
    ROBUSTNESS:
    - Handles NaNs (ignores them).
    - Handles Infs (treats them as NaNs/missing).
    - Tracks per-feature sample counts to handle variable missingness.
    """
    def __init__(self, num_features):
        self.num_features = num_features
        # We defer device allocation until we see the first batch
        self.n = None
        self.mean = None
        self.M2 = None

    def _init_stats(self, device, dtype):
        self.n = torch.zeros(self.num_features, dtype=dtype, device=device)
        self.mean = torch.zeros(self.num_features, dtype=dtype, device=device)
        self.M2 = torch.zeros(self.num_features, dtype=dtype, device=device)

    def update(self, batch):
        """
        Update stats with a new batch. 
        Shape: [Batch_Size, Num_Features] or [Num_Features]
        """
        # 1. Standardize Shape and Type
        batch = batch.reshape(-1, self.num_features).to(torch.float64)
        
        if batch.shape[0] == 0:
            return

        # Initialize stats on the correct device if this is the first batch
        if self.mean is None:
            self._init_stats(batch.device, torch.float64)

        # 2. SANITIZE: Convert +/- Infinity to NaN
        # This prevents mean -> Inf, which causes Inf - Inf -> NaN later.
        if torch.isinf(batch).any():
            # We clone to avoid modifying the dataset tensor in-place
            batch = batch.clone()
            batch[torch.isinf(batch)] = float('nan')

        # 3. Calculate Batch Stats (Robust to NaNs)
        # Count valid (non-NaN) values per feature
        # ~isnan() returns 1 for valid, 0 for nan
        n_b = torch.isnan(batch).logical_not().sum(dim=0).to(torch.float64)
        
        # Calculate batch mean (ignoring NaNs)
        # nanmean returns NaN if a column is ALL NaNs -> we default these to 0.0
        mean_b = torch.nanmean(batch, dim=0)
        mean_b = torch.nan_to_num(mean_b, nan=0.0)

        # Calculate M2_b: sum((x - mean_b)^2) ignoring NaNs
        # (batch - mean_b) creates NaNs where batch was NaN. nansum treats them as 0.
        diff = batch - mean_b
        M2_b = torch.nansum(diff ** 2, dim=0)

        # 4. Merge with Global Stats (Welford's Parallel Formula)
        n_a = self.n
        mean_a = self.mean
        M2_a = self.M2

        new_n = n_a + n_b

        # Mask to handle cases where a feature effectively has NO data yet (n=0)
        # This prevents 0/0 division errors
        valid_mask = new_n > 0
        
        delta = mean_b - mean_a

        # Prepare updates
        # We only update indices where we actually have data (valid_mask)
        term1 = torch.zeros_like(mean_a)
        term1[valid_mask] = delta[valid_mask] * (n_b[valid_mask] / new_n[valid_mask])
        
        term2 = torch.zeros_like(M2_a)
        term2[valid_mask] = (delta[valid_mask] ** 2) * (n_a[valid_mask] * n_b[valid_mask] / new_n[valid_mask])

        # Commit updates
        self.mean = mean_a + term1
        self.M2 = M2_a + M2_b + term2
        self.n = new_n

    @property
    def var(self):
        if self.n is None: return None
        # Variance is M2 / (n - 1)
        # Return 0.0 where n < 2 to avoid NaNs
        variance = torch.zeros_like(self.mean)
        valid = self.n > 1
        variance[valid] = self.M2[valid] / (self.n[valid] - 1)
        return variance

    @property
    def std(self):
        if self.n is None: return None
        return torch.sqrt(self.var)


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

    def validation_step(self, batch, batch_idx = 0):
        bmg, V_d, X_d, targets, weights, lt_mask, gt_mask = batch
        targets = standard_scale(targets, self.feature_means, self.feature_vars)
        targets = self.winsorization(targets)
        return super().validation_step((bmg, V_d, X_d, targets, weights, lt_mask, gt_mask), batch_idx)

    def test_step(self, batch, batch_idx = 0):
        bmg, V_d, X_d, targets, weights, lt_mask, gt_mask = batch
        targets = standard_scale(targets, self.feature_means, self.feature_vars)
        targets = self.winsorization(targets)
        return super().test_step((bmg, V_d, X_d, targets, weights, lt_mask, gt_mask), batch_idx)

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
        self.log("train/masked_loss", l, batch_size=batch_size, prog_bar=True, on_epoch=True, sync_dist=distributed.is_initialized())
        return l


if __name__ == "__main__":
    import sys
    from pathlib import Path
    
    from tqdm import tqdm
    from chemprop.nn import NormAggregation, BondMessagePassing, RegressionFFN, metrics
    from lightning.pytorch.utilities import rank_zero_info
    from lightning.pytorch import Trainer
    from lightning.pytorch.callbacks.model_checkpoint import ModelCheckpoint
    from lightning.pytorch.callbacks.early_stopping import EarlyStopping
    from lightning.pytorch.loggers import TensorBoardLogger
    import polars
    from utils.torchford import Welford
    from rdkit.rdBase import BlockLogs
    bl = BlockLogs()
    
    NUM_EPOCHS = 40
    PATIENCE = 4
    HIDDEN_SIZE = 2_048
    DEPTH = 6
    
    try:
        training_store = Path(sys.argv[1])
        output_dir = Path(sys.argv[2])
        smiles_file = Path(sys.argv[3])
    except:
        print("usage: python chemprop_foundation.py TRAINING_STORE OUTPUT_DIR /path/to/smiles.parquet")
        exit(1)
        
    z = zarr.open_array(training_store, mode='r')
    n_features = z.shape[1]
    del z

    smiles = polars.read_parquet(smiles_file)["SMILES"].to_list()
    
    
    # lightning training code from other script    
    dataset = ChemPropChunkwiseZarrDataset(
        smiles,
        training_store,
    )
    gen = torch.Generator().manual_seed(1701)
    train_dset, val_dset, test_dset = torch.utils.data.random_split(dataset, [0.95, 0.04, 0.01], gen)
    
    sampler = None
    from torch.utils.data import DataLoader
    train_dataloader = DataLoader(dataset=train_dset, batch_size=None, shuffle=True, num_workers=4, persistent_workers=True)
    val_dataloader = DataLoader(dataset=val_dset, batch_size=None, shuffle=False, num_workers=4, persistent_workers=True)
    test_dataloader = DataLoader(dataset=test_dset, batch_size=None, shuffle=False, num_workers=4, persistent_workers=True)

    cached_means_fpath = f"feature_means_cached_{training_store.stem}.pt"
    cached_vars_fpath = f"feature_vars_cached_{training_store.stem}.pt"
    if not os.path.exists(cached_means_fpath) or not os.path.exists(cached_vars_fpath):
        print("missing cached stats, run get_training_set_stats.py before this script")
        exit(1)
    feature_means = torch.load(cached_means_fpath, weights_only=True, map_location="cpu")
    feature_vars = torch.load(cached_vars_fpath, weights_only=True, map_location="cpu")

    rigr_atom_featurizer = RIGRAtomFeaturizer()
    rigr_bond_featurizer = RIGRBondFeaturizer()
    featurizer = SimpleMoleculeMolGraphFeaturizer(atom_featurizer=rigr_atom_featurizer, bond_featurizer=rigr_bond_featurizer)

    model = MaskedDescriptorsMPNN(
        BondMessagePassing(
            d_v=featurizer.atom_fdim,
            d_e=featurizer.bond_fdim,
            d_h=HIDDEN_SIZE,
            depth=DEPTH,
        ),
        NormAggregation(),
        predictor=RegressionFFN(
            n_tasks=n_features,
            input_dim=HIDDEN_SIZE,
            hidden_dim=1_024,
        ),
        metrics=[metrics.MSE()],
        masking_ratio=0.30,
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

