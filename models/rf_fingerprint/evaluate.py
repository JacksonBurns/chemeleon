from pathlib import Path
import sys
import datetime
import json
import warnings

import polaris as po
from polaris.utils.types import TargetType

from scikit_mol.conversions import SmilesToMolTransformer
from scikit_mol.fingerprints import MorganFingerprintTransformer
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import TransformedTargetRegressor

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)



if __name__ == "__main__":
    try:
        output_dir = Path(sys.argv[1])
    except:
        print("usage: python evaluate.py OUTPUT_DIR")
        exit(1)
    if not output_dir.exists():
        output_dir.mkdir()
    output_file = open(output_dir / "train_results.md", "w")
    output_file.write(f"""# Random Forest Baseline Results
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
            targets = targets.fillna(targets.mean(axis=0)).to_numpy().ravel()
            train_smiles = train_df[smiles_col]
            test_smiles = test_df[smiles_col]

            # typical scikit-mol training
            if task_type == TargetType.REGRESSION:
                model = TransformedTargetRegressor(regressor=RandomForestRegressor(random_state=random_seed), transformer=StandardScaler())
            else:
                model = RandomForestClassifier(random_state=random_seed)
            pipe = Pipeline(
                [
                    ('smiles2mol', SmilesToMolTransformer()),
                    ('mol2fp', MorganFingerprintTransformer()),
                    ('model', model),
                ]
            )
            pipe.fit(train_smiles, targets)
            
            # prepare the predictions in the format polaris expects
            if task_type == TargetType.CLASSIFICATION:
                predictions = pipe.predict_proba(test_smiles)[:, 1].flatten()
                results = benchmark.evaluate(predictions > 0.5, predictions)
            elif task_type == TargetType.REGRESSION:
                predictions = pipe.predict(test_smiles).flatten()
                # if len(target_cols) > 1:  # if there were multitask
                #     predictions = {t: predictions[:, i] for i, t in enumerate(target_cols)}
                results = benchmark.evaluate(predictions)
            output_file.write(f"""
### `{benchmark_name}`

{results.results.to_markdown()}

""")
            performance = results.results.query(f"Metric == '{benchmark.main_metric.label}'")['Score'].values[0]
            performance_dict[benchmark_name] = performance
        
        output_file.write(f"""
### Summary

```
results_dict = {json.dumps(performance_dict, indent=4)}
```
""")
