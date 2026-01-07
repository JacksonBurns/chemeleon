"""
fit a chemprop model directly on the smiles, with additional Mordred descriptors as molecule features

This version includes clamping of descriptor values to ±6 standard deviations after scaling
to handle extreme outliers and prevent numerical instability.

note that polaris requires zarr<3 but the feature generator requires
zarr>=3 so two separate python environments are needed
"""

import datetime
import json
import os
import shutil
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import polaris as po
import torch
from astartes import train_test_split
from chemprop.conf import DEFAULT_HIDDEN_DIM
from chemprop.data import MoleculeDatapoint, MoleculeDataset, build_dataloader
from chemprop.featurizers import SimpleMoleculeMolGraphFeaturizer
from chemprop.models import MPNN
from chemprop.nn import (BinaryClassificationFFN, BondMessagePassing,
                         RegressionFFN, ScaleTransform, UnscaleTransform)
from chemprop.nn.agg import MeanAggregation
from lightning import Trainer
from lightning.pytorch.callbacks import EarlyStopping, ModelCheckpoint
from lightning.pytorch.loggers import TensorBoardLogger
from mordred import Calculator, descriptors
from polaris.utils.types import TargetType
from rdkit import Chem
from rdkit.Chem import MolFromSmiles
from sklearn.metrics import root_mean_squared_error

BENCHMARK_SET = os.getenv("BENCHMARK_SET", "polaris")
print(f"Running benchmark set {BENCHMARK_SET}")


if __name__ == "__main__":
    try:
        output_dir = Path(sys.argv[1])
    except:
        print("usage: python evaluate.py OUTPUT_DIR")
        exit(1)
    if not output_dir.exists():
        output_dir.mkdir()
    output_file = open(output_dir / "train_results.md", "w")
    output_file.write(
        f"""# ChemProp Baseline Results
timestamp: {datetime.datetime.now()}
"""
    )
    performance_dict = {}
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
    moleculeace_benchmarks = (
        "CHEMBL1862_Ki",
        "CHEMBL1871_Ki",
        "CHEMBL2034_Ki",
        "CHEMBL2047_EC50",
        "CHEMBL204_Ki",
        "CHEMBL2147_Ki",
        "CHEMBL214_Ki",
        "CHEMBL218_EC50",
        "CHEMBL219_Ki",
        "CHEMBL228_Ki",
        "CHEMBL231_Ki",
        "CHEMBL233_Ki",
        "CHEMBL234_Ki",
        "CHEMBL235_EC50",
        "CHEMBL236_Ki",
        "CHEMBL237_EC50",
        "CHEMBL237_Ki",
        "CHEMBL238_Ki",
        "CHEMBL239_EC50",
        "CHEMBL244_Ki",
        "CHEMBL262_Ki",
        "CHEMBL264_Ki",
        "CHEMBL2835_Ki",
        "CHEMBL287_Ki",
        "CHEMBL2971_Ki",
        "CHEMBL3979_EC50",
        "CHEMBL4005_Ki",
        "CHEMBL4203_Ki",
        "CHEMBL4616_EC50",
        "CHEMBL4792_Ki",
    )

    # Initialize Mordred calculator for descriptor computation
    calc = Calculator(descriptors, ignore_3D=True)
    calc.config(timeout=1)

    for random_seed in (42, 117, 709, 1701, 9001):
        output_file.write(f"## Random Seed {random_seed}\n")
        seed_dir = output_dir / f"seed_{random_seed}"
        for benchmark_name in (
            polaris_benchmarks if BENCHMARK_SET == "polaris" else moleculeace_benchmarks
        ):
            if BENCHMARK_SET == "polaris":
                # load the benchmarking data
                benchmark = po.load_benchmark(benchmark_name)
                smiles_col = list(benchmark.input_cols)[0]
                target_cols = list(benchmark.target_cols)
                train, test = benchmark.get_train_test_split()
                train_df, test_df = train.as_dataframe(), test.as_dataframe()
                task_type = benchmark.target_types[target_cols[0]]
            else:
                smiles_col = "smiles"
                target_cols = ["y"]
                df = pd.read_csv(
                    f"https://raw.githubusercontent.com/molML/MoleculeACE/7e6de0bd2968c56589c580f2a397f01c531ede26/MoleculeACE/Data/benchmark_data/{benchmark_name}.csv"
                )
                train_df, test_df = (
                    df[df["split"] == "train"],
                    df[df["split"] == "test"],
                )
                task_type = TargetType.REGRESSION

            targets = train_df[target_cols]
            targets = targets.fillna(targets.mean(axis=0)).to_numpy()

            # Calculate Mordred descriptors for all molecules
            train_mols = [MolFromSmiles(smi) for smi in train_df[smiles_col]]
            test_mols = [MolFromSmiles(smi) for smi in test_df[smiles_col]]

            # Set molecule names to avoid issues
            for mol in train_mols:
                if mol is not None:
                    mol.SetProp("_Name", "")
            for mol in test_mols:
                if mol is not None:
                    mol.SetProp("_Name", "")

            # Calculate Mordred descriptors as extra datapoint descriptors
            train_descriptors = (
                calc.pandas(train_mols).fill_missing().to_numpy(dtype=np.float32)
            )
            test_descriptors = (
                calc.pandas(test_mols).fill_missing().to_numpy(dtype=np.float32)
            )

            # typical chemprop training
            train_idxs, val_idxs = train_test_split(
                np.arange(len(targets)),
                train_size=0.80,
                test_size=0.20,
                random_state=random_seed,
            )
            train_data = [
                MoleculeDatapoint.from_smi(smi, y, x_d=descriptors)
                for smi, y, descriptors in zip(
                    train_df[smiles_col].iloc[train_idxs],
                    targets[train_idxs],
                    train_descriptors[train_idxs],
                )
            ]
            val_data = [
                MoleculeDatapoint.from_smi(smi, y, x_d=descriptors)
                for smi, y, descriptors in zip(
                    train_df[smiles_col].iloc[val_idxs],
                    targets[val_idxs],
                    train_descriptors[val_idxs],
                )
            ]
            test_data = [
                MoleculeDatapoint.from_smi(smi, x_d=descriptors)
                for smi, descriptors in zip(test_df[smiles_col], test_descriptors)
            ]
            featurizer = SimpleMoleculeMolGraphFeaturizer()
            train_dataset = MoleculeDataset(train_data, featurizer)
            val_dataset = MoleculeDataset(val_data, featurizer)
            test_dataset = MoleculeDataset(test_data, featurizer)
            scaler = None
            if task_type == TargetType.REGRESSION:
                scaler = train_dataset.normalize_targets()
                val_dataset.normalize_targets(scaler)

            # Normalize Mordred descriptor features (extra datapoint descriptors)
            descriptor_scaler = train_dataset.normalize_inputs("X_d")
            val_dataset.normalize_inputs("X_d", descriptor_scaler)

            # Clamp descriptor values to ±6 standard deviations to handle extreme outliers
            train_dataset.X_d = np.clip(train_dataset.X_d, -6.0, 6.0)
            val_dataset.X_d = np.clip(val_dataset.X_d, -6.0, 6.0)

            train_dataloader = build_dataloader(train_dataset, num_workers=1)
            val_dataloader = build_dataloader(val_dataset, num_workers=1, shuffle=False)
            test_dataloader = build_dataloader(
                test_dataset, num_workers=1, shuffle=False
            )
            output_transform = (
                UnscaleTransform.from_standard_scaler(scaler)
                if scaler is not None
                else torch.nn.Identity()
            )

            # Create transform for extra datapoint descriptors (Mordred descriptors)
            # This combines scaling with clamping to handle extreme outliers during inference
            class ScaleAndClampTransform(torch.nn.Module):
                def __init__(self, scaler, clamp_min=-6.0, clamp_max=6.0):
                    super().__init__()
                    self.scale_transform = ScaleTransform.from_standard_scaler(scaler)
                    self.clamp_min = clamp_min
                    self.clamp_max = clamp_max

                def forward(self, x):
                    x = self.scale_transform(x)
                    return torch.clamp(x, self.clamp_min, self.clamp_max)

            X_d_transform = ScaleAndClampTransform(descriptor_scaler)

            # Training from scratch (no pretraining)
            mp = BondMessagePassing()
            agg = MeanAggregation()
            hidden_size = DEFAULT_HIDDEN_DIM

            # FFN input dimension: mp output + Mordred descriptors
            num_descriptors = train_descriptors.shape[1]
            ffn_input_dim = hidden_size + num_descriptors

            fnn = (
                RegressionFFN(
                    output_transform=output_transform,
                    input_dim=ffn_input_dim,
                    hidden_dim=hidden_size,
                )
                if task_type == TargetType.REGRESSION
                else BinaryClassificationFFN(
                    output_transform=output_transform,
                    input_dim=ffn_input_dim,
                    hidden_dim=hidden_size,
                )
            )
            model = MPNN(mp, agg, fnn, X_d_transform=X_d_transform)
            _subdir = "".join(c if c.isalnum() else "_" for c in benchmark_name)
            tensorboard_logger = TensorBoardLogger(
                seed_dir / _subdir,
                name="tensorboard_logs",
                default_hp_metric=False,
            )
            callbacks = [
                EarlyStopping(
                    monitor="val_loss",
                    mode="min",
                    verbose=False,
                    patience=5,
                ),
                ModelCheckpoint(
                    monitor="val_loss",
                    save_top_k=2,
                    mode="min",
                    dirpath=seed_dir / _subdir / "checkpoints",
                ),
            ]
            trainer = Trainer(
                max_epochs=50,
                logger=tensorboard_logger,
                log_every_n_steps=1,
                enable_checkpointing=True,
                check_val_every_n_epoch=1,
                callbacks=callbacks,
            )
            trainer.fit(model, train_dataloader, val_dataloader)
            ckpt_path = trainer.checkpoint_callback.best_model_path
            print(f"Reloading best model from checkpoint file: {ckpt_path}")
            del model, train_dataloader, train_dataset, val_dataloader, val_dataset
            torch.cuda.empty_cache()
            model = MPNN.load_from_checkpoint(ckpt_path)
            trainer = Trainer(logger=tensorboard_logger)
            predictions = (
                torch.vstack(trainer.predict(model, test_dataloader))
                .numpy(force=True)
                .flatten()
            )

            if task_type == TargetType.CLASSIFICATION:
                if BENCHMARK_SET == "polaris":
                    results = benchmark.evaluate(predictions > 0.5, predictions).results
                    performance = results.query(
                        f"Metric == '{benchmark.main_metric.label}'"
                    )["Score"].values[0]
                else:
                    # Arity check: benchmark expects an array of class predictions
                    # NOT probabilities for non-binary classification
                    results = pd.DataFrame(
                        {"metric": ["classification not supported"], "value": [None]}
                    )
                    performance = None
            elif task_type == TargetType.REGRESSION:
                if BENCHMARK_SET == "polaris":
                    results = benchmark.evaluate(predictions).results
                    performance = results.query(
                        f"Metric == '{benchmark.main_metric.label}'"
                    )["Score"].values[0]
                else:
                    results = pd.DataFrame.from_records(
                        [
                            dict(
                                metric="overall test rmse",
                                value=root_mean_squared_error(
                                    predictions, test_df["y"]
                                ),
                            ),
                            dict(
                                metric="noncliff test rmse",
                                value=root_mean_squared_error(
                                    predictions[test_df["cliff_mol"] == 0],
                                    test_df[test_df["cliff_mol"] == 0]["y"],
                                ),
                            ),
                            dict(
                                metric="cliff test rmse",
                                value=root_mean_squared_error(
                                    predictions[test_df["cliff_mol"] == 1],
                                    test_df[test_df["cliff_mol"] == 1]["y"],
                                ),
                            ),
                        ],
                        index="metric",
                    )
                    performance = {
                        "cliff": results.at["cliff test rmse", "value"],
                        "noncliff": results.at["noncliff test rmse", "value"],
                    }

            output_file.write(
                f"""
### `{benchmark_name}`

{results.to_markdown()}

"""
            )
            performance_dict[benchmark_name] = performance

            # free up the disk space
            shutil.rmtree(seed_dir / _subdir / "checkpoints")

        output_file.write(
            f"""
### Summary

```
results_dict = {json.dumps(performance_dict, indent=4)}
```
"""
        )
