import csv
import argparse
import copy
from pathlib import Path
from urllib.request import urlretrieve

import numpy as np
import pandas as pd
import torch
from loguru import logger
from sklearn.model_selection import PredefinedSplit, train_test_split

# Chemprop specific imports
from chemprop.data import (
    BatchMolGraph,
    MoleculeDatapoint,
    MoleculeDataset,
    build_dataloader,
)
from chemprop.models import MPNN
from chemprop.nn import (
    BinaryClassificationFFN,
    BondMessagePassing,
    MeanAggregation,
)

# Lightning imports
from lightning import Trainer, seed_everything
from lightning.pytorch.callbacks import Callback, ModelCheckpoint
from lightning.pytorch.loggers import TensorBoardLogger

# Assumes this local file exists in your directory
try:
    from common import parse_endpoint_input
except ImportError:
    logger.error("Could not find 'common.py'. Ensure parse_endpoint_input is available.")

# ---------------------------------------------------------------------
# Logger for CSV
# ---------------------------------------------------------------------
class CSVLossLogger(Callback):
    def __init__(self, csv_path: Path):
        super().__init__()
        self.csv_path = csv_path

    def on_train_epoch_end(self, trainer, pl_module):
        metrics = trainer.callback_metrics

        # Ensure we extract scalar values from tensors safely
        def get_metric(name):
            val = metrics.get(name)
            if torch.is_tensor(val):
                return val.item()
            return val

        row = {
            "epoch": trainer.current_epoch,
            "train_loss": get_metric("train_loss"),
            "val_loss": get_metric("val_loss"),
        }

        write_header = not self.csv_path.exists()
        with open(self.csv_path, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["epoch", "train_loss", "val_loss"])
            if write_header:
                writer.writeheader()
            writer.writerow(row)

# ---------------------------------------------------------------------
# Model & Dataset Helpers
# ---------------------------------------------------------------------
def from_chemeleon(no_weights: bool = False) -> BondMessagePassing:
    ckpt_dir = Path.home() / ".chemprop"
    ckpt_dir.mkdir(exist_ok=True)
    model_path = ckpt_dir / "chemeleon_mp.pt"

    if not model_path.exists():
        logger.info("Downloading CheMeleon foundation model...")
        urlretrieve(
            "https://zenodo.org/records/15460715/files/chemeleon_mp.pt",
            model_path,
        )

    ckpt = torch.load(model_path, weights_only=True, map_location="cpu")
    mp = BondMessagePassing(**ckpt["hyper_parameters"])

    if not no_weights:
        mp.load_state_dict(ckpt["state_dict"])

    return mp

def smiles_to_dataset(df: pd.DataFrame) -> MoleculeDataset:
    df = df.dropna(subset=["smiles", "label"])
    datapoints = [
        MoleculeDatapoint.from_smi(smi, y)
        for smi, y in zip(df["smiles"], df[["label"]].to_numpy(), strict=True)
    ]
    return MoleculeDataset(datapoints)

def fingerprint_dataset(model: MPNN, dataset: MoleculeDataset) -> np.ndarray:
    model.eval()
    device = next(model.parameters()).device
    with torch.inference_mode():
        mol_graphs = [dp.mg for dp in dataset]
        # Process in one batch (if dataset is very large, consider a loop/dataloader)
        fps = model.fingerprint(BatchMolGraph(mol_graphs).to(device))
        return fps.detach().cpu().numpy()

# ---------------------------------------------------------------------
# Training Logic
# ---------------------------------------------------------------------
def train_model(model: MPNN, train_loader, val_loader, split_dir: Path, epochs: int):
    ckpt_cb = ModelCheckpoint(
        monitor="val_loss",
        mode="min",
        save_top_k=1,
        save_last=True,
        dirpath=split_dir / "checkpoints",
    )

    csv_logger = CSVLossLogger(split_dir / "losses.csv")

    trainer = Trainer(
        max_epochs=epochs,
        callbacks=[ckpt_cb, csv_logger],
        logger=TensorBoardLogger(str(split_dir), name="tensorboard_logs"),
        log_every_n_steps=1,
        deterministic=True,
        accelerator="auto", # Automatically use GPU if available
    )

    trainer.fit(model, train_loader, val_dataloaders=val_loader)
    return ckpt_cb.best_model_path, ckpt_cb.last_model_path

# ---------------------------------------------------------------------
# Main Execution
# ---------------------------------------------------------------------
def main(n_workers: int, endpoint: str, model_name: str, seed: int):
    seed_everything(seed, workers=True)

    IS_FROZEN = model_name == "chemeleon_frozen"
    base_path = Path(__file__).resolve().parent
    data_path = base_path / "data"
    epochs = 50

    endpoints = parse_endpoint_input(endpoint)
    split_strategies = ["Random", "Agglomerative clustering"]

    # Pre-load the base Message Passing block once to save time
    logger.info(f"Initializing base model: {model_name}")
    if model_name in ["chemeleon_frozen", "chemeleon_finetuned"]:
        master_mp = from_chemeleon()
    elif model_name == "chemprop_large":
        master_mp = from_chemeleon(no_weights=True)
    else:  # standard chemprop
        master_mp = BondMessagePassing()

    for ep in endpoints:
        df_path = data_path / "intermediate_data" / "presplit_data" / f"presplit_data_{ep}.tsv"
        if not df_path.exists():
            logger.warning(f"Data file not found: {df_path}")
            continue

        endpoint_df = pd.read_csv(df_path, sep="\t")
        all_predictions = []

        for split_strategy in split_strategies:
            ps = PredefinedSplit(endpoint_df[split_strategy])
            
            for trial, (train_idx, test_idx) in enumerate(ps.split()):
                logger.info(f"Processing {ep} | {split_strategy} | Trial {trial}")
                
                split_dir = (
                    data_path / "intermediate_data" / "model_data" / 
                    model_name / ep / split_strategy / f"fold_{trial}"
                )
                split_dir.mkdir(parents=True, exist_ok=True)

                train_df = endpoint_df.iloc[train_idx]
                test_df = endpoint_df.iloc[test_idx].copy()
                test_dataset = smiles_to_dataset(test_df)

                # Clone the master MP block for this specific trial
                mp_block = copy.deepcopy(master_mp)
                model = MPNN(
                    mp_block,
                    MeanAggregation(),
                    BinaryClassificationFFN(input_dim=mp_block.output_dim, hidden_dim=300),
                )

                if IS_FROZEN:
                    for p in model.parameters():
                        p.requires_grad = False
                    
                    train_dataset = smiles_to_dataset(train_df)
                    np.save(split_dir / "train_fps.npy", fingerprint_dataset(model, train_dataset))
                    np.save(split_dir / "test_fps.npy", fingerprint_dataset(model, test_dataset))
                    continue

                # --- Trainable Path ---
                train_df, val_df = train_test_split(
                    train_df, test_size=0.1, random_state=seed, shuffle=True
                )

                train_loader = build_dataloader(smiles_to_dataset(train_df), num_workers=n_workers, shuffle=True)
                val_loader = build_dataloader(smiles_to_dataset(val_df), num_workers=n_workers, shuffle=False)
                test_loader = build_dataloader(test_dataset, num_workers=n_workers, shuffle=False)

                best_ckpt, last_ckpt = train_model(model, train_loader, val_loader, split_dir, epochs)

                # Load for evaluation
                model_best = MPNN.load_from_checkpoint(best_ckpt)
                model_last = MPNN.load_from_checkpoint(last_ckpt)

                # Predict
                predict_trainer = Trainer(logger=False, accelerator="auto")
                preds_list = predict_trainer.predict(model_best, test_loader)
                preds = torch.vstack(preds_list).cpu().numpy().flatten()

                # Save fingerprints
                full_train_ds = MoleculeDataset(smiles_to_dataset(train_df).data + smiles_to_dataset(val_df).data)
                np.save(split_dir / "train_fps_best.npy", fingerprint_dataset(model_best, full_train_ds))
                np.save(split_dir / "test_fps_best.npy", fingerprint_dataset(model_best, test_dataset))

                # Store Results
                test_df["proba"] = preds
                test_df["prediction"] = (preds > 0.5).astype(int)
                test_df["endpoint"] = ep
                test_df["trial"] = trial
                test_df["Split strategy"] = split_strategy
                test_df["model"] = model_name
                all_predictions.append(test_df)

                # Cleanup to prevent VRAM accumulation
                del model, model_best, model_last, mp_block
                torch.cuda.empty_cache()

        if not IS_FROZEN and all_predictions:
            output_file = data_path / "intermediate_data" / "model_data" / model_name / ep / "test_predictions.tsv"
            pd.concat(all_predictions).to_csv(output_file, sep="\t", index=False)

# ---------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_workers", type=int, default=1)
    parser.add_argument("--endpoint", required=True)
    parser.add_argument(
        "--model-name",
        required=True,
        choices=["chemprop", "chemprop_large", "chemeleon_finetuned", "chemeleon_frozen"],
    )
    parser.add_argument("--seed", type=int, default=23)
    args = parser.parse_args()

    main(args.n_workers, args.endpoint, args.model_name, args.seed)