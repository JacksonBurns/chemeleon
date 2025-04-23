from pathlib import Path
import sys
import datetime
import json
import warnings

import pandas as pd
from scikit_mol.conversions import SmilesToMolTransformer
from scikit_mol.fingerprints import MorganFingerprintTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import TransformedTargetRegressor
from sklearn.metrics import root_mean_squared_error
from tqdm import tqdm

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
    output_file = open(output_dir / "moleculeace_results.md", "w")
    output_file.write(f"""# Random Forest Baseline Results
timestamp: {datetime.datetime.now()}
""")
    performance_dict = {}
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
        for benchmark_name in tqdm(moleculeace_benchmarks, f"Running MoleculeACE Benchmarks ({random_seed=})"):
            # load the benchmarking data
            df = pd.read_csv(f"https://raw.githubusercontent.com/molML/MoleculeACE/7e6de0bd2968c56589c580f2a397f01c531ede26/MoleculeACE/Data/benchmark_data/{benchmark_name}.csv")
            train_df, test_df = df[df["split"] == "train"], df[df["split"] == "test"]

            # extract metadata, targets, and inputs
            targets = train_df["y"].to_numpy().ravel()
            train_smiles = train_df["smiles"]
            test_smiles = test_df["smiles"]

            # typical scikit-mol training
            model = TransformedTargetRegressor(regressor=RandomForestRegressor(random_state=random_seed), transformer=StandardScaler())
            pipe = Pipeline(
                [
                    ('smiles2mol', SmilesToMolTransformer()),
                    ('mol2fp', MorganFingerprintTransformer()),
                    ('model', model),
                ]
            )
            pipe.fit(train_smiles, targets)
            predictions = pipe.predict(test_smiles).flatten()
            results = pd.DataFrame.from_records([
                dict(metric="overall test rmse", value=root_mean_squared_error(predictions, test_df["y"])),
                dict(metric="noncliff test rmse", value=root_mean_squared_error(predictions[test_df["cliff_mol"] == 0], test_df[test_df["cliff_mol"] == 0]["y"])),
                dict(metric="cliff test rmse", value=root_mean_squared_error(predictions[test_df["cliff_mol"] == 1], test_df[test_df["cliff_mol"] == 1]["y"])),
            ], index="metric")
            output_file.write(f"""
### `{benchmark_name}`

{results.to_markdown()}

""")
            performance_dict[benchmark_name] = results.at["noncliff test rmse", "value"] - results.at["cliff test rmse", "value"]
        
        output_file.write(f"""
### Summary

```
results_dict = {json.dumps(performance_dict, indent=4)}
```
""")
