import datetime
import json
import os
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import polaris as po
import torch
from fastprop.data import inverse_standard_scale, standard_scale
from mordred import Calculator, descriptors
from polaris.utils.types import TargetType
from rdkit.Chem import MolFromSmiles
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import root_mean_squared_error

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

BENCHMARK_SET = os.getenv("BENCHMARK_SET", "polaris")
print(f"Running benchmark set {BENCHMARK_SET}")

# Initialize the Mordred calculator once for efficiency
descriptor_calculator = Calculator(descriptors, ignore_3D=True)
descriptor_calculator.config(timeout=1)

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
        if not seed_dir.exists():
            seed_dir.mkdir()

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

            # Convert molecules to descriptors first, matching how the MLP script processes data
            train_mols = list(map(MolFromSmiles, train_smiles))
            test_mols = list(map(MolFromSmiles, test_smiles))

            # Set molecule names to empty strings as in the MLP script
            for mol in train_mols:
                mol.SetProp("_Name", "")
            for mol in test_mols:
                mol.SetProp("_Name", "")

            # Calculate descriptors using the global calculator
            train_desc = (
                descriptor_calculator.pandas(train_mols)
                .fill_missing()
                .to_numpy(dtype=np.float32)
            )
            test_desc = (
                descriptor_calculator.pandas(test_mols)
                .fill_missing()
                .to_numpy(dtype=np.float32)
            )

            # Convert to torch tensors for use with standard_scale
            train_desc_tensor = torch.tensor(train_desc, dtype=torch.float32)
            targets_tensor = torch.tensor(targets, dtype=torch.float32).reshape(-1, 1)

            # Scale features and targets as in the MLP script
            if task_type == TargetType.REGRESSION:
                _, target_means, target_vars = standard_scale(targets_tensor)
                targets_scaled = (
                    standard_scale(targets_tensor, target_means, target_vars)
                    .numpy()
                    .ravel()
                )
                targets = targets_scaled

            # Feature scaling - exactly as in the MLP script with clamping as in RescalingEncoder
            _, feature_means, feature_vars = standard_scale(train_desc_tensor)
            train_desc = (
                standard_scale(train_desc_tensor, feature_means, feature_vars)
                .clamp(min=-6, max=6)
                .numpy()
            )
            test_desc_tensor = torch.tensor(test_desc, dtype=torch.float32)
            test_desc = (
                standard_scale(test_desc_tensor, feature_means, feature_vars)
                .clamp(min=-6, max=6)
                .numpy()
            )

            # Create and train model
            if task_type == TargetType.REGRESSION:
                model = RandomForestRegressor(random_state=random_seed)
            else:
                model = RandomForestClassifier(random_state=random_seed)

            # Train model directly on the descriptors
            model.fit(train_desc, targets)

            # generate predictions and evaluate performance
            print(f"Evaluating benchmark: {benchmark_name}")

            if task_type == TargetType.CLASSIFICATION:
                # Get probability predictions for classification tasks
                predictions = model.predict_proba(test_desc)[:, 1].flatten()
                results = benchmark.evaluate(predictions > 0.5, predictions).results
                performance = results.query(
                    f"Metric == '{benchmark.main_metric.label}'"
                )["Score"].values[0]
            elif task_type == TargetType.REGRESSION:
                # Get value predictions for regression tasks
                predictions = model.predict(test_desc).flatten()
                # Inverse transform the predictions using the same scaling approach as in the MLP script
                predictions_tensor = torch.tensor(
                    predictions, dtype=torch.float32
                ).reshape(-1, 1)
                predictions = (
                    inverse_standard_scale(
                        predictions_tensor, target_means, target_vars
                    )
                    .numpy()
                    .ravel()
                )

                if BENCHMARK_SET == "polaris":
                    results = benchmark.evaluate(predictions).results
                    performance = results.query(
                        f"Metric == '{benchmark.main_metric.label}'"
                    )["Score"].values[0]
                else:
                    # MoleculeACE evaluation metrics
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
