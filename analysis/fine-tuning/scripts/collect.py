import argparse
from pathlib import Path

import pandas as pd


RNG_SEEDS = (42, 117, 709, 1701, 9001)
POLARIS_BENCHMARKS = (
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


def parse_args():
    parser = argparse.ArgumentParser(description="Collect results.")
    parser.add_argument(
        "directory", type=Path, help="Directory to collect results from."
    )
    parser.add_argument("output_file", type=Path, help="Output file.")
    args = parser.parse_args()
    return args.directory, args.output_file


def read_scaled_loss(log_path: Path):
    log_df = pd.read_csv(log_path / "metrics.csv")
    train_loss = log_df["train_loss_epoch"].dropna().values
    val_loss = log_df["val_loss"].dropna().values
    return train_loss, val_loss


if __name__ == "__main__":
    directory, output_file = parse_args()
    results = {}
    for seed in RNG_SEEDS:
        for benchmark_name in POLARIS_BENCHMARKS:
            name = "".join(c if c.isalnum() else "_" for c in benchmark_name)
            subdir = directory / f"seed_{seed}" / name / "trainer_logs" / "version_0"
            train_loss, val_loss = read_scaled_loss(subdir)
            results[f"{name}_seed{seed}_train"] = train_loss
            results[f"{name}_seed{seed}_val"] = val_loss
df = pd.DataFrame(results)
print(f"Writing results to {output_file}")
df.to_csv(output_file, index=False)
