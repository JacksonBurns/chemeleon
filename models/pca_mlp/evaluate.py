"""
fit a direct MLP model on PCA-reduced descriptors without pretraining
"""
from pathlib import Path
import sys
import datetime
import warnings
import json
import argparse
from typing import Tuple
from statistics import mean
import os
import pandas as pd

import torch
from astartes import train_test_split
from mordred import Calculator, descriptors
import numpy as np
from rdkit.Chem import MolFromSmiles
import polaris as po
from torch import distributed
from polaris.utils.types import TargetType
from lightning import Trainer, LightningModule
from lightning.pytorch.callbacks import ModelCheckpoint, EarlyStopping
from lightning.pytorch.loggers import TensorBoardLogger
from fastprop.data import standard_scale, inverse_standard_scale
from sklearn.decomposition import PCA
from sklearn.metrics import root_mean_squared_error

BENCHMARK_SET = os.getenv("BENCHMARK_SET", "polaris")
print(f"Running benchmark set {BENCHMARK_SET}")


warnings.filterwarnings("ignore", category=FutureWarning)


class PCAMLP(LightningModule):
    def __init__(
        self,
        input_dim: int,
        task_type: TargetType,
        hidden_sizes: Tuple[int, ...] = (1800, 1800),
        learning_rate: float = 1e-5,
        feature_means: torch.Tensor = None,
        feature_vars: torch.Tensor = None,
        pca: PCA = None,
    ):
        super().__init__()
        self.learning_rate = learning_rate
        self.task_type = task_type

        # Store standardization parameters
        self.register_buffer("feature_means", feature_means)
        self.register_buffer("feature_vars", feature_vars)

        # Save PCA transformer
        self.pca = pca

        # Build the network
        modules = []
        for i in range(len(hidden_sizes)):
            modules.append(
                torch.nn.Linear(
                    input_dim if i == 0 else hidden_sizes[i - 1], hidden_sizes[i]
                )
            )
            modules.append(torch.nn.ReLU())
        modules.append(torch.nn.Linear(hidden_sizes[-1], 1))
        if task_type == TargetType.CLASSIFICATION:
            modules.append(torch.nn.Sigmoid())

        self.model = torch.nn.Sequential(*modules)
        self.save_hyperparameters(ignore=["pca"])

    def configure_optimizers(self):
        return {"optimizer": torch.optim.Adam(self.parameters(), lr=self.learning_rate)}

    def log(self, name, value, **kwargs):
        """Wrap the parent PyTorch Lightning log function to automatically detect DDP."""
        return super().log(
            name, value, sync_dist=distributed.is_initialized(), **kwargs
        )

    def forward(self, descriptors):
        # Apply standardization
        x = standard_scale(descriptors, self.feature_means, self.feature_vars).clamp(
            min=-6, max=6
        )

        # Apply PCA if available
        if self.pca is not None:
            # Convert to numpy, apply PCA, then back to tensor
            device = x.device
            x_np = x.cpu().numpy()
            x_pca = self.pca.transform(x_np)
            x = torch.tensor(x_pca, dtype=torch.float32, device=device)

        return self.model(x)

    def _step(self, batch, name):
        descriptors, y = batch
        y_hat = self(descriptors)
        if self.task_type == TargetType.CLASSIFICATION:
            loss = torch.nn.functional.binary_cross_entropy(y_hat, y, reduction="mean")
        else:
            loss = torch.nn.functional.mse_loss(y_hat, y, reduction="mean")
        self.log(f"{name}/loss", loss)
        return loss

    def training_step(self, batch, batch_idx):
        return self._step(batch, "train")

    def validation_step(self, batch, batch_idx):
        return self._step(batch, "validation")

    def test_step(self, batch, batch_idx):
        return self._step(batch, "test")

    def predict_step(self, batch, batch_idx):
        return self(batch[0])


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Train MLP with or without PCA dimensionality reduction"
    )
    parser.add_argument("output_dir", type=str, help="Directory to save results")
    parser.add_argument(
        "--pca-method",
        type=str,
        choices=["none", "on-the-fly", "pretrained"],
        default="none",
        help="PCA method to use",
    )
    parser.add_argument(
        "--explained-variance",
        type=float,
        default=0.95,
        help="Explained variance ratio for on-the-fly PCA (0-1)",
    )
    parser.add_argument(
        "--pca-model-path",
        type=str,
        help="Path to pretrained PCA model (required for pretrained method)",
    )
    parser.add_argument("--gpu", action="store_true", help="Use GPU if available")
    args = parser.parse_args()

    # Convert hyphenated argument names to underscores for easy access
    args.pca_method = args.pca_method
    args.explained_variance = args.explained_variance
    args.pca_model_path = args.pca_model_path

    return args


if __name__ == "__main__":
    args = parse_args()
    output_dir = Path(args.output_dir)

    # Check for GPU availability and CUDA_VISIBLE_DEVICES
    gpu_available = torch.cuda.is_available()
    cuda_devices = os.environ.get("CUDA_VISIBLE_DEVICES")
    gpu_count = torch.cuda.device_count() if gpu_available else 0
    use_gpu = args.gpu and gpu_available

    print(f"GPU available: {gpu_available}")
    print(f"CUDA_VISIBLE_DEVICES: {cuda_devices}")
    print(f"GPU count: {gpu_count}")
    print(f"Using GPU: {use_gpu}")

    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    output_file = open(output_dir / "train_results.md", "w")

    # Determine title based on PCA method
    if args.pca_method == "none":
        title = "Descriptor MLP Results"
    elif args.pca_method == "on-the-fly":
        title = f"MLP on PCA-reduced Descriptors (On-the-fly, {args.explained_variance*100:.1f}% variance) Results"
    else:  # pretrained
        title = "MLP on PCA-reduced Descriptors (Pretrained PCA) Results"

    output_file.write(
        f"""# {title}
timestamp: {datetime.datetime.now()}
GPU: {use_gpu} (CUDA_VISIBLE_DEVICES={cuda_devices})
"""
    )

    # Load pretrained PCA if needed
    pretrained_pca = None
    if args.pca_method == "pretrained":
        if not args.pca_model_path:
            raise ValueError(
                "For pretrained PCA method, you must provide a PCA model path"
            )
        try:
            # Allow loading of scikit-learn PCA objects with the new PyTorch 2.6 security restrictions
            from sklearn.decomposition import PCA
            import torch.serialization

            # Explicitly add PCA to the allowlist of safe globals for deserialization
            with torch.serialization.safe_globals([PCA]):
                pretrained_pca = torch.load(args.pca_model_path, weights_only=False)

            output_file.write(
                f"Using pretrained PCA from {args.pca_model_path} with {pretrained_pca.n_components_} components\n\n"
            )

        except Exception as e:
            raise RuntimeError(f"Failed to load pretrained PCA model: {e}")

    # Define benchmarks lists
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

    calc = Calculator(descriptors, ignore_3D=True)
    calc.config(timeout=1)

    # Process benchmarks and define global PCA models outside the random seed loop
    if args.pca_method == "on-the-fly":
        global_pca_models = {}
        for benchmark_name in (
            polaris_benchmarks if BENCHMARK_SET == "polaris" else moleculeace_benchmarks
        ):
            # Load the benchmarking data first to fit PCA on entire dataset
            if BENCHMARK_SET == "polaris":
                benchmark = po.load_benchmark(benchmark_name)
                smiles_col = list(benchmark.input_cols)[0]
                train, test = benchmark.get_train_test_split()
                train_df, test_df = train.as_dataframe(), test.as_dataframe()
            else:
                smiles_col = "smiles"
                df = pd.read_csv(
                    f"https://raw.githubusercontent.com/molML/MoleculeACE/7e6de0bd2968c56589c580f2a397f01c531ede26/MoleculeACE/Data/benchmark_data/{benchmark_name}.csv"
                )
                train_df, test_df = (
                    df[df["split"] == "train"],
                    df[df["split"] == "test"],
                )

            # Process all molecules from both train and test
            all_smiles = pd.concat(
                [train_df[smiles_col], test_df[smiles_col]]
            ).reset_index(drop=True)
            all_mols = list(map(MolFromSmiles, all_smiles))
            for mol in all_mols:
                mol.SetProp("_Name", "")

            # Calculate descriptors for all molecules
            all_desc = torch.tensor(
                calc.pandas(all_mols).fill_missing().to_numpy(dtype=np.float32),
                dtype=torch.float32,
            )

            # Calculate global stats for standardization on all data
            global_desc_std, global_means, global_vars = standard_scale(all_desc)

            # Handle the special case of explained_variance = 1.0
            pca_components = args.explained_variance
            if pca_components == 1.0:
                # Use None to keep all components
                pca_components = None
                print(f"Using all components for PCA (explained_variance=1.0)")

            # Fit PCA on all data
            try:
                pca_model = PCA(n_components=pca_components, svd_solver="full")
                global_desc_std_np = global_desc_std.cpu().numpy()
                # Apply clamp before PCA fit, like in the forward() method
                global_desc_std_np = np.clip(global_desc_std_np, -6, 6)
                pca_model.fit(global_desc_std_np)

                # Get the number of components that explain the requested variance
                n_components = pca_model.n_components_

                # Log PCA details
                pca_info = f"""
### Global PCA Details for {benchmark_name}
- Original descriptor dimension: {all_desc.shape[1]}
- PCA components for {args.explained_variance*100:.1f}% variance: {n_components}
- Dimension reduction: {all_desc.shape[1] - n_components} ({(1 - n_components/all_desc.shape[1])*100:.1f}%)
- Fitted on entire dataset (train + test): {all_desc.shape[0]} molecules
"""
                output_file.write(pca_info)
                print(pca_info)

                # Save the PCA model for this benchmark
                global_pca_models[benchmark_name] = pca_model

            except Exception as e:
                print(f"Error fitting global PCA for {benchmark_name}: {e}")
                print("Will fall back to direct MLP without PCA")
                output_file.write(
                    f"\nError fitting global PCA for {benchmark_name}: {e}\nWill fall back to direct MLP without PCA\n"
                )
                global_pca_models[benchmark_name] = None

    performance_dict = {}

    for random_seed in (42, 117, 709, 1701, 9001):
        output_file.write(f"## Random Seed {random_seed}\n")
        seed_dir = output_dir / f"seed_{random_seed}"
        for benchmark_name in (
            polaris_benchmarks if BENCHMARK_SET == "polaris" else moleculeace_benchmarks
        ):
            # load the benchmarking data
            if BENCHMARK_SET == "polaris":
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

            # extract metadata, targets, and inputs
            targets = train_df[target_cols]
            targets = targets.fillna(targets.mean(axis=0)).to_numpy()
            targets = torch.tensor(targets, dtype=torch.float32)

            # Create molecules from SMILES and calculate descriptors
            train_mols = list(map(MolFromSmiles, train_df[smiles_col]))
            for mol in train_mols:
                mol.SetProp("_Name", "")
            test_mols = list(map(MolFromSmiles, test_df[smiles_col]))
            for mol in test_mols:
                mol.SetProp("_Name", "")

            # Calculate descriptors
            train_desc = torch.tensor(
                calc.pandas(train_mols).fill_missing().to_numpy(dtype=np.float32),
                dtype=torch.float32,
            )
            test_desc = torch.tensor(
                calc.pandas(test_mols).fill_missing().to_numpy(dtype=np.float32),
                dtype=torch.float32,
            )

            # Create directory for benchmark results
            _subdir = "".join(c if c.isalnum() else "_" for c in benchmark_name)
            benchmark_dir = seed_dir / _subdir
            if not benchmark_dir.exists():
                benchmark_dir.mkdir(parents=True)

            # Split data for training and validation
            train_idxs, val_idxs = train_test_split(
                np.arange(train_desc.shape[0]),
                train_size=0.80,
                random_state=random_seed,
            )

            # Standardize features
            _, feature_means, feature_vars = standard_scale(train_desc[train_idxs])

            # Apply PCA if requested
            pca_model = None
            input_dim = train_desc.shape[1]  # Original descriptor dimension

            if args.pca_method == "on-the-fly":
                # Use the global PCA model for this benchmark
                pca_model = global_pca_models.get(benchmark_name)
                if pca_model is not None:
                    input_dim = pca_model.n_components_

            elif args.pca_method == "pretrained":
                pca_model = pretrained_pca
                input_dim = pca_model.n_components_

            # Standardize targets for regression tasks
            if task_type == TargetType.REGRESSION:
                _, target_means, target_vars = standard_scale(targets[train_idxs])
                targets = standard_scale(targets, target_means, target_vars)

            # Create datasets and dataloaders
            train_dataset = torch.utils.data.TensorDataset(
                train_desc[train_idxs], targets[train_idxs]
            )
            validation_dataset = torch.utils.data.TensorDataset(
                train_desc[val_idxs], targets[val_idxs]
            )
            test_dataset = torch.utils.data.TensorDataset(test_desc)

            train_dataloader = torch.utils.data.DataLoader(
                train_dataset,
                num_workers=1,
                persistent_workers=True,
                batch_size=64,
                shuffle=True,
            )
            val_dataloader = torch.utils.data.DataLoader(
                validation_dataset,
                num_workers=1,
                batch_size=64,
                persistent_workers=True,
            )
            test_dataloader = torch.utils.data.DataLoader(
                test_dataset, num_workers=1, batch_size=64, persistent_workers=True
            )

            # Create the model
            model = PCAMLP(
                input_dim=input_dim,
                task_type=task_type,
                hidden_sizes=(1800, 1800),
                learning_rate=1e-5,
                feature_means=feature_means,
                feature_vars=feature_vars,
                pca=pca_model,
            )

            # Set up logger and callbacks
            tensorboard_logger = TensorBoardLogger(
                benchmark_dir,
                name="tensorboard_logs",
                default_hp_metric=False,
            )

            callbacks = [
                EarlyStopping(
                    monitor="validation/loss",
                    mode="min",
                    verbose=False,
                    patience=5,
                ),
                ModelCheckpoint(
                    monitor="validation/loss",
                    save_top_k=2,
                    mode="min",
                    dirpath=benchmark_dir / "checkpoints",
                ),
            ]

            # Create and train the model with GPU support if available
            if use_gpu:
                trainer = Trainer(
                    max_epochs=50,
                    logger=tensorboard_logger,
                    log_every_n_steps=1,
                    enable_checkpointing=True,
                    check_val_every_n_epoch=1,
                    callbacks=callbacks,
                    accelerator="gpu",
                    devices=1,
                )
            else:
                trainer = Trainer(
                    max_epochs=50,
                    logger=tensorboard_logger,
                    log_every_n_steps=1,
                    enable_checkpointing=True,
                    check_val_every_n_epoch=1,
                    callbacks=callbacks,
                    accelerator="cpu",
                )

            trainer.fit(model, train_dataloader, val_dataloader)

            # Load the best model for prediction
            ckpt_path = trainer.checkpoint_callback.best_model_path
            print(f"Reloading best model from checkpoint file: {ckpt_path}")
            model = model.__class__.load_from_checkpoint(
                ckpt_path, map_location="cpu", pca=pca_model
            )

            # Make predictions with the same accelerator configuration
            if use_gpu:
                trainer = Trainer(
                    logger=tensorboard_logger,
                    accelerator="gpu",
                    devices=1,
                )
            else:
                trainer = Trainer(
                    logger=tensorboard_logger,
                    accelerator="cpu",
                )
            predictions = torch.vstack(trainer.predict(model, test_dataloader))

            # Inverse transform predictions for regression tasks
            if task_type == TargetType.REGRESSION:
                predictions = inverse_standard_scale(
                    predictions, target_means, target_vars
                )

            predictions = predictions.numpy(force=True).flatten()

            # Evaluate the model
            if BENCHMARK_SET == "polaris":
                if task_type == TargetType.CLASSIFICATION:
                    results = benchmark.evaluate(predictions > 0.5, predictions).results
                    performance = results.query(
                        f"Metric == '{benchmark.main_metric.label}'"
                    )["Score"].values[0]
                else:
                    results = benchmark.evaluate(predictions).results
                    performance = results.query(
                        f"Metric == '{benchmark.main_metric.label}'"
                    )["Score"].values[0]
            else:
                # For MoleculeACE benchmarks, use the same format as in descriptor_mlp/evaluate.py
                results = pd.DataFrame.from_records(
                    [
                        dict(
                            metric="overall test rmse",
                            value=root_mean_squared_error(predictions, test_df["y"]),
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

            # Write results
            output_file.write(
                f"""
### `{benchmark_name}`

{results.to_markdown()}

"""
            )
            performance_dict[benchmark_name] = performance

        output_file.write(
            f"""
### Summary

```
results_dict = {json.dumps(performance_dict, indent=4)}
```
"""
        )
