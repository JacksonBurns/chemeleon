from pathlib import Path
import sys
import datetime
import json
import os
import shutil

import polaris as po
from polaris.utils.types import TargetType

import torch
from datasets import Dataset
from astartes import train_test_split
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    TrainingArguments,
    Trainer,
)
import numpy as np
import pandas as pd
from sklearn.metrics import root_mean_squared_error

BASE_MODEL = "ibm-research/MoLFormer-XL-both-10pct"
BENCHMARK_SET = os.getenv('BENCHMARK_SET', "polaris")
print(f"Running benchmark set {BENCHMARK_SET}")


def tokenize_function(df, smiles_col, tokenizer):
    return tokenizer(df[smiles_col], padding="max_length", truncation=True)


def preprocess_labels(example, target_col):
    example["labels"] = float(example[target_col])
    return example


class RegressionTrainer(Trainer):
    def compute_loss(
        self, model, inputs, return_outputs=False, num_items_in_batch=None
    ):
        labels = inputs.pop("labels")  # Extract labels
        outputs = model(**inputs)
        logits = outputs.logits.squeeze(-1)  # Ensure shape compatibility
        loss_fct = torch.nn.MSELoss()  # Mean Squared Error for regression
        loss = loss_fct(logits, labels)
        return (loss, outputs) if return_outputs else loss


def predict(model, smiles):
    model.eval()
    inputs = tokenizer(
        smiles, return_tensors="pt", padding="max_length", truncation=True
    ).to(model.device)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.logits.item()


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
        f"""# {BASE_MODEL} Results
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
        for benchmark_name in (polaris_benchmarks if BENCHMARK_SET == "polaris" else moleculeace_benchmarks):
            if BENCHMARK_SET == "polaris":
                # load the benchmarking data
                benchmark = po.load_benchmark(benchmark_name)
                smiles_col = list(benchmark.input_cols)[0]
                target_cols = list(benchmark.target_cols)
                train, test = benchmark.get_train_test_split()
                train_df, test_df = train.as_dataframe(), test.as_dataframe()
                task_type = benchmark.target_types[target_cols[0]]
            else:
                smiles_col = "smiles"
                target_cols = "y"
                df = pd.read_csv(f"https://raw.githubusercontent.com/molML/MoleculeACE/7e6de0bd2968c56589c580f2a397f01c531ede26/MoleculeACE/Data/benchmark_data/{benchmark_name}.csv")
                train_df, test_df = df[df["split"] == "train"], df[df["split"] == "test"]
                task_type = TargetType.REGRESSION

            # extract metadata
            _subdir = "".join(c if c.isalnum() else "_" for c in benchmark_name)

            # molformer fine tuning
            train_idxs, val_idxs = train_test_split(
                np.arange(train_df.shape[0]),
                random_state=random_seed,
                train_size=0.80,
                test_size=0.20,
            )
            train_dataset = Dataset.from_pandas(train_df.iloc[train_idxs])
            val_dataset = Dataset.from_pandas(train_df.iloc[val_idxs])
            tokenizer = AutoTokenizer.from_pretrained(
                BASE_MODEL, trust_remote_code=True
            )
            model = AutoModelForSequenceClassification.from_pretrained(
                BASE_MODEL, num_labels=1, trust_remote_code=True
            )
            train_dataset = train_dataset.map(
                lambda x: tokenize_function(x, smiles_col, tokenizer), batched=True
            ).map(lambda e: preprocess_labels(e, target_cols[0]))
            val_dataset = val_dataset.map(
                lambda x: tokenize_function(x, smiles_col, tokenizer), batched=True
            ).map(lambda e: preprocess_labels(e, target_cols[0]))

            training_args = TrainingArguments(
                output_dir=seed_dir / _subdir,
                eval_strategy="epoch",
                save_strategy="epoch",
                num_train_epochs=5,
                per_device_train_batch_size=8,
                per_device_eval_batch_size=8,
                weight_decay=0.01,
                logging_dir=seed_dir / _subdir,
                logging_steps=10,
                save_total_limit=2,
                report_to=["tensorboard"],
            )

            if task_type == TargetType.REGRESSION:
                trainer = RegressionTrainer(
                    model=model,
                    args=training_args,
                    train_dataset=train_dataset,
                    eval_dataset=val_dataset,
                    processing_class=tokenizer,
                )
            else:
                trainer = Trainer(
                    model=model,
                    args=training_args,
                    train_dataset=train_dataset,
                    eval_dataset=val_dataset,
                    processing_class=tokenizer,
                )

            trainer.train()
            trainer.save_model(seed_dir / _subdir)
            tokenizer.save_pretrained(seed_dir / _subdir)
            tokenizer = AutoTokenizer.from_pretrained(
                seed_dir / _subdir, trust_remote_code=True
            )
            model = AutoModelForSequenceClassification.from_pretrained(
                seed_dir / _subdir, num_labels=1, trust_remote_code=True
            )

            predictions = test_df.apply(
                lambda row: predict(model, row[smiles_col]), axis=1
            )

            # prepare the predictions in the format polaris expects
            if task_type == TargetType.CLASSIFICATION:
                results = benchmark.evaluate(predictions > 0.5, predictions).results
                performance = results.query(f"Metric == '{benchmark.main_metric.label}'")['Score'].values[0]
            elif task_type == TargetType.REGRESSION:
                if BENCHMARK_SET == "polaris":
                    results = benchmark.evaluate(predictions).results
                    performance = results.query(f"Metric == '{benchmark.main_metric.label}'")['Score'].values[0]
                else:
                    results = pd.DataFrame.from_records([
                        dict(metric="overall test rmse", value=root_mean_squared_error(predictions, test_df["y"])),
                        dict(metric="noncliff test rmse", value=root_mean_squared_error(predictions[test_df["cliff_mol"] == 0], test_df[test_df["cliff_mol"] == 0]["y"])),
                        dict(metric="cliff test rmse", value=root_mean_squared_error(predictions[test_df["cliff_mol"] == 1], test_df[test_df["cliff_mol"] == 1]["y"])),
                    ], index="metric")
                    performance = {"cliff": results.at["cliff test rmse", "value"], "noncliff": results.at["noncliff test rmse", "value"]}
            output_file.write(f"""
### `{benchmark_name}`

{results.to_markdown()}

""")
            
            performance_dict[benchmark_name] = performance

            # free up the disk space
            for ckpt_dir in (seed_dir / _subdir).glob("checkpoint-*"):
                shutil.rmtree(ckpt_dir)

        output_file.write(
            f"""
### Summary

```
results_dict = {json.dumps(performance_dict, indent=4)}
```
"""
        )
