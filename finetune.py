from pathlib import Path
import sys

import torch
from mordred import Calculator, descriptors
import numpy as np
from rdkit.Chem import MolFromSmiles
import polaris as po

from .models import fastpropFoundation


def get_pretrained_encodings(smiles, ckpt_path):
    calc = Calculator(descriptors, ignore_3D=True)
    calc.config(timeout=1)
    mols = list(map(MolFromSmiles, smiles))
    for mol in mols:
        mol.SetProp("_Name", "")
    desc = torch.tensor(calc.pandas(mols).fill_missing().to_numpy(dtype=np.float32), dtype=torch.float32)
    model = fastpropFoundation.load_from_checkpoint(ckpt_path)
    model.eval()
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
        "polaris/pkis2-lok-slk-cls-v2",
        "polaris/pkis2-ret-wt-cls-v2",
        "polaris/pkis2-ret-wt-reg-v2",
        "polaris/pkis2-kit-wt-cls-v2",
        "polaris/pkis2-kit-wt-reg-v2",
        "polaris/pkis2-egfr-wt-reg-v2",
        "biogen/adme-fang-solu-reg-v1",
        "biogen/adme-fang-rppb-reg-v1",
        "biogen/adme-fang-hppb-reg-v1",
        "biogen/adme-fang-perm-reg-v1",
        "biogen/adme-fang-rclint-reg-v1",
        "biogen/adme-fang-hclint-reg-v1",
        "biogen/adme-fang-reg-v1",
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
        "tdcommons/cyp2d6-veith",
        "tdcommons/solubility-aqsoldb",
        "tdcommons/cyp3a4-veith",
        "tdcommons/ames",
        "tdcommons/ld50-zhu",
    ]

    for benchmark_name in polaris_benchmarks:
        benchmark = po.load_benchmark(benchmark_name)
        train, test = benchmark.get_train_test_split()
        train_df, test_df = train.as_dataframe(), test.as_dataframe()
        encodings = get_pretrained_encodings(train_df["smiles"], ckpt_path)
        targets = train_df[list(benchmark.target_cols)]
        # fit a random forest model
        rf = None
        encodings = get_pretrained_encodings(test_df["smiles"], ckpt_path)
        pred = rf.predict(encodings)
        # prepare the predictions in the format polaris expects (based on # targets, reg. or class.
        predictions = None
        results = benchmark.evaluate(...)
        # save results, plot them
        
        

