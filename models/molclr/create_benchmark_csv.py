import argparse
import json
import logging
import os
import re
from typing import Dict, List

import pandas as pd
import polaris as po
from polaris.utils.types import TargetType

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Define default benchmark list
DEFAULT_POLARIS_BENCHMARKS = [
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


def sanitize_filename(name: str) -> str:
    """
    Sanitize filename to avoid issues with special characters.
    """
    # Replace slashes with underscores
    name = name.replace("/", "_")
    # Remove any other unsafe characters
    name = re.sub(r"[^\w\-\.]", "_", name)
    return name


def extract_benchmarks_to_csv(
    benchmark_names: List[str] = DEFAULT_POLARIS_BENCHMARKS,
    output_dir: str = "polaris_benchmarks",
) -> Dict[str, Dict[str, str]]:
    """
    Extract Polaris benchmarks and save train/test sets as CSV files.

    Args:
        benchmark_names: List of benchmark names to process
        output_dir: Directory where CSV files will be saved

    Returns:
        Dictionary mapping benchmark names to their train/test CSV paths.
    """
    os.makedirs(output_dir, exist_ok=True)
    benchmark_files = {}

    for name in benchmark_names:
        logger.info(f"Processing benchmark: {name}")
        try:
            benchmark = po.load_benchmark(name)
            smiles_col = list(benchmark.input_cols)[0]
            target_cols = list(benchmark.target_cols)

            # Validate that the SMILES column exists in the data
            train, test = benchmark.get_train_test_split()
            train_df, test_df = train.as_dataframe(), test.as_dataframe()

            if smiles_col not in train_df.columns:
                logger.error(
                    f"SMILES column '{smiles_col}' not found in benchmark {name}"
                )
                continue

            # Determine the task type
            primary_task_type = benchmark.target_types[target_cols[0]]

            # Create a sanitized filename
            safe_name = sanitize_filename(name)

            if primary_task_type == TargetType.REGRESSION:
                task_dir = os.path.join(output_dir, "regression")
                os.makedirs(task_dir, exist_ok=True)
                train_file = os.path.join(task_dir, f"{safe_name}_train.csv")
                test_file = os.path.join(task_dir, f"{safe_name}_test.csv")
                train_df.to_csv(train_file, index=False)
                test_df.to_csv(test_file, index=False)
                benchmark_files[name] = {"train": train_file, "test": test_file}

                # Create metadata file
                metadata = {
                    "name": name,
                    "task_type": "regression",
                    "smiles_column": smiles_col,
                    "target_columns": target_cols,
                    "num_train_samples": len(train_df),
                    "num_test_samples": len(test_df),
                    "single_task": True,
                }
                meta_file = os.path.join(task_dir, f"{safe_name}_metadata.json")
                with open(meta_file, "w") as f:
                    json.dump(metadata, f, indent=2)
                benchmark_files[name]["metadata"] = meta_file

            elif primary_task_type == TargetType.CLASSIFICATION:
                task_dir = os.path.join(output_dir, "classification")
                os.makedirs(task_dir, exist_ok=True)
                train_file = os.path.join(task_dir, f"{safe_name}_train.csv")
                test_file = os.path.join(task_dir, f"{safe_name}_test.csv")
                train_df.to_csv(train_file, index=False)
                test_df.to_csv(test_file, index=False)
                benchmark_files[name] = {"train": train_file, "test": test_file}

                # Create metadata file
                # # For classification tasks, determine number of classes
                # num_classes = {}
                # for col in target_cols:
                #     if benchmark.target_types[col] == TargetType.CLASSIFICATION:
                #         unique_values = set(train_df[col].unique()) | set(test_df[col].unique())
                #         num_classes[col] = len(unique_values)

                metadata = {
                    "name": name,
                    "task_type": "classification",
                    "smiles_column": smiles_col,
                    "target_columns": target_cols,
                    "num_train_samples": len(train_df),
                    "num_test_samples": len(test_df),
                    "single_task": True,
                    # "num_classes": num_classes
                }
                meta_file = os.path.join(task_dir, f"{safe_name}_metadata.json")
                with open(meta_file, "w") as f:
                    json.dump(metadata, f, indent=2)
                benchmark_files[name]["metadata"] = meta_file

            logger.info(
                f"Successfully processed benchmark: {name}, saved to {train_file} and {test_file}"
            )

        except Exception as e:
            logger.error(f"Failed to process benchmark {name}: {str(e)}")
            continue

    return benchmark_files


def main():
    """Main function to execute the script."""
    parser = argparse.ArgumentParser(
        description="Extract Polaris benchmarks to CSV files"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="polaris_benchmarks",
        help="Directory where CSV files will be saved",
    )
    parser.add_argument(
        "--benchmarks",
        type=str,
        nargs="+",
        default=DEFAULT_POLARIS_BENCHMARKS,
        help="List of benchmark names to process",
    )

    args = parser.parse_args()

    benchmark_files = extract_benchmarks_to_csv(
        benchmark_names=args.benchmarks, output_dir=args.output_dir
    )

    # Print summary
    print(f"\nProcessed {len(benchmark_files)} benchmarks successfully.")
    print(f"Files saved to {os.path.abspath(args.output_dir)}")


if __name__ == "__main__":
    main()
