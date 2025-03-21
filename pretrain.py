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
import numpy as np
from tqdm import tqdm
from torch.utils.data import DataLoader as TorchDataLoader
from torch.utils.data import Dataset as TorchDataset

from lightning import Trainer
from lightning.pytorch.utilities.rank_zero import rank_zero_info
from lightning.pytorch.callbacks import ModelCheckpoint, EarlyStopping
from lightning.pytorch.loggers import TensorBoardLogger

from models import fastpropFoundation
from utils.torchford import Welford


# autoencoder architecture
HIDDEN_SIZES = (1500, 1300, 1100, 900, 700, 500, 300, 100)
ENCODING_SIZE = 32

# training configuration
LEARNING_RATE = 1e-4
NUM_EPOCHS = 20
PATIENCE = 2
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
    except:
        print("usage: python pretrain.py TRAINING_STORE OUTPUT_DIR")
        exit(1)

    z = zarr.open_array(training_store, mode='r')
    n_samples = z.shape[0]
    n_features = z.shape[1]

    cached_means_fpath = f"feature_means_cached_{training_store.stem}.pt"
    cached_vars_fpath = f"feature_vars_cached_{training_store.stem}.pt"
    if not os.path.exists(cached_means_fpath) or not os.path.exists(cached_vars_fpath):
        w = Welford()
        idx_batches = np.array_split(np.arange(n_samples), n_samples // 1_024)
        for idxs in tqdm(idx_batches, desc="Calculating Feature Statistics"):
            batch = torch.tensor(z[idxs], dtype=torch.float32).to("cuda:0")
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
        del w
    del z
    feature_means = torch.load(cached_means_fpath, weights_only=True, map_location="cpu")
    feature_vars = torch.load(cached_vars_fpath, weights_only=True, map_location="cpu")
    
    dataset = ZarrDataset(training_store)
    gen = torch.Generator().manual_seed(1701)
    train_dset, val_dset, test_dset = torch.utils.data.random_split(dataset, [0.7, 0.2, 0.1], gen)
    train_dataloader = TorchDataLoader(train_dset, num_workers=32, persistent_workers=True, batch_size=BATCH_SIZE, shuffle=True)
    val_dataloader = TorchDataLoader(val_dset, num_workers=16, batch_size=BATCH_SIZE, persistent_workers=True)
    test_dataloader = TorchDataLoader(test_dset, num_workers=16, batch_size=BATCH_SIZE, persistent_workers=True)

    model = fastpropFoundation(
        feature_means=feature_means,
        feature_vars=feature_vars,
        num_features=n_features,
        hidden_sizes=HIDDEN_SIZES,
        encoding_size=ENCODING_SIZE,
        learning_rate=LEARNING_RATE,
    )
    # model = fastpropBatchNormAutoEncoder.load_from_checkpoint(".ckpt")
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
    model = model.__class__.load_from_checkpoint(ckpt_path)
    trainer = Trainer(devices=1, logger=tensorboard_logger)
    trainer.test(model, test_dataloader)
