"""
finetune models using the fastpropFoundation encoding as an input vector

note that polaris requires zarr<3 but the feature generator requires
zarr>=3 so two separate python environments are needed
"""
from pathlib import Path
import sys
import warnings

import torch
from mordred import Calculator, descriptors
import numpy as np
from rdkit.Chem import MolFromSmiles
import polaris as po
from polaris.utils.types import TargetType
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

from models import fastpropFoundation


warnings.filterwarnings('ignore', category=FutureWarning)


def get_pretrained_encodings(smiles, ckpt_path):
    model = fastpropFoundation.load_from_checkpoint(ckpt_path)
    model.eval()
    calc = Calculator(descriptors, ignore_3D=True)
    calc.config(timeout=1)
    mols = list(map(MolFromSmiles, smiles))
    for mol in mols:
        mol.SetProp("_Name", "")
    desc = torch.tensor(calc.pandas(mols).fill_missing().to_numpy(dtype=np.float32), dtype=torch.float32).to(device=model.device)
    enc = model.encode(desc).numpy(force=True)
    return enc
    
if __name__ == "__main__":
    try:
        ckpt_path = Path(sys.argv[1])
        output_dir = Path(sys.argv[2])
    except:
        print("usage: python pretrain.py PRETRAINED_CHECKPOINT_PATH OUTPUT_DIR")
        exit(1)
    polaris_benchmarks = [
        # "polaris/pkis2-lok-slk-cls-v2",
        # "polaris/pkis2-ret-wt-cls-v2",
        # "polaris/pkis2-ret-wt-reg-v2",
        # "polaris/pkis2-kit-wt-cls-v2",
        # "polaris/pkis2-kit-wt-reg-v2",
        # "polaris/pkis2-egfr-wt-reg-v2",
        "biogen/adme-fang-solu-reg-v1",
        "biogen/adme-fang-rppb-reg-v1",
        "biogen/adme-fang-hppb-reg-v1",
        "biogen/adme-fang-perm-reg-v1",
        "biogen/adme-fang-rclint-reg-v1",
        "biogen/adme-fang-hclint-reg-v1",
        "biogen/adme-fang-reg-v1",
        # "tdcommons/lipophilicity-astrazeneca",
        # "tdcommons/ppbr-az",
        # "tdcommons/clearance-hepatocyte-az",
        # "tdcommons/cyp2d6-substrate-carbonmangels",
        # "tdcommons/half-life-obach",
        # "tdcommons/cyp2c9-substrate-carbonmangels",
        # "tdcommons/clearance-microsome-az",
        # "tdcommons/dili",
        # "tdcommons/bioavailability-ma",
        # "tdcommons/vdss-lombardo",
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

    for benchmark_name in polaris_benchmarks:
        benchmark = po.load_benchmark(benchmark_name)
        smiles_col = list(benchmark.input_cols)[0]
        target_cols = list(benchmark.target_cols)
        train, test = benchmark.get_train_test_split()
        train_df, test_df = train.as_dataframe(), test.as_dataframe()
        encodings = get_pretrained_encodings(train_df[smiles_col], ckpt_path)
        test_encodings = get_pretrained_encodings(test_df[smiles_col], ckpt_path)
        targets = train_df[target_cols].to_numpy()
        if targets.shape[1] == 1:
            targets = targets.flatten()
        # fit a random forest model
        task_type = benchmark.target_types[target_cols[0]]
        if task_type == TargetType.CLASSIFICATION:
            rf = RandomForestClassifier()
            rf.fit(encodings, targets)
            predictions = rf.predict_proba(test_encodings)
            predictions = predictions[:, 1].flatten()
        elif task_type == TargetType.REGRESSION:
            rf = RandomForestRegressor()
            rf.fit(encodings, targets)
            predictions = rf.predict(test_encodings)
        else:
            print(f"Unknown task type {task_type}")
            exit(1)
        # run inference
        # prepare the predictions in the format polaris expects (based on # targets, reg. or class.)
        if task_type == TargetType.CLASSIFICATION:
            results = benchmark.evaluate(predictions > 0.5, predictions)
        elif task_type == TargetType.REGRESSION:
            if len(target_cols) > 1:  # only regression (?)
                predictions = {t: predictions[:, i] for i, t in enumerate(target_cols)}
            results = benchmark.evaluate(predictions)
        print(results.results)
        # save results, plot them
