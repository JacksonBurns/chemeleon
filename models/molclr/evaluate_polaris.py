import datetime
import json
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import polaris as po
from polaris.utils.types import TargetType
from sklearn.metrics import root_mean_squared_error

BENCHMARK_SET = os.getenv("BENCHMARK_SET", "polaris")
print(f"Running benchmark set {BENCHMARK_SET}")


def load_benchmark_predictions(
    prediction_dir: str, benchmark_name: str, seed: int
) -> np.ndarray:
    """Load the predictions for a benchmark from the output directory for a specific seed."""
    prediction_path = os.path.join(
        prediction_dir, f"{benchmark_name}_test_predictions.csv"
    )
    if not os.path.exists(prediction_path):
        raise FileNotFoundError(f"Prediction file not found: {prediction_path}")

    df = pd.read_csv(prediction_path)
    seed_column = f"seed_{seed}"
    if seed_column not in df.columns:
        raise ValueError(f"Seed column {seed_column} not found in predictions file")

    return df[seed_column].values


if __name__ == "__main__":
    try:
        output_dir = Path(sys.argv[1])
    except:
        print("usage: python new_evaluate.py OUTPUT_DIR")
        exit(1)
    if not output_dir.exists():
        output_dir.mkdir()
    output_file = open(output_dir / "MolCLR.md", "w")
    output_file.write(
        f"""# `molclr` Results
timestamp: {datetime.datetime.now()}

"""
    )

    polaris_benchmarks = [
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
    ]

    for random_seed in (42, 117, 709, 1701, 9001):
        output_file.write(f"## Random Seed {random_seed}\n")
        performance_dict = {}  # Create a new performance dict for each seed

        for benchmark_name in polaris_benchmarks:
            # Convert benchmark name to the format used in our directory structure
            if benchmark_name.startswith("polaris/"):
                dir_name = benchmark_name.replace("polaris/", "polaris_")
            elif benchmark_name.startswith("tdcommons/"):
                dir_name = benchmark_name.replace("tdcommons/", "tdcommons_")
            else:
                dir_name = benchmark_name

            # Load the benchmark from Polaris
            try:
                benchmark = po.load_benchmark(benchmark_name)
                target_cols = list(benchmark.target_cols)
                task_type = benchmark.target_types[target_cols[0]]

                # Determine the category directory based on task type
                category = (
                    "classification"
                    if task_type == TargetType.CLASSIFICATION
                    else "regression"
                )
                benchmark_dir = output_dir / category / dir_name

                if not benchmark_dir.exists():
                    print(
                        f"Warning: Benchmark directory {benchmark_dir} not found, skipping"
                    )
                    continue

                # Load the predictions for this seed
                try:
                    predictions = load_benchmark_predictions(
                        benchmark_dir, dir_name, random_seed
                    )

                    # Evaluate predictions
                    if task_type == TargetType.CLASSIFICATION:
                        results = benchmark.evaluate(
                            predictions > 0.5, predictions
                        ).results
                        performance = results.query(
                            f"Metric == '{benchmark.main_metric.label}'"
                        )["Score"].values[0]
                    else:  # Regression
                        results = benchmark.evaluate(predictions).results
                        performance = results.query(
                            f"Metric == '{benchmark.main_metric.label}'"
                        )["Score"].values[0]

                    # Write results to markdown file - format exactly like the minimol script
                    output_file.write(
                        f"""
### `{benchmark_name}`

{results.to_markdown()}

"""
                    )

                    # Store performance for summary
                    performance_dict[benchmark_name] = performance

                except Exception as e:
                    print(
                        f"Error evaluating benchmark {benchmark_name} with seed {random_seed}: {e}"
                    )
                    output_file.write(
                        f"""
### `{benchmark_name}`

Error: {str(e)}

"""
                    )
            except Exception as e:
                print(f"Error loading benchmark {benchmark_name}: {e}")
                continue

        # Write summary for this seed
        output_file.write(
            f"""
### Summary

```
results_dict = {json.dumps(performance_dict, indent=4)}
```
"""
        )

    print(f"Evaluation complete. Results written to {output_dir / 'MolCLR.md'}")
