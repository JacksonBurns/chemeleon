"""
fine-tune chemeleon with temporarily frozen message passing weights

note that polaris requires zarr<3 but the feature generator requires
zarr>=3 so two separate python environments are needed
"""

from pathlib import Path
import sys
import pathlib

import torch
import polaris as po
from polaris.utils.types import TargetType
from lightning import Trainer, Callback
from lightning.pytorch.callbacks import ModelCheckpoint
from lightning.pytorch.loggers import CSVLogger
from astartes import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from chemprop.data import MoleculeDatapoint, MoleculeDataset, build_dataloader
from chemprop.featurizers import SimpleMoleculeMolGraphFeaturizer
from chemprop.nn import (
    BondMessagePassing,
    BinaryClassificationFFN,
    RegressionFFN,
    UnscaleTransform,
)
from chemprop.models import MPNN
from chemprop.nn.agg import MeanAggregation

NUM_WORKERS = 4


class FreezeMessagePassingCallback(Callback):
    def __init__(self, freeze_epochs: int):
        super().__init__()
        self.freeze_epochs = freeze_epochs

    def on_fit_start(self, trainer, pl_module):
        for param in pl_module.message_passing.parameters():
            param.requires_grad = False
        print(f"Freezing message passing for first {self.freeze_epochs} epochs.")

    def on_train_epoch_start(self, trainer, pl_module):
        if trainer.current_epoch == self.freeze_epochs:
            for param in pl_module.message_passing.parameters():
                param.requires_grad = True
            print(f"Unfreezing message passing after {self.freeze_epochs} epochs.")


def create_trainer(
    output_dir: pathlib.Path,
    freeze_epochs: int,
    verbose: bool = True,
):
    """Create Lightning trainer with callbacks."""
    callbacks = [
        ModelCheckpoint(
            dirpath=output_dir / "checkpoints",
            filename="best-epoch={epoch}-val_loss={val_loss:.4f}",
            monitor="val_loss",
            mode="min",
            save_last=True,
            auto_insert_metric_name=False,
            enable_version_counter=True,
        ),
    ]
    if freeze_epochs > 0:
        callbacks.append(FreezeMessagePassingCallback(freeze_epochs))

    return Trainer(
        max_epochs=30,
        logger=CSVLogger(output_dir, "trainer_logs"),
        log_every_n_steps=1,
        enable_checkpointing=True,
        check_val_every_n_epoch=1,
        accelerator="gpu",
        callbacks=callbacks,
        deterministic=True,
        enable_progress_bar=verbose,
        enable_model_summary=verbose,
    )


def plot_loss(log_path: pathlib.Path, title: str):
    """Plot training and validation loss curves."""
    log_df = pd.read_csv(log_path / "metrics.csv")
    train_loss = log_df["train_loss_epoch"].dropna().values
    val_loss = log_df["val_loss"].dropna().values
    plt.plot(range(len(train_loss)), train_loss, label="train loss")
    plt.plot(range(len(val_loss)), val_loss, label="val loss")
    plt.title(title)
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.savefig(log_path / "loss.png")
    plt.close()


if __name__ == "__main__":
    try:
        output_dir = Path(sys.argv[1])
        chemeleon_path = Path(sys.argv[2])
        freeze_epochs = int(sys.argv[3])
    except (IndexError, ValueError):
        print(f"usage: python {sys.argv[0]} OUTPUT_DIR CHEMELEON_PATH FREEZE_EPOCHS")
        exit(1)
    if not output_dir.exists():
        output_dir.mkdir()
    polaris_benchmarks = (
        "polaris/pkis2-ret-wt-cls-v2",
        "polaris/pkis2-ret-wt-reg-v2",
        "polaris/pkis2-kit-wt-cls-v2",
        "polaris/pkis2-kit-wt-reg-v2",
        "polaris/pkis2-egfr-wt-reg-v2",
        "polaris/adme-fang-solu-1",
        "polaris/adme-fang-rppb-1",
        "polaris/adme-fang-hppb-1",
        "polaris/adme-fang-perm-1",
        "polaris/adme-fang-rclint-1",
        "polaris/adme-fang-hclint-1",
        "tdcommons/lipophilicity-astrazeneca",
        "tdcommons/ppbr-az",
        "tdcommons/clearance-hepatocyte-az",
        "tdcommons/cyp2d6-substrate-carbonmangels",
        "tdcommons/half-life-obach",
        "tdcommons/cyp2c9-substrate-carbonmangels",
        "tdcommons/clearance-microsome-az",
        "tdcommons/dili",
        "tdcommons/bioavailability-ma",
        "tdcommons/vdss-lombardo",
        "tdcommons/cyp3a4-substrate-carbonmangels",
        "tdcommons/pgp-broccatelli",
        "tdcommons/caco2-wang",
        "tdcommons/herg",
        "tdcommons/bbb-martins",
        "tdcommons/ames",
        "tdcommons/ld50-zhu",
    )
    moleculeace_benchmarks = ()
    for random_seed in (42, 117, 709, 1701, 9001):
        seed_dir = output_dir / f"seed_{random_seed}"
        for benchmark_name in polaris_benchmarks:
            # load the benchmarking data
            benchmark = po.load_benchmark(benchmark_name)
            smiles_col = list(benchmark.input_cols)[0]
            target_cols = list(benchmark.target_cols)
            train, test = benchmark.get_train_test_split()
            train_df, test_df = train.as_dataframe(), test.as_dataframe()
            task_type = benchmark.target_types[target_cols[0]]

            targets = train_df[target_cols]
            targets = targets.fillna(targets.mean(axis=0)).to_numpy()

            # typical chemprop training
            train_idxs, val_idxs = train_test_split(
                np.arange(len(targets)),
                train_size=0.80,
                test_size=0.20,
                random_state=random_seed,
            )
            train_data = [
                MoleculeDatapoint.from_smi(smi, y)
                for smi, y in zip(
                    train_df[smiles_col].iloc[train_idxs], targets[train_idxs]
                )
            ]
            val_data = [
                MoleculeDatapoint.from_smi(smi, y)
                for smi, y in zip(
                    train_df[smiles_col].iloc[val_idxs], targets[val_idxs]
                )
            ]
            test_data = list(map(MoleculeDatapoint.from_smi, test_df[smiles_col]))
            featurizer = SimpleMoleculeMolGraphFeaturizer()
            train_dataset = MoleculeDataset(train_data, featurizer)
            val_dataset = MoleculeDataset(val_data, featurizer)
            test_dataset = MoleculeDataset(test_data, featurizer)
            scaler = None
            if task_type == TargetType.REGRESSION:
                scaler = train_dataset.normalize_targets()
                val_dataset.normalize_targets(scaler)
            train_dataloader = build_dataloader(train_dataset, num_workers=NUM_WORKERS)
            val_dataloader = build_dataloader(
                val_dataset, num_workers=NUM_WORKERS, shuffle=False
            )
            test_dataloader = build_dataloader(
                test_dataset, num_workers=NUM_WORKERS, shuffle=False
            )
            output_transform = (
                UnscaleTransform.from_standard_scaler(scaler)
                if scaler is not None
                else torch.nn.Identity()
            )
            chemeleon_mp = torch.load(chemeleon_path, weights_only=True)
            mp = BondMessagePassing(**chemeleon_mp["hyper_parameters"])
            mp.load_state_dict(chemeleon_mp["state_dict"])
            agg = MeanAggregation()
            hidden_size = mp.output_dim
            fnn = (
                RegressionFFN(
                    output_transform=output_transform,
                    input_dim=hidden_size,
                    hidden_dim=256,
                )
                if task_type == TargetType.REGRESSION
                else BinaryClassificationFFN(
                    output_transform=output_transform,
                    input_dim=hidden_size,
                    hidden_dim=256,
                )
            )
            model = MPNN(mp, agg, fnn)

            _subdir = "".join(c if c.isalnum() else "_" for c in benchmark_name)
            trainer = create_trainer(seed_dir / _subdir, freeze_epochs, verbose=False)
            trainer.fit(model, train_dataloader, val_dataloader)
            log_path = (
                seed_dir
                / _subdir
                / "trainer_logs"
                / f"version_{trainer.logger.version}"
            )
            plot_loss(log_path, f"{benchmark_name} ({task_type.value})")
