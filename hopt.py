import sys
import os
from pathlib import Path

import torch
import zarr
from torch.utils.data import DataLoader as TorchDataLoader

from lightning import Trainer
from lightning.pytorch.utilities.rank_zero import rank_zero_info
from lightning.pytorch.callbacks import ModelCheckpoint, EarlyStopping
from lightning.pytorch.loggers import TensorBoardLogger
from tqdm import tqdm

import optuna

from models import fastpropFoundation
from pretrain import ZarrDataset
from utils.torchford import Welford


# training configuration
LEARNING_RATE = 1e-5
NUM_EPOCHS = 500
PATIENCE = 50
BATCH_SIZE = 1024

# hopt config
NUM_HOPT_TRIALS = 10


def fit_one(trial, training_store, n_features, output_dir):
    embedding_size = trial.suggest_categorical("embedding_size", (4, 8, 12, 16))
    num_layers = trial.suggest_categorical("num_layers", (2, 3, 4))
    hidden_size = trial.suggest_categorical("hidden_size", (1024, 2048, 4096))
    
    dataset = ZarrDataset(training_store)
    gen = torch.Generator().manual_seed(1701)
    train_dset, val_dset, test_dset = torch.utils.data.random_split(dataset, [0.7, 0.2, 0.1], gen)
    train_dataloader = TorchDataLoader(train_dset, num_workers=3, persistent_workers=True, batch_size=BATCH_SIZE, shuffle=True)
    val_dataloader = TorchDataLoader(val_dset, num_workers=1, batch_size=BATCH_SIZE, persistent_workers=True)
    test_dataloader = TorchDataLoader(test_dset, num_workers=1, batch_size=BATCH_SIZE, persistent_workers=True)

    cached_means_fpath = f"feature_means_cached_{training_store.stem}.pt"
    cached_vars_fpath = f"feature_vars_cached_{training_store.stem}.pt"
    feature_means = torch.load(cached_means_fpath, weights_only=True, map_location="cpu")
    feature_vars = torch.load(cached_vars_fpath, weights_only=True, map_location="cpu")

    model = fastpropFoundation(
        feature_means=feature_means,
        feature_vars=feature_vars,
        num_features=n_features,
        winsorization_factor=6,
        hidden_sizes=[hidden_size]*num_layers,
        decoder_sizes=tuple(),
        encoding_size=hidden_size,
        learning_rate=LEARNING_RATE,
        masking_ratio=0.15,
        embedding_dim=embedding_size,
    )
    rank_zero_info(model)
    output_dir = output_dir / f"e{embedding_size}_n{num_layers}_h{hidden_size}"
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
        strategy="ddp_spawn",  # required to make optuna work
    )
    trainer.fit(model, train_dataloader, val_dataloader)
    ckpt_path = trainer.checkpoint_callback.best_model_path
    print(f"Reloading best model from checkpoint file: {ckpt_path}")
    trainer = Trainer(logger=tensorboard_logger, devices=[0])
    model = fastpropFoundation.load_from_checkpoint(ckpt_path, map_location="cpu")
    res = trainer.test(model, test_dataloader)[0]
    torch.save(model, output_dir / f"e{embedding_size}_n{num_layers}_h{hidden_size}_best.pt")
    return res["test/loss"]

def main():
    # load the data
    try:
        training_store = Path(sys.argv[1])
        output_dir = Path(sys.argv[2])
    except:
        print("usage: python hopt.py TRAINING_STORE OUTPUT_DIR")
        exit(1)
    output_dir.mkdir(exist_ok=True)

    z = zarr.open_array(training_store, mode='r')
    n_features = z.shape[1]
    del z

    study = optuna.create_study(direction="minimize")
    study.optimize(
        lambda trial: fit_one(
            trial,
            training_store=training_store,
            n_features=n_features,
            output_dir=output_dir,
        ),
        n_trials=NUM_HOPT_TRIALS,
    )
    study.trials_dataframe().to_csv("hopt_results.csv")

if __name__ == "__main__":
    main()
