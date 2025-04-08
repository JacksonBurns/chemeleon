import sys
from pathlib import Path

import torch
import zarr
from torch.utils.data import DataLoader as TorchDataLoader

from lightning import Trainer
from lightning.pytorch.utilities.rank_zero import rank_zero_info
from lightning.pytorch.callbacks import ModelCheckpoint, EarlyStopping
from lightning.pytorch.loggers import TensorBoardLogger

import ray
from ray import tune
from ray.tune.search.optuna import OptunaSearch

from models import fastpropFoundation
from pretrain import ZarrDataset


# training configuration
LEARNING_RATE = 1e-5
NUM_EPOCHS = 500
PATIENCE = 50
BATCH_SIZE = 1024

# hopt config
NUM_HOPT_TRIALS = 10

ray.init(num_cpus=64, num_gpus=8)


def define_by_run_func(trial):
    trial.suggest_categorical("embedding_size", (4, 8, 12, 16))
    trial.suggest_categorical("num_layers", (2, 3, 4))
    trial.suggest_categorical("hidden_size", (1024, 2048, 4096))
    
def fit_one(training_store, n_features, output_dir, embedding_size, num_layers, hidden_size):
    dataset = ZarrDataset(training_store)
    gen = torch.Generator().manual_seed(1701)
    train_dset, val_dset, test_dset = torch.utils.data.random_split(dataset, [0.7, 0.2, 0.1], gen)
    train_dataloader = TorchDataLoader(train_dset, num_workers=4, persistent_workers=True, batch_size=BATCH_SIZE, shuffle=True)
    val_dataloader = TorchDataLoader(val_dset, num_workers=4, batch_size=BATCH_SIZE, persistent_workers=True)
    test_dataloader = TorchDataLoader(test_dset, num_workers=4, batch_size=BATCH_SIZE, persistent_workers=True)

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
    res = trainer.test(model, test_dataloader)[0]
    torch.save(model, output_dir / "best.pt")
    return res

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

    algo = OptunaSearch(space=define_by_run_func, metric="test/loss", mode="min")
    tuner = tune.Tuner(
        tune.with_resources(
            lambda trial: fit_one(
                training_store,
                n_features,
                output_dir,
                trial["embedding_size"], 
                trial["num_layers"],
                trial["hidden_size"],
            ),
            resources={"gpu": 8},
        ),
        tune_config=tune.TuneConfig(
            search_alg=algo,
            max_concurrent_trials=1,
            num_samples=NUM_HOPT_TRIALS,
            metric="test/loss",
            mode="min",
        ),
    )
    results = tuner.fit()
    results.get_dataframe().to_csv("hopt_results.csv")
    best = results.get_best_result().config
    print(f"Best hyperparameters identified: {', '.join([key + ': ' + str(val) for key, val in best.items()])}")

if __name__ == "__main__":
    main()
