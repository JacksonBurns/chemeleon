# polaris_leaderboard.py
#
# runs chemeleon on a set of benchmarks from the polaris benchmarking suite and pushes
# the results to the leaderboard
import os
import subprocess
from pathlib import Path

import pandas as pd
import polaris as po
from polaris.utils.types import TargetType

_var = "UPLOAD_RESULTS"
_DO_UPLOAD = bool(os.getenv(_var, False))
print(f"Environment variable '{_var}' was '{_DO_UPLOAD}', results will {"" if _DO_UPLOAD else "not "}be uploaded!")

HPOPT_NUM_TRIALS = 20

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

if __name__ == "__main__":
    for benchmark_name in POLARIS_BENCHMARKS:
        benchmark = po.load_benchmark(benchmark_name)
        outdir = Path("/data2/jwburns/chemeleon_polaris/outputs_" + benchmark_name.replace("/", "_"))
        outdir.mkdir(exist_ok=True)

        smiles_column = list(benchmark.input_cols)[0]
        assert len(benchmark.target_cols) == 1, "Only single task supported with this script!"
        target_column = list(benchmark.target_cols)[0]
        task_type = "classification" if benchmark.target_types[target_column] == TargetType.CLASSIFICATION else "regression"

        train, test = benchmark.get_train_test_split()
        train.as_dataframe().to_csv(outdir / "train.csv", index=False)
        test.as_dataframe().to_csv(outdir / "test.csv", index=False)
        train_args = [
                "chemprop",
                "hpopt",
                "--from-foundation",
                "CheMeleon",
                "--data-path",
                outdir / "train.csv",
                "--hpopt-save-dir",
                outdir,
                "--pytorch-seed",
                "42",
                "--data-seed",
                "42",
                "--hyperopt-random-state-seed",
                "42",
                "--smiles-columns",
                smiles_column,
                "--target-columns",
                target_column,
                "--task-type",
                task_type,
                "--split-type",
                "random",
                "--split-sizes",
                "0.90",
                "0.10",
                "0.00",
                "--raytune-temp-dir",
                "/data2/jwburns/chemeleon_polaris",
                "--raytune-max-concurrent-trials",
                "1",
                "--raytune-num-gpus",
                "1",
                "--raytune-num-samples",
                str(HPOPT_NUM_TRIALS),
                "--patience",
                "5",
                "--num-workers",
                "4",
        ]
        if task_type == "binary":
            train_args.append("--class-balance")
        subprocess.run(
            train_args,
            check=True,
        )
        subprocess.run(
            [
                "chemprop",
                "predict",
                "--num-workers",
                "4",
                "--model-path",
                outdir / "best_checkpoint.ckpt",
                "--preds-path",
                outdir / "test_predictions.csv",
                "--test-path",
                outdir / "test.csv",
                "--smiles-column",
                smiles_column
            ],
            check=True,
        )

        predictions = pd.read_csv(outdir / "test_predictions.csv")["pred_0"].to_numpy()

        # Evaluate your predictions
        if task_type == "classification":
            results = benchmark.evaluate(predictions > 0.5, predictions)
        else:
            results = benchmark.evaluate(predictions)
        
        results.name = "CheMeleon"
        results.description = "CheMeleon Descriptor-based Foundation Model (Chemrop 2.2.1)"
        results.github_url = "https://github.com/JacksonBurns/chemeleon"
        results.paper_url = "https://www.alphaxiv.org/abs/2506.15792"
        
        print(results.results)

        if _DO_UPLOAD:
            results.upload_to_hub(owner="jacksonburns")
