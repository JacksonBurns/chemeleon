"""
fit a chemprop model directly on the smiles

note that polaris requires zarr<3 but the feature generator requires
zarr>=3 so two separate python environments are needed
"""
from pathlib import Path
import sys
import datetime
import warnings
import json
from typing import Tuple
from statistics import mean

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

from models import fastpropFoundation


warnings.filterwarnings('ignore', category=FutureWarning)

class RescalingEncoder(torch.nn.Module):
    def __init__(self, feature_means, feature_vars):
        super().__init__()
        self.register_buffer("feature_means", feature_means)
        self.register_buffer("feature_vars", feature_vars)
    
    def encode(self, x):
        return standard_scale(x, self.feature_means, self.feature_vars)


class FineTuner(LightningModule):
    def __init__(
        self,
        encoder: torch.nn.Module,
        input_dim: int,
        task_type: TargetType,
        hidden_sizes: Tuple[int, ...] = (1024,),
        learning_rate: float = 0.0001,
    ):
        super().__init__()
        self.encoder: fastpropFoundation = encoder
        self.learning_rate = learning_rate
        modules = []
        for i in range(len(hidden_sizes)):
            modules.append(torch.nn.Linear(input_dim if i == 0 else hidden_sizes[i], hidden_sizes[i]))
            modules.append(torch.nn.ReLU())
        modules.append(torch.nn.Linear(hidden_sizes[-1], 1))
        if task_type == TargetType.CLASSIFICATION:
            modules.append(torch.nn.Sigmoid())
        self.task_type = task_type
        self.fnn = torch.nn.Sequential(*modules)
        self.save_hyperparameters()
    
    def configure_optimizers(self):
        return {"optimizer": torch.optim.Adam(self.parameters(), lr=self.learning_rate)}

    def log(self, name, value, **kwargs):
        """Wrap the parent PyTorch Lightning log function to automatically detect DDP."""
        return super().log(name, value, sync_dist=distributed.is_initialized(), **kwargs)

    def forward(self, descriptors):
        return self.fnn(self.encoder.encode(descriptors))

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

if __name__ == "__main__":
    try:
        output_dir = Path(sys.argv[1])
        pretrain_pt = None
        if len(sys.argv) == 3:
            pretrain_pt = Path(sys.argv[2])
    except:
        print("usage: python evaluate.py OUTPUT_DIR [PRETRAIN_PT]")
        exit(1)
    if not output_dir.exists():
        output_dir.mkdir()
    output_file = open(output_dir / "train_results.md", "w")
    output_file.write(f"""# Descriptor MLP Results
timestamp: {datetime.datetime.now()}
""")
    performance_dict = {}
    polaris_benchmarks = [
        "polaris/pkis2-ret-wt-cls-v2",
        # "polaris/pkis2-ret-wt-reg-v2",
        # "polaris/pkis2-kit-wt-cls-v2",
        # "polaris/pkis2-kit-wt-reg-v2",
        # "polaris/pkis2-egfr-wt-reg-v2",
        "polaris/adme-fang-solu-1",
        "polaris/adme-fang-rppb-1",
        "polaris/adme-fang-hppb-1",
        "polaris/adme-fang-perm-1",
        "polaris/adme-fang-rclint-1",
        "polaris/adme-fang-hclint-1",
        # "tdcommons/lipophilicity-astrazeneca",
        # "tdcommons/ppbr-az",
        # "tdcommons/clearance-hepatocyte-az",
        # "tdcommons/cyp2d6-substrate-carbonmangels",
        # "tdcommons/half-life-obach",
        # "tdcommons/cyp2c9-substrate-carbonmangels",
        "tdcommons/clearance-microsome-az",
        "tdcommons/dili",
        "tdcommons/bioavailability-ma",
        "tdcommons/vdss-lombardo",
        # "tdcommons/cyp3a4-substrate-carbonmangels",
        # "tdcommons/pgp-broccatelli",
        # "tdcommons/caco2-wang",
        "tdcommons/herg",
        # "tdcommons/bbb-martins",
        # "tdcommons/cyp2d6-veith",
        # "tdcommons/solubility-aqsoldb",
        # "tdcommons/cyp3a4-veith",
        # "tdcommons/ames",
        # "tdcommons/ld50-zhu",
    ]

    calc = Calculator(descriptors, ignore_3D=True)
    calc.config(timeout=1)
    for random_seed in (42, 117, 709, 1701, 9001):
        output_file.write(f"## Random Seed {random_seed}\n")
        seed_dir = output_dir / f"seed_{random_seed}"
        for benchmark_name in polaris_benchmarks:
            # load the benchmarking data
            benchmark = po.load_benchmark(benchmark_name)
            smiles_col = list(benchmark.input_cols)[0]
            target_cols = list(benchmark.target_cols)
            train, test = benchmark.get_train_test_split()
            train_df, test_df = train.as_dataframe(), test.as_dataframe()

            # extract metadata, targets, and inputs
            task_type = benchmark.target_types[target_cols[0]]
            targets = train_df[target_cols]
            targets = targets.fillna(targets.mean(axis=0)).to_numpy()

            # typical fastprop training
            task_type = benchmark.target_types[target_cols[0]]
            targets = train_df[target_cols]
            targets = targets.fillna(targets.mean(axis=0)).to_numpy()
            targets = torch.tensor(targets, dtype=torch.float32)
            train_mols = list(map(MolFromSmiles, train_df[smiles_col]))
            for mol in train_mols:
                mol.SetProp("_Name", "")
            test_mols = list(map(MolFromSmiles, test_df[smiles_col]))
            for mol in test_mols:
                mol.SetProp("_Name", "")
            train_desc = torch.tensor(calc.pandas(train_mols).fill_missing().to_numpy(dtype=np.float32), dtype=torch.float32)
            test_desc = torch.tensor(calc.pandas(test_mols).fill_missing().to_numpy(dtype=np.float32), dtype=torch.float32)
            _subdir = "".join(c if c.isalnum() else "_" for c in benchmark_name)
            train_idxs, val_idxs = train_test_split(np.arange(train_desc.shape[0]), train_size=0.80, random_state=random_seed)
            if task_type == TargetType.REGRESSION:
                _, target_means, target_vars = standard_scale(targets[train_idxs])
                targets = standard_scale(targets, target_means, target_vars)
            train_dataset = torch.utils.data.TensorDataset(train_desc[train_idxs], targets[train_idxs])
            validation_dataset = torch.utils.data.TensorDataset(train_desc[val_idxs], targets[val_idxs])
            test_dataset = torch.utils.data.TensorDataset(test_desc)
            train_dataloader = torch.utils.data.DataLoader(train_dataset, num_workers=1, persistent_workers=True, batch_size=64, shuffle=True)
            val_dataloader = torch.utils.data.DataLoader(validation_dataset, num_workers=1, batch_size=64, persistent_workers=True)
            test_dataloader = torch.utils.data.DataLoader(test_dataset, num_workers=1, batch_size=64, persistent_workers=True)
            if pretrain_pt is None:
                _, feature_means, feature_vars = standard_scale(train_desc[train_idxs])
                encoder = RescalingEncoder(feature_means, feature_vars)
                input_size = feature_means.shape[0]
            else:
                encoder: fastpropFoundation = torch.load(pretrain_pt, map_location="cpu", weights_only=False)
                input_size = encoder.encoder[-1].out_features
            model = FineTuner(encoder, input_size, task_type, (128, 128), learning_rate=1e-5)
            tensorboard_logger = TensorBoardLogger(
                seed_dir / _subdir,
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
                    dirpath=seed_dir  / _subdir / "checkpoints",
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
            model = model.__class__.load_from_checkpoint(ckpt_path, map_location="cpu")
            trainer = Trainer(logger=tensorboard_logger)
            predictions = torch.vstack(trainer.predict(model, test_dataloader))
            if task_type == TargetType.REGRESSION:
                predictions = inverse_standard_scale(predictions, target_means, target_vars)
            predictions = predictions.numpy(force=True).flatten()
            
            # prepare the predictions in the format polaris expects
            if task_type == TargetType.CLASSIFICATION:
                results = benchmark.evaluate(predictions > 0.5, predictions)
            elif task_type == TargetType.REGRESSION:
                # if len(target_cols) > 1:  # if there were multitask
                #     predictions = {t: predictions[:, i] for i, t in enumerate(target_cols)}
                results = benchmark.evaluate(predictions)
            output_file.write(f"""
### `{benchmark_name}`

{results.results.to_markdown()}

""")
            performance = results.results.query(f"Metric == '{benchmark.main_metric.label}'")['Score'].values[0]
            performance_dict[benchmark_name] = performance

            # actually free the memory
            del model, test_dataloader, test_dataset
            torch.cuda.empty_cache()
        
        output_file.write(f"""
### Summary

```
results_dict = {json.dumps(performance_dict, indent=4)}
```
""")
