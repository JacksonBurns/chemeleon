"""
train.py

Trains an autoencoder using features calculated by features.py and
saved in Zarr format. Emphasis on low memory consumption so that this
approach can scale to infinity.
"""

import os
import sys
from pathlib import Path

import torch
import zarr
from tqdm import tqdm
from torch.utils.data import DataLoader as TorchDataLoader
from torch.utils.data import Dataset as TorchDataset

from lightning import Trainer
from lightning.pytorch.utilities.rank_zero import rank_zero_info
from lightning.pytorch.callbacks import ModelCheckpoint, EarlyStopping
from lightning.pytorch.loggers import TensorBoardLogger

from models import fastpropFoundation
from utils.torchford import Welford


# architecture
EMBEDDING_DIM = 8
ENCODING_SIZE = 4096
HIDDEN_SIZES = tuple([ENCODING_SIZE] * 3)
DECODER_SIZES = tuple()
# output/pubchem1MM_MDAE_PLR_15mask_8embedding_4096x3layers_4096encoding
# 
# output/pubchem1MM_MDAE_15mask_64encoding_shrinkpercent30
# (1129, 790, 553, 387, 270, 189, 132, 92)  # contiually shrink by 30% encoding 64

# training configuration
LEARNING_RATE = 1e-5
NUM_EPOCHS = 500
PATIENCE = 50
BATCH_SIZE = 1024


class ZarrDataset(TorchDataset):
    def __init__(self, zarr_path: str):
        self.z = zarr.open_array(zarr_path)
        self.len = self.z.shape[0]

    def __len__(self):
        return self.len

    def __getitem__(self, batch_idx: list[int]):
        return torch.tensor(self.z[batch_idx], dtype=torch.float32)


if __name__ == "__main__":
    try:
        training_store = Path(sys.argv[1])
        output_dir = Path(sys.argv[2])
        restart_ckpt = None
        if len(sys.argv) == 4:
            restart_ckpt = Path(sys.argv[3])
    except:
        print("usage: python pretrain.py TRAINING_STORE OUTPUT_DIR [RESTART_CKPT]")
        exit(1)

    z = zarr.open_array(training_store, mode='r')
    n_features = z.shape[1]
    del z
    
    dataset = ZarrDataset(training_store)
    gen = torch.Generator().manual_seed(1701)
    train_dset, val_dset, test_dset = torch.utils.data.random_split(dataset, [0.7, 0.2, 0.1], gen)
    train_dataloader = TorchDataLoader(train_dset, num_workers=3, persistent_workers=True, batch_size=BATCH_SIZE, shuffle=True)
    val_dataloader = TorchDataLoader(val_dset, num_workers=1, batch_size=BATCH_SIZE, persistent_workers=True)
    test_dataloader = TorchDataLoader(test_dset, num_workers=1, batch_size=BATCH_SIZE, persistent_workers=True)

    cached_means_fpath = f"feature_means_cached_{training_store.stem}.pt"
    cached_vars_fpath = f"feature_vars_cached_{training_store.stem}.pt"
    if not os.path.exists(cached_means_fpath) or not os.path.exists(cached_vars_fpath):
        w = Welford()
        loader = TorchDataLoader(train_dset, batch_size=BATCH_SIZE)
        for batch in tqdm(loader, desc="Calculating Feature Statistics"):
            batch = batch.to("cuda:0")
            w.add_all(batch)
        # set all missing and invariant features means and vars to zero
        torch.save(
            torch.nan_to_num(w.mean, posinf=0.0, neginf=0.0),
            cached_means_fpath,
        )
        torch.save(
            torch.nan_to_num(w.var_p, posinf=0.0, neginf=0.0),
            cached_vars_fpath,
        )
        del w, loader
    feature_means = torch.load(cached_means_fpath, weights_only=True, map_location="cpu")
    feature_vars = torch.load(cached_vars_fpath, weights_only=True, map_location="cpu")

    if restart_ckpt is None:
        model = fastpropFoundation(
            feature_means=feature_means,
            feature_vars=feature_vars,
            num_features=n_features,
            winsorization_factor=6,
            hidden_sizes=HIDDEN_SIZES,
            decoder_sizes=DECODER_SIZES,
            encoding_size=ENCODING_SIZE,
            learning_rate=LEARNING_RATE,
            masking_ratio=0.15,
            embedding_dim=EMBEDDING_DIM,
        )
    else:
        model = fastpropFoundation.load_from_checkpoint(restart_ckpt, map_location="cpu")
    rank_zero_info(model)

    tensorboard_logger = TensorBoardLogger(
        output_dir,
        name="tensorboard_logs",
        default_hp_metric=False,
    )
    callbacks = [
        EarlyStopping(
            monitor="validation/loss",
            mode="min",
            verbose=False,
            patience=PATIENCE,
        ),
        ModelCheckpoint(
            monitor="validation/loss",
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
    model = fastpropFoundation.load_from_checkpoint(ckpt_path, map_location="cpu")
    trainer.test(model, test_dataloader)
    torch.save(model, output_dir / "best.pt")
