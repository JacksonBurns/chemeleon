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
    MoleculeDatapoint,
    MoleculeDataset,
    build_dataloader,
    BatchMolGraph,
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

try:
    from common import parse_endpoint_input
except ImportError:
    logger.error("Could not find 'common.py'.")

# ---------------------------------------------------------------------
# 1. Logging Callback
# ---------------------------------------------------------------------
class CSVLossLogger(Callback):
    def __init__(self, csv_path: Path):
        super().__init__()
        self.csv_path = csv_path

    def on_train_epoch_end(self, trainer, pl_module):
        metrics = trainer.callback_metrics
        row = {
            "epoch": trainer.current_epoch,
            "train_loss": metrics.get("train_loss").item() if torch.is_tensor(metrics.get("train_loss")) else metrics.get("train_loss"),
            "val_loss": metrics.get("val_loss").item() if torch.is_tensor(metrics.get("val_loss")) else metrics.get("val_loss"),
        }
        write_header = not self.csv_path.exists()
        with open(self.csv_path, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["epoch", "train_loss", "val_loss"])
            if write_header: writer.writeheader()
            writer.writerow(row)

# ---------------------------------------------------------------------
# 2. Helper Functions
# ---------------------------------------------------------------------
def from_chemeleon(no_weights: bool = False) -> BondMessagePassing:
    ckpt_dir = Path.home() / ".chemprop"
    ckpt_dir.mkdir(exist_ok=True)
    model_path = ckpt_dir / "chemeleon_mp.pt"
    if not model_path.exists():
        logger.info("Downloading CheMeleon weights...")
        urlretrieve("https://zenodo.org/records/15460715/files/chemeleon_mp.pt", model_path)
    ckpt = torch.load(model_path, weights_only=True, map_location="cpu")
    mp = BondMessagePassing(**ckpt["hyper_parameters"])
    if not no_weights: mp.load_state_dict(ckpt["state_dict"])
    return mp

def smiles_table_to_chemprop_molecule_dataset(df_data: pd.DataFrame, smiles_col: str, label_cols: list[str]) -> MoleculeDataset:
    df_data_ref = df_data.dropna(subset=[smiles_col, *label_cols], how="any")
    smiles = df_data_ref.loc[:, smiles_col].to_numpy()
    ys = df_data_ref.loc[:, label_cols].to_numpy()
    datapoints = [MoleculeDatapoint.from_smi(smi, y) for smi, y in zip(smiles, ys, strict=True)]
    return MoleculeDataset(datapoints)

# ---------------------------------------------------------------------
# 3. Main Logic
# ---------------------------------------------------------------------
def main(n_workers: int, endpoint: str, model_name: str, seed: int):
    seed_everything(seed, workers=True)
    base_path = Path(__file__).resolve().parent
    data_path = base_path / "data"
    epochs = 50

    endpoints = parse_endpoint_input(endpoint)
    split_strategies = ["Random", "Agglomerative clustering"]

    for ep in endpoints:
        df_path = data_path / "intermediate_data" / "presplit_data" / f"presplit_data_{ep}.tsv"
        if not df_path.exists(): continue
        
        endpoint_df = pd.read_csv(df_path, sep="\t")
        all_predictions = []

        for split_strategy in split_strategies:
            ps = PredefinedSplit(endpoint_df[split_strategy])
            for trial, (train_idx, test_idx) in enumerate(ps.split()):
                logger.info(f"EP: {ep} | {split_strategy} | Fold: {trial}")
                split_dir = data_path / "intermediate_data" / "model_data" / model_name / ep / split_strategy / f"fold_{trial}"
                split_dir.mkdir(parents=True, exist_ok=True)

                train_df = endpoint_df.iloc[train_idx]
                test_df = endpoint_df.iloc[test_idx].copy()

                if model_name != "chemeleon_frozen":
                    train_df_split, val_df = train_test_split(train_df, test_size=0.1, random_state=seed, shuffle=True)
                else:
                    train_df_split, val_df = train_df, None

                train_ds = smiles_table_to_chemprop_molecule_dataset(train_df_split, "smiles", ["label"])
                test_ds = smiles_table_to_chemprop_molecule_dataset(test_df, "smiles", ["label"])
                val_ds = smiles_table_to_chemprop_molecule_dataset(val_df, "smiles", ["label"]) if val_df is not None else None

                if "chemeleon" in model_name or model_name == "chemprop_large":
                    mp = from_chemeleon(no_weights=(model_name == "chemprop_large"))
                else:
                    mp = BondMessagePassing()
                
                model = MPNN(mp, MeanAggregation(), BinaryClassificationFFN(input_dim=mp.output_dim, hidden_dim=300))

                if model_name == "chemeleon_frozen":
                    for p in model.parameters(): p.requires_grad = False
                    dummy_trainer = Trainer(accelerator="auto", logger=False)
                    dummy_trainer.predict(model, build_dataloader(train_ds, num_workers=n_workers))
                    dummy_trainer.predict(model, build_dataloader(test_ds, num_workers=n_workers))
                    
                    with torch.inference_mode():
                        np.save(split_dir / "train_fps.npy", model.fingerprint(BatchMolGraph([dp.mg for dp in train_ds])).cpu().numpy())
                        np.save(split_dir / "test_fps.npy", model.fingerprint(BatchMolGraph([dp.mg for dp in test_ds])).cpu().numpy())
                    continue

                ckpt_cb = ModelCheckpoint(monitor="val_loss", mode="min", save_top_k=1, save_last=True, dirpath=split_dir / "checkpoints")
                loss_logger = CSVLossLogger(split_dir / "losses.csv")
                trainer = Trainer(max_epochs=epochs, callbacks=[ckpt_cb, loss_logger], accelerator="auto", logger=False)
                
                trainer.fit(model, 
                            build_dataloader(train_ds, num_workers=n_workers, shuffle=True), 
                            val_dataloaders=build_dataloader(val_ds, num_workers=n_workers, shuffle=False) if val_ds else None)

                # Loop through Best and Last exactly as requested
                for label, ckpt_path in [("best", ckpt_cb.best_model_path), ("last", ckpt_cb.last_model_path)]:
                    if not ckpt_path: continue
                    logger.info(f"Generating {label} fingerprints using checkpoint: {ckpt_path}")
                    m_eval = MPNN.load_from_checkpoint(ckpt_path)
                    eval_trainer = Trainer(accelerator="auto", logger=False)
                    
                    # 1. Predict to (a) save probas and (b) trigger featurization of test_ds
                    preds = torch.vstack(eval_trainer.predict(m_eval, build_dataloader(test_ds, num_workers=n_workers))).cpu().numpy().flatten()
                    
                    if label == "best":
                        test_df["proba"] = preds
                        test_df["prediction"] = (preds > 0.5).astype(int)
                        for k, v in {"endpoint": ep, "trial": trial, "Split strategy": split_strategy, "model": model_name}.items():
                            test_df[k] = v
                        all_predictions.append(test_df.copy())

                    # 2. Trigger featurization of train and val datasets
                    eval_trainer.predict(m_eval, build_dataloader(train_ds, num_workers=n_workers))
                    if val_ds: eval_trainer.predict(m_eval, build_dataloader(val_ds, num_workers=n_workers))

                    # 3. Save fingerprints using the old script's list comprehension style
                    with torch.inference_mode():
                        fps_train_part = m_eval.fingerprint(BatchMolGraph([dp.mg for dp in train_ds])).cpu().numpy()
                        fps_val_part = m_eval.fingerprint(BatchMolGraph([dp.mg for dp in val_ds])).cpu().numpy() if val_ds else np.array([])
                        fps_test = m_eval.fingerprint(BatchMolGraph([dp.mg for dp in test_ds])).cpu().numpy()
                    
                    fps_train_full = np.concatenate([fps_train_part, fps_val_part], axis=0) if fps_val_part.size else fps_train_part
                    
                    np.save(split_dir / f"train_fps_{label}.npy", fps_train_full)
                    np.save(split_dir / f"test_fps_{label}.npy", fps_test)
                    del m_eval

                torch.cuda.empty_cache()

        if all_predictions:
            pd.concat(all_predictions).to_csv(data_path / "intermediate_data" / "model_data" / model_name / ep / "test_predictions.tsv", sep="\t", index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_workers", type=int, default=1)
    parser.add_argument("--endpoint", required=True)
    parser.add_argument("--model-name", required=True)
    parser.add_argument("--seed", type=int, default=23)
    args = parser.parse_args()
    main(args.n_workers, args.endpoint, args.model_name, args.seed)