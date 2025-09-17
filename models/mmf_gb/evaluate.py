from pathlib import Path
import sys
import datetime
import json
import warnings
import os

import polaris as po
from polaris.utils.types import TargetType

from scikit_mol.conversions import SmilesToMolTransformer
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import TransformedTargetRegressor
from sklearn.metrics import root_mean_squared_error
import pandas as pd

from mmf.mmf_transform import MolFingerprintTransformer

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

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
        f"""# Random Forest Baseline Results
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

                # extract metadata, targets, and inputs
                task_type = benchmark.target_types[target_cols[0]]
                targets = train_df[target_cols]
                targets = targets.fillna(targets.mean(axis=0)).to_numpy().ravel()
                train_smiles = train_df[smiles_col]
                test_smiles = test_df[smiles_col]
            else:
                df = pd.read_csv(
                    f"https://raw.githubusercontent.com/molML/MoleculeACE/7e6de0bd2968c56589c580f2a397f01c531ede26/MoleculeACE/Data/benchmark_data/{benchmark_name}.csv"
                )
                train_df, test_df = (
                    df[df["split"] == "train"],
                    df[df["split"] == "test"],
                )

                # extract metadata, targets, and inputs
                task_type = TargetType.REGRESSION
                targets = train_df["y"].to_numpy().ravel()
                train_smiles = train_df["smiles"]
                test_smiles = test_df["smiles"]

            # typical scikit-mol training
            if task_type == TargetType.REGRESSION:
                model = TransformedTargetRegressor(
                    regressor=GradientBoostingRegressor(random_state=random_seed),
                    transformer=StandardScaler(),
                )
            else:
                model = GradientBoostingClassifier(random_state=random_seed)
            pipe = Pipeline(
                [
                    ("smiles2mol", SmilesToMolTransformer()),
                    ("mol2fp", MolFingerprintTransformer()),
                    ("model", model),
                ]
            )
            pipe.fit(train_smiles, targets)

            # prepare the predictions in the format polaris expects
            if task_type == TargetType.CLASSIFICATION:
                predictions = pipe.predict_proba(test_smiles)[:, 1].flatten()
                results = benchmark.evaluate(predictions > 0.5, predictions).results
                performance = results.query(
                    f"Metric == '{benchmark.main_metric.label}'"
                )["Score"].values[0]
            elif task_type == TargetType.REGRESSION:
                predictions = pipe.predict(test_smiles).flatten()
                # if len(target_cols) > 1:  # if there were multitask
                #     predictions = {t: predictions[:, i] for i, t in enumerate(target_cols)}
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

        output_file.write(
            f"""
### Summary

```
results_dict = {json.dumps(performance_dict, indent=4)}
```
"""
        )
