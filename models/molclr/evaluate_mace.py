#!/usr/bin/env python

import os
import sys
import yaml
import json
import datetime
import warnings
import numpy as np
import pandas as pd
from pathlib import Path

import torch
from torch import nn
import torch.nn.functional as F
from torch.utils.tensorboard import SummaryWriter
from torch.utils.data import Dataset
from torch.utils.data.sampler import SubsetRandomSampler
from torch.optim.lr_scheduler import CosineAnnealingLR
from sklearn.metrics import mean_squared_error, mean_absolute_error

from torch_geometric.data import Data, DataLoader

# MolCLR imports
sys.path.append("/home/akshatz/MolCLR")
from models.gcn_finetune import GCN
from dataset.dataset_test import ATOM_LIST, CHIRALITY_LIST, BOND_LIST, BONDDIR_LIST

import rdkit
from rdkit import Chem
from rdkit.Chem.rdchem import HybridizationType
from rdkit.Chem.rdchem import BondType as BT
from rdkit import RDLogger

RDLogger.DisableLog("rdApp.*")

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

# Constants for MolCLR
ATOM_LIST = list(range(1, 119))
CHIRALITY_LIST = [
    Chem.rdchem.ChiralType.CHI_UNSPECIFIED,
    Chem.rdchem.ChiralType.CHI_TETRAHEDRAL_CW,
    Chem.rdchem.ChiralType.CHI_TETRAHEDRAL_CCW,
    Chem.rdchem.ChiralType.CHI_OTHER,
]
BOND_LIST = [BT.SINGLE, BT.DOUBLE, BT.TRIPLE, BT.AROMATIC]
BONDDIR_LIST = [
    Chem.rdchem.BondDir.NONE,
    Chem.rdchem.BondDir.ENDUPRIGHT,
    Chem.rdchem.BondDir.ENDDOWNRIGHT,
]


# Define task type for regression
class TargetType:
    REGRESSION = "regression"
    CLASSIFICATION = "classification"


class Normalizer(object):
    """Normalize a Tensor and restore it later."""

    def __init__(self, tensor):
        self.mean = torch.mean(tensor)
        self.std = torch.std(tensor)

    def norm(self, tensor):
        return (tensor - self.mean) / self.std

    def denorm(self, normed_tensor):
        return normed_tensor * self.std + self.mean

    def state_dict(self):
        return {"mean": self.mean, "std": self.std}

    def load_state_dict(self, state_dict):
        self.mean = state_dict["mean"]
        self.std = state_dict["std"]


class MolDataset(Dataset):
    def __init__(self, df, smiles_column="smiles", target_column="y"):
        self.df = df
        self.smiles_column = smiles_column
        self.target_column = target_column

        self.smiles_data = df[smiles_column].values
        self.labels = df[target_column].values

    def __getitem__(self, index):
        mol = Chem.MolFromSmiles(self.smiles_data[index])
        if mol is None:
            print(f"Could not convert SMILES to molecule: {self.smiles_data[index]}")
            # Return a default simple molecule to prevent errors
            mol = Chem.MolFromSmiles("C")
        mol = Chem.AddHs(mol)

        # Prepare node features
        type_idx = []
        chirality_idx = []
        for atom in mol.GetAtoms():
            atomic_num = atom.GetAtomicNum()
            if atomic_num not in ATOM_LIST:
                atomic_num = 6  # Default to carbon if atom type not found
            type_idx.append(ATOM_LIST.index(atomic_num))
            chirality_idx.append(CHIRALITY_LIST.index(atom.GetChiralTag()))

        x1 = torch.tensor(type_idx, dtype=torch.long).view(-1, 1)
        x2 = torch.tensor(chirality_idx, dtype=torch.long).view(-1, 1)
        x = torch.cat([x1, x2], dim=-1)

        # Prepare edge features
        row, col, edge_feat = [], [], []
        for bond in mol.GetBonds():
            start, end = bond.GetBeginAtomIdx(), bond.GetEndAtomIdx()
            row += [start, end]
            col += [end, start]
            edge_feat.append(
                [
                    BOND_LIST.index(bond.GetBondType()),
                    BONDDIR_LIST.index(bond.GetBondDir()),
                ]
            )
            edge_feat.append(
                [
                    BOND_LIST.index(bond.GetBondType()),
                    BONDDIR_LIST.index(bond.GetBondDir()),
                ]
            )

        if len(row) == 0:  # No bonds (single atom molecule)
            # Create self-loop
            row = [0]
            col = [0]
            edge_feat = [[0, 0]]

        edge_index = torch.tensor([row, col], dtype=torch.long)
        edge_attr = torch.tensor(np.array(edge_feat), dtype=torch.long)

        # Target value
        y = torch.tensor(self.labels[index], dtype=torch.float).view(1, -1)

        data = Data(x=x, y=y, edge_index=edge_index, edge_attr=edge_attr)
        return data

    def __len__(self):
        return len(self.smiles_data)


def calculate_rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))


class MolCLRFineTuner:
    def __init__(self, config, train_loader, val_loader, test_loader):
        self.config = config
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.test_loader = test_loader
        self.device = self._get_device()
        self.criterion = nn.MSELoss()

        # Create model
        self.model = self._create_model()

        # Prepare training directories
        current_time = datetime.datetime.now().strftime("%b%d_%H-%M-%S")
        dir_name = current_time + "_" + config["task_name"]
        log_dir = os.path.join("finetune_outputs", dir_name)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        self.log_dir = log_dir
        self.writer = SummaryWriter(log_dir=log_dir)

        # Create normalizer for regression targets - collect all training targets first
        all_targets = []
        for data in train_loader:
            all_targets.extend(data.y.view(-1).tolist())
        targets_tensor = torch.tensor(all_targets, dtype=torch.float)
        self.normalizer = Normalizer(targets_tensor)

    def _get_device(self):
        if torch.cuda.is_available() and self.config.get("gpu", "cpu") != "cpu":
            device = self.config["gpu"]
            torch.cuda.set_device(device)
        else:
            device = "cpu"
        print(f"Running on: {device}")
        return device

    def _create_model(self):
        model = GCN("regression", **self.config["model"]).to(self.device)
        model = self._load_pre_trained_weights(model)
        return model

    def _load_pre_trained_weights(self, model):
        try:
            checkpoints_folder = os.path.join(
                "/home/akshatz/MolCLR/ckpt",
                self.config["fine_tune_from"],
                "checkpoints",
            )
            state_dict = torch.load(
                os.path.join(checkpoints_folder, "model.pth"), map_location=self.device
            )
            model.load_my_state_dict(state_dict)
            print("Loaded pre-trained model with success.")
        except FileNotFoundError:
            print("Pre-trained weights not found. Training from scratch.")
        return model

    def _step(self, model, data):
        data = data.to(self.device)
        _, pred = model(data)

        # In PyTorch Geometric, data.y is now a tensor on the device
        target = self.normalizer.norm(data.y)
        loss = self.criterion(pred, target)

        return loss, pred

    def train(self, random_seed):
        print(f"Training model with random seed {random_seed}")

        # Set seed for reproducibility
        torch.manual_seed(random_seed)
        np.random.seed(random_seed)

        # Create new model instance for this seed
        model = self._create_model()

        # Setup optimizer with separate learning rates for the backbone and prediction head
        layer_list = []
        for name, param in model.named_parameters():
            if "pred_head" in name:
                print(name, param.requires_grad)
                layer_list.append(name)

        params = list(
            map(
                lambda x: x[1],
                list(filter(lambda kv: kv[0] in layer_list, model.named_parameters())),
            )
        )
        base_params = list(
            map(
                lambda x: x[1],
                list(
                    filter(lambda kv: kv[0] not in layer_list, model.named_parameters())
                ),
            )
        )

        optimizer = torch.optim.Adam(
            [
                {"params": base_params, "lr": self.config["init_base_lr"]},
                {"params": params, "lr": self.config["init_lr"]},
            ],
            weight_decay=float(self.config["weight_decay"]),
        )

        # Training loop
        n_iter = 0
        valid_n_iter = 0
        best_valid_loss = float("inf")
        best_valid_rmse = float("inf")

        for epoch in range(self.config["epochs"]):
            model.train()

            train_loss = 0
            for bn, data in enumerate(self.train_loader):
                optimizer.zero_grad()

                loss, _ = self._step(model, data)
                loss.backward()
                optimizer.step()

                train_loss += loss.item()

                if n_iter % self.config["log_every_n_steps"] == 0:
                    self.writer.add_scalar(
                        f"train_loss_{random_seed}", loss.item(), global_step=n_iter
                    )

                n_iter += 1

            # Print average train loss for the epoch
            print(
                f"Epoch {epoch}, Train Loss: {train_loss / len(self.train_loader):.6f}"
            )

            # Validate model
            if epoch % self.config["eval_every_n_epochs"] == 0:
                valid_loss, valid_rmse = self._validate(model, self.val_loader)
                self.writer.add_scalar(
                    f"valid_loss_{random_seed}", valid_loss, global_step=valid_n_iter
                )
                self.writer.add_scalar(
                    f"valid_rmse_{random_seed}", valid_rmse, global_step=valid_n_iter
                )

                print(
                    f"Epoch {epoch}, Valid Loss: {valid_loss:.6f}, Valid RMSE: {valid_rmse:.6f}"
                )

                if valid_rmse < best_valid_rmse:
                    best_valid_rmse = valid_rmse
                    model_path = os.path.join(self.log_dir, f"model_{random_seed}.pth")
                    torch.save(model.state_dict(), model_path)
                    print(f"Epoch {epoch}: New best validation RMSE: {valid_rmse:.4f}")

                valid_n_iter += 1

        # Load best model for this seed
        best_model_path = os.path.join(self.log_dir, f"model_{random_seed}.pth")
        model.load_state_dict(torch.load(best_model_path))

        return model

    def _validate(self, model, loader):
        model.eval()
        predictions = []
        labels = []

        valid_loss = 0.0
        num_data = 0

        with torch.no_grad():
            for data in loader:
                data = data.to(self.device)
                loss, pred = self._step(model, data)

                valid_loss += loss.item() * data.y.size(0)
                num_data += data.y.size(0)

                # Denormalize predictions
                pred = self.normalizer.denorm(pred)

                # Extract predictions and labels properly from batched data
                if self.device == "cpu":
                    predictions.extend(pred.detach().numpy().reshape(-1))
                    labels.extend(data.y.detach().numpy().reshape(-1))
                else:
                    predictions.extend(pred.cpu().detach().numpy().reshape(-1))
                    labels.extend(data.y.cpu().detach().numpy().reshape(-1))

        valid_loss /= num_data

        # Calculate RMSE
        predictions = np.array(predictions)
        labels = np.array(labels)
        rmse = calculate_rmse(labels, predictions)

        model.train()
        return valid_loss, rmse

    def evaluate(self, model, loader):
        model.eval()
        predictions = []
        labels = []

        with torch.no_grad():
            for data in loader:
                data = data.to(self.device)
                _, pred = self._step(model, data)

                # Denormalize predictions
                pred = self.normalizer.denorm(pred)

                # Extract predictions and labels properly from batched data
                if self.device == "cpu":
                    predictions.extend(pred.detach().numpy().reshape(-1))
                    labels.extend(data.y.detach().numpy().reshape(-1))
                else:
                    predictions.extend(pred.cpu().detach().numpy().reshape(-1))
                    labels.extend(data.y.cpu().detach().numpy().reshape(-1))

        # Calculate metrics
        predictions = np.array(predictions)
        labels = np.array(labels)
        rmse = calculate_rmse(labels, predictions)
        mae = mean_absolute_error(labels, predictions)

        return predictions, labels, rmse, mae


if __name__ == "__main__":
    try:
        output_dir = Path(sys.argv[1])
    except:
        print("usage: python evaluate_mace_fixed.py OUTPUT_DIR")
        exit(1)

    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    # Create output markdown file
    output_file = open(output_dir / "train_results.md", "w")
    output_file.write(
        f"""# `molclr` GNN Results
timestamp: {datetime.datetime.now()}

"""
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

    # Process each random seed
    for random_seed in (42, 117, 709, 1701, 9001):
        torch.manual_seed(random_seed)
        np.random.seed(random_seed)

        output_file.write(f"## Random Seed {random_seed}\n\n")
        performance_dict = {}
        seed_dir = output_dir / f"seed_{random_seed}"
        if not seed_dir.exists():
            seed_dir.mkdir(parents=True)

        # Process each benchmark dataset
        for benchmark_name in moleculeace_benchmarks:
            print(f"Processing {benchmark_name} with seed {random_seed}")
            output_file.write(f"### `{benchmark_name}`\n\n")

            # Load data
            smiles_col = "smiles"
            target_col = "y"
            df = pd.read_csv(
                f"https://raw.githubusercontent.com/molML/MoleculeACE/7e6de0bd2968c56589c580f2a397f01c531ede26/MoleculeACE/Data/benchmark_data/{benchmark_name}.csv"
            )

            # Split into train/test based on provided splits
            train_df = df[df["split"] == "train"].reset_index(drop=True)
            test_df = df[df["split"] == "test"].reset_index(drop=True)

            # Further split train into train/validation (80/20)
            train_idx = np.arange(len(train_df))
            np.random.shuffle(train_idx)
            split_idx = int(len(train_idx) * 0.8)
            train_idx, val_idx = train_idx[:split_idx], train_idx[split_idx:]

            # Create datasets
            train_dataset = MolDataset(
                train_df.iloc[train_idx],
                smiles_column=smiles_col,
                target_column=target_col,
            )
            val_dataset = MolDataset(
                train_df.iloc[val_idx],
                smiles_column=smiles_col,
                target_column=target_col,
            )
            test_dataset = MolDataset(
                test_df, smiles_column=smiles_col, target_column=target_col
            )

            # Create dataloaders
            train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
            val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)
            test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

            # Configure MolCLR model
            config = {
                "batch_size": 32,
                "epochs": 50,
                "eval_every_n_epochs": 1,
                "fine_tune_from": "pretrained_gcn",
                "log_every_n_steps": 50,
                "init_lr": 0.0005,
                "init_base_lr": 0.0001,
                "weight_decay": "1e-6",
                "gpu": "cuda:0" if torch.cuda.is_available() else "cpu",
                "task_name": benchmark_name,
                "model_type": "gcn",
                "model": {
                    "num_layer": 5,
                    "emb_dim": 300,
                    "feat_dim": 512,
                    "drop_ratio": 0.3,
                    "pool": "mean",
                },
                "dataset": {"task": "regression", "target": target_col},
            }

            # Initialize MolCLR finetuner
            finetuner = MolCLRFineTuner(config, train_loader, val_loader, test_loader)

            # Train the model
            model = finetuner.train(random_seed)

            # Evaluate the model on test set
            predictions, labels, test_rmse, test_mae = finetuner.evaluate(
                model, test_loader
            )

            # Calculate performance for ACE cliff and noncliff compounds
            test_df_with_preds = test_df.copy()
            test_df_with_preds["predictions"] = predictions

            # Calculate RMSE for cliff and non-cliff compounds
            if "cliff_mol" in test_df.columns:
                # If cliff_mol column exists, use it to separate cliff vs. non-cliff
                cliff_df = test_df_with_preds[test_df_with_preds["cliff_mol"] == 1]
                noncliff_df = test_df_with_preds[test_df_with_preds["cliff_mol"] == 0]

                cliff_rmse = 0
                noncliff_rmse = 0

                if len(cliff_df) > 0:
                    cliff_rmse = calculate_rmse(
                        cliff_df[target_col], cliff_df["predictions"]
                    )

                if len(noncliff_df) > 0:
                    noncliff_rmse = calculate_rmse(
                        noncliff_df[target_col], noncliff_df["predictions"]
                    )
            else:
                # If cliff_mol column doesn't exist, calculate overall RMSE only
                # and set cliff and non-cliff RMSEs to the same value
                cliff_rmse = test_rmse
                noncliff_rmse = test_rmse

            # Write results to markdown file in the same format as minimol.md
            output_file.write("| metric             |    value |\n")
            output_file.write("|:-------------------|---------:|\n")
            output_file.write(f"| overall test rmse  | {test_rmse:.6f} |\n")
            output_file.write(f"| noncliff test rmse | {noncliff_rmse:.6f} |\n")
            output_file.write(f"| cliff test rmse    | {cliff_rmse:.6f} |\n\n\n")

            # Store performance metrics in dictionary
            performance = {"cliff": cliff_rmse, "noncliff": noncliff_rmse}
            performance_dict[benchmark_name] = performance

        # After processing all benchmarks for this seed, write the summary with results_dict
        output_file.write(
            f"""
### Summary

```
results_dict = {json.dumps(performance_dict, indent=4)}
```
"""
        )

    output_file.close()
    print(
        f"Training and evaluation complete. Results saved to {output_dir / 'train_results.md'}"
    )
