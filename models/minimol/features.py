from pathlib import Path

import polaris as po
import pandas as pd
import numpy as np
from minimol import Minimol


if __name__ == "__main__":
    all_benchmarks = (
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
    model = Minimol()
    outdir = Path("minimol_features")
    outdir.mkdir(exist_ok=True)
    for benchmark_name in all_benchmarks:
        if "/" in benchmark_name:
            # load the benchmarking data
            benchmark = po.load_benchmark(benchmark_name)
            smiles_col = list(benchmark.input_cols)[0]
            train, test = benchmark.get_train_test_split()
            train_df, test_df = train.as_dataframe(), test.as_dataframe()
            smiles = train_df[smiles_col].to_list() + test_df[smiles_col].to_list()
            outname = benchmark_name.split("/")[1]
        else:
            smiles_col = "smiles"
            df = pd.read_csv(f"https://raw.githubusercontent.com/molML/MoleculeACE/7e6de0bd2968c56589c580f2a397f01c531ede26/MoleculeACE/Data/benchmark_data/{benchmark_name}.csv")
            smiles = df["smiles"].to_list()
            outname = benchmark_name
        # calculate the features with model(smiles) -> may need to batch, or just run individually?
        features = [t.tolist() for t in model(smiles)]
        # save df of SMILES and features into a df, write to parquet
        df = pd.DataFrame(data=features, columns=[f'feature_{i}' for i in range(512)], index=smiles)
        df.to_parquet(outdir / (outname + ".parquet"))
