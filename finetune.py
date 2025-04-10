"""
finetune models using the fastpropFoundation encoding as an input vector

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


class UnsupervisedDataset(torch.utils.data.Dataset):
    def __init__(self, features: torch.Tensor):
        self.features = features
        self.len = features.shape[0]

    def __len__(self):
        return self.len

    def __getitem__(self, batch_idx: list[int]):
        return self.features[batch_idx]


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


class SkipConnectionFineTuner(FineTuner):
    def __init__(
        self,
        encoder: torch.nn.Module,
        input_dim: int,
        task_type: TargetType,
        feature_means: torch.Tensor,
        feature_vars: torch.Tensor,
        hidden_sizes: Tuple[int, ...] = (1024,),
        learning_rate: float = 0.0001,
    ):
        super().__init__(encoder, input_dim, task_type, hidden_sizes, learning_rate)
        self.register_buffer("feature_means", feature_means)
        self.register_buffer("feature_vars", feature_vars)
        self.save_hyperparameters()

    def forward(self, descriptors):
        x_1 = self.encoder.encode(descriptors)
        x_2 = standard_scale(descriptors, self.feature_means, self.feature_vars)
        return self.fnn(torch.cat((x_1, x_2), dim=1))


if __name__ == "__main__":
    try:
        pt_path = Path(sys.argv[1])
        output_dir = Path(sys.argv[2])
    except:
        print("usage: python finetune.py PRETRAINED_CHECKPOINT_PATH OUTPUT_DIR")
        exit(1)
    if not output_dir.exists():
        output_dir.mkdir()
    output_file = open(output_dir / "finetune_results.md", "w")
    encoder: fastpropFoundation = torch.load(pt_path, weights_only=False)
    output_file.write(f"""# `fastprop` Finetuning Results
timestamp: {datetime.datetime.now()}
pretrained model: {pt_path}
{encoder}
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
    for benchmark_name in polaris_benchmarks:
        _subdir = "".join(c if c.isalnum() else "_" for c in benchmark_name)
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
        targets = torch.tensor(targets, dtype=torch.float32)
        train_mols = list(map(MolFromSmiles, train_df[smiles_col]))
        for mol in train_mols:
            mol.SetProp("_Name", "")
        test_mols = list(map(MolFromSmiles, test_df[smiles_col]))
        for mol in test_mols:
            mol.SetProp("_Name", "")
        train_desc = torch.tensor(calc.pandas(train_mols).fill_missing().to_numpy(dtype=np.float32), dtype=torch.float32)
        test_desc = torch.tensor(calc.pandas(test_mols).fill_missing().to_numpy(dtype=np.float32), dtype=torch.float32)

        initial_error = 0.0
        tuned_error = 0.0
        # fine tuning stage 1 - unsupervised
        # all_desc = torch.cat((train_desc, test_desc))
        # train_idxs, val_idxs = train_test_split(range(all_desc.shape[0]), train_size=0.80, test_size=0.20, random_state=1701)
        # _, feature_means, feature_vars = standard_scale(all_desc[train_idxs])
        # train_dataset = UnsupervisedDataset(all_desc[train_idxs])
        # validation_dataset = UnsupervisedDataset(all_desc[val_idxs])
        # train_dataloader = torch.utils.data.DataLoader(train_dataset, num_workers=1, persistent_workers=True, batch_size=64, shuffle=True)
        # val_dataloader = torch.utils.data.DataLoader(validation_dataset, num_workers=1, batch_size=64, persistent_workers=True)
        model: fastpropFoundation = torch.load(pt_path, weights_only=False)
        # model = fastpropFoundation(
        #     feature_means=feature_means,
        #     feature_vars=feature_vars,
        #     num_features=train_desc.shape[1],
        #     winsorization_factor=6,
        #     hidden_sizes=(1024, 1024, 1024),
        #     decoder_sizes=tuple(),
        #     encoding_size=1_024,
        #     learning_rate=1e-4,
        #     masking_ratio=0.15,
        #     embedding_dim=4,
        # )
        # unsupervised_output = output_dir / _subdir / "unsupervised"
        # tensorboard_logger = TensorBoardLogger(
        #     unsupervised_output,
        #     name="tensorboard_logs",
        #     default_hp_metric=False,
        # )
        # callbacks = [
        #     EarlyStopping(
        #         monitor="validation/loss",
        #         mode="min",
        #         verbose=False,
        #         patience=50,
        #     ),
        #     ModelCheckpoint(
        #         monitor="validation/loss",
        #         save_top_k=2,
        #         mode="min",
        #         dirpath=unsupervised_output / "checkpoints",
        #     ),
        # ]
        # callbacks[1].STARTING_VERSION = 0
        # trainer = Trainer(
        #     max_epochs=500,
        #     logger=tensorboard_logger,
        #     log_every_n_steps=1,
        #     enable_checkpointing=True,
        #     check_val_every_n_epoch=1,
        #     callbacks=callbacks,
        # )
        # initial_error = trainer.validate(model, val_dataloader)[0]['validation/loss']
        # trainer.fit(model, train_dataloader, val_dataloader)
        # ckpt_path = trainer.checkpoint_callback.best_model_path
        # print(f"Reloading best model from checkpoint file: {ckpt_path}")
        # encoder = fastpropFoundation.load_from_checkpoint(ckpt_path, map_location="cpu")
        # tuned_error = trainer.validate(encoder, val_dataloader)[0]['validation/loss']

        # part 2 - supervised training
        supervised_output = output_dir / _subdir / "supervised"
        
        # fit model
        train_idxs, val_idxs = train_test_split(np.arange(train_desc.shape[0]), train_size=0.80, random_state=1701)
        _, feature_means, feature_vars = standard_scale(train_desc[train_idxs])   # only used for skip connection
        if task_type == TargetType.REGRESSION:
            _, target_means, target_vars = standard_scale(targets[train_idxs])
            targets = standard_scale(targets, target_means, target_vars)
        train_dataset = torch.utils.data.TensorDataset(train_desc[train_idxs], targets[train_idxs])
        validation_dataset = torch.utils.data.TensorDataset(train_desc[val_idxs], targets[val_idxs])
        test_dataset = torch.utils.data.TensorDataset(test_desc)
        train_dataloader = torch.utils.data.DataLoader(train_dataset, num_workers=1, persistent_workers=True, batch_size=64, shuffle=True)
        val_dataloader = torch.utils.data.DataLoader(validation_dataset, num_workers=1, batch_size=64, persistent_workers=True)
        test_dataloader = torch.utils.data.DataLoader(test_dataset, num_workers=1, batch_size=64, persistent_workers=True)
    
        # build the fine tuner
        model = FineTuner(encoder, 4_096, task_type, (128, 128), learning_rate=1e-5)
        # model = SkipConnectionFineTuner(
        #     encoder=encoder,
        #     input_dim=4_096 + 1_613,
        #     task_type=task_type,
        #     feature_means=feature_means,
        #     feature_vars=feature_vars,
        #     hidden_sizes=[128, 128],
        #     learning_rate=1e-5,
        # ) 
        tensorboard_logger = TensorBoardLogger(
            supervised_output,
            name="tensorboard_logs",
            default_hp_metric=False,
        )
        callbacks = [
            EarlyStopping(
                monitor="validation/loss",
                mode="min",
                verbose=False,
                patience=10,
            ),
            ModelCheckpoint(
                monitor="validation/loss",
                save_top_k=2,
                mode="min",
                dirpath=supervised_output / "checkpoints",
            ),
        ]
        callbacks[1].STARTING_VERSION = 0
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
## `{benchmark_name}`

Pre-trained Encoder Reconstruction Error: {initial_error:.4f}
Fine-tuned Encoder Reconstruction Error: {tuned_error:.4f}

{results.results.to_markdown()}

""")
        performance = results.results.query(f"Metric == '{benchmark.main_metric.label}'")['Score'].values[0]
        performance_dict[benchmark_name] = performance

        # actually free the memory
        del model, test_dataloader, test_dataset
        torch.cuda.empty_cache()
    
    output_file.write(f"""
# Summary

```
results_dict = {json.dumps(performance_dict, indent=4)}
```
""")
