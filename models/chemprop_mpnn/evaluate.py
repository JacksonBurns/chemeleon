"""
fit a chemprop model directly on the smiles

note that polaris requires zarr<3 but the feature generator requires
zarr>=3 so two separate python environments are needed
"""
from pathlib import Path
import sys
import datetime
import json

import torch
from mordred import Calculator, descriptors
import polaris as po
from polaris.utils.types import TargetType
from lightning import Trainer
from lightning.pytorch.callbacks import ModelCheckpoint, EarlyStopping
from lightning.pytorch.loggers import TensorBoardLogger
from astartes import train_test_split

from chemprop.data import MoleculeDatapoint, MoleculeDataset, build_dataloader
from chemprop.featurizers import SimpleMoleculeMolGraphFeaturizer
from chemprop.conf import DEFAULT_HIDDEN_DIM
from chemprop.nn import BondMessagePassing, BinaryClassificationFFN, RegressionFFN, UnscaleTransform
from chemprop.models import MPNN
from chemprop.nn.agg import MeanAggregation

from pretrain import MaskedDescriptorsMPNN, WinsorizeStdevN


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
    output_file.write(f"""# ChemProp Baseline Results
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

            # typical chemprop training
            train_idxs, val_idxs = train_test_split(range(len(targets)), train_size=0.80, test_size=0.20, random_state=random_seed)
            train_data = [MoleculeDatapoint.from_smi(smi, y) for smi, y in zip(train_df[smiles_col][train_idxs], targets[train_idxs])]
            val_data = [MoleculeDatapoint.from_smi(smi, y) for smi, y in zip(train_df[smiles_col][val_idxs], targets[val_idxs])]
            test_data = list(map(MoleculeDatapoint.from_smi, test_df[smiles_col]))
            featurizer = SimpleMoleculeMolGraphFeaturizer()
            train_dataset = MoleculeDataset(train_data, featurizer)
            val_dataset = MoleculeDataset(val_data, featurizer)
            test_dataset = MoleculeDataset(test_data, featurizer)
            scaler = None
            if task_type == TargetType.REGRESSION:
                scaler = train_dataset.normalize_targets()
                val_dataset.normalize_targets(scaler)
            train_dataloader = build_dataloader(train_dataset, num_workers=1)
            val_dataloader = build_dataloader(val_dataset, num_workers=1, shuffle=False)
            test_dataloader = build_dataloader(test_dataset, num_workers=1, shuffle=False)
            output_transform = UnscaleTransform.from_standard_scaler(scaler) if scaler is not None else torch.nn.Identity()
            if pretrain_pt is None:
                mp = BondMessagePassing()
                agg = MeanAggregation()
                hidden_size = DEFAULT_HIDDEN_DIM
            else:
                pretrained: MaskedDescriptorsMPNN = torch.load(pretrain_pt, map_location="cpu", weights_only=False)
                mp = pretrained.message_passing
                agg = pretrained.agg
                hidden_size = pretrained.message_passing.output_dim
            fnn = RegressionFFN(output_transform=output_transform, input_dim=hidden_size) if task_type == TargetType.REGRESSION else BinaryClassificationFFN(output_transform=output_transform, input_dim=hidden_size)
            model = MPNN(mp, agg, fnn)
            
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
            del model, train_dataloader, train_dataset, val_dataloader, val_dataset
            torch.cuda.empty_cache()
            model = MPNN.load_from_checkpoint(ckpt_path)
            trainer = Trainer(logger=tensorboard_logger)
            predictions = torch.vstack(trainer.predict(model, test_dataloader)).numpy(force=True).flatten()
            
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
