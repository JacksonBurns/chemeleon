import datetime
import json
import logging
import os
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
import yaml
from sklearn.metrics import (mean_absolute_error, mean_squared_error,
                             roc_auc_score)
from sklearn.model_selection import train_test_split
from torch import nn
from torch.optim.lr_scheduler import CosineAnnealingLR
from torch.utils.data import Dataset
from torch.utils.data.sampler import SubsetRandomSampler
from torch.utils.tensorboard import SummaryWriter
from torch_geometric.data import Data, DataLoader
from tqdm import tqdm

# MolCLR imports
sys.path.append("/home/akshatz/MolCLR")
import rdkit
from dataset.dataset_test import (ATOM_LIST, BOND_LIST, BONDDIR_LIST,
                                  CHIRALITY_LIST)
from rdkit import Chem, RDLogger
from rdkit.Chem.rdchem import BondType as BT
from rdkit.Chem.rdchem import HybridizationType

from models.gcn_finetune import GCN

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


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

# Constants
RANDOM_SEEDS = [42, 117, 709, 1701, 9001]  # 5 different seeds for multiple splits


class MolDataset(Dataset):
    def __init__(self, df, smiles_column, target_column=None, classification=False):
        self.df = df
        self.smiles_column = smiles_column
        self.target_column = target_column
        self.classification = classification

        self.smiles_data = df[smiles_column].values

        if target_column is not None:
            if classification:
                self.labels = df[target_column].values.astype(np.int64)
            else:
                self.labels = df[target_column].values.astype(np.float32)
        else:
            # For test datasets without labels
            self.labels = None

    def __getitem__(self, index):
        mol = Chem.MolFromSmiles(self.smiles_data[index])
        if mol is None:
            logger.warning(f"Invalid SMILES: {self.smiles_data[index]}")
            # Return a placeholder for invalid SMILES to avoid breaking the dataloader
            return self.__getitem__(0) if index != 0 else None

        mol = Chem.AddHs(mol)

        # Prepare node features
        type_idx = []
        chirality_idx = []
        for atom in mol.GetAtoms():
            atom_idx = (
                ATOM_LIST.index(atom.GetAtomicNum())
                if atom.GetAtomicNum() in ATOM_LIST
                else 0
            )
            chiral_idx = CHIRALITY_LIST.index(atom.GetChiralTag())
            type_idx.append(atom_idx)
            chirality_idx.append(chiral_idx)

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

        if len(row) == 0:  # Molecule with no bonds
            edge_index = torch.zeros((2, 0), dtype=torch.long)
            edge_attr = torch.zeros((0, 2), dtype=torch.long)
        else:
            edge_index = torch.tensor([row, col], dtype=torch.long)
            edge_attr = torch.tensor(np.array(edge_feat), dtype=torch.long)

        # Target value
        if self.labels is not None:
            if self.classification:
                y = torch.tensor(self.labels[index], dtype=torch.long)
            else:
                y = torch.tensor(self.labels[index], dtype=torch.float).view(1, -1)
        else:
            y = torch.tensor(0, dtype=torch.float).view(
                1, -1
            )  # Placeholder for test sets without labels

        data = Data(x=x, y=y, edge_index=edge_index, edge_attr=edge_attr)
        return data

    def __len__(self):
        return len(self.smiles_data)


def calculate_rmse(y_true, y_pred):
    # Make sure arrays have same shape
    if y_true.shape != y_pred.shape:
        logger.warning(
            f"Shape mismatch in calculate_rmse: y_true {y_true.shape}, y_pred {y_pred.shape}"
        )
        # If there's a shape mismatch, try to fix it
        if len(y_pred.shape) > 1 and y_pred.shape[1] == 2:
            # Binary classification case, take only probability of class 1
            y_pred = y_pred[:, 1]

    return np.sqrt(mean_squared_error(y_true, y_pred))


class MolCLRFineTuner:
    def __init__(self, config, train_loader, val_loader, test_loader):
        self.config = config
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.test_loader = test_loader
        self.device = self._get_device()
        self.classification = config.get("classification", False)

        # Set criterion based on task type
        if self.classification:
            self.criterion = nn.CrossEntropyLoss()
        else:
            self.criterion = nn.MSELoss()

        # Create model
        self.model = self._create_model()

        # Prepare training directories
        current_time = datetime.datetime.now().strftime("%b%d_%H-%M-%S")
        task_suffix = config["task_name"]
        dir_name = current_time + "_" + task_suffix
        log_dir = os.path.join("finetune_outputs", dir_name)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        self.log_dir = log_dir
        self.writer = SummaryWriter(log_dir=log_dir)

        # Create normalizer for regression targets (only for regression tasks)
        self.normalizer = None
        if not self.classification:
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
        from models.gcn_finetune import GCN

        task_type = "classification" if self.classification else "regression"

        # GCN model doesn't accept num_class parameter, it's hardcoded to 2 for classification in the model
        model = GCN(
            task_type,
            num_layer=self.config["model"].get("num_layer", 5),
            emb_dim=self.config["model"].get("emb_dim", 300),
            feat_dim=self.config["model"].get("feat_dim", 512),
            drop_ratio=self.config["model"].get("drop_ratio", 0.3),
            pool=self.config["model"].get("pool", "mean"),
        ).to(self.device)

        model = self._load_pre_trained_weights(model)
        return model

    def _load_pre_trained_weights(self, model):
        try:
            # Load either from a specified checkpoint or from the default MolCLR path
            if "checkpoint_path" in self.config and os.path.exists(
                self.config["checkpoint_path"]
            ):
                state_dict = torch.load(
                    self.config["checkpoint_path"], map_location=self.device
                )
                model.load_state_dict(state_dict, strict=False)
            else:
                molclr_path = (
                    "/home/akshatz/MolCLR/ckpt/pretrained_gcn/checkpoints/model.pth"
                )
                if os.path.exists(molclr_path):
                    state_dict = torch.load(molclr_path, map_location=self.device)
                    model.load_state_dict(state_dict, strict=False)
                    logger.info("Loaded pre-trained MolCLR weights")
                else:
                    logger.warning(
                        "Pre-trained weights not found. Training from scratch."
                    )
        except Exception as e:
            logger.error(f"Error loading pre-trained weights: {e}")
            logger.info("Training from scratch.")
        return model

    def _step(self, model, data):
        data = data.to(self.device)

        if self.classification:
            _, logits = model(data)
            loss = self.criterion(logits, data.y)
            pred = F.softmax(logits, dim=1)
        else:
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

            # Validate model
            if epoch % self.config["eval_every_n_epochs"] == 0:
                valid_loss, valid_rmse = self._validate(model, self.val_loader)
                self.writer.add_scalar(
                    f"valid_loss_{random_seed}", valid_loss, global_step=valid_n_iter
                )
                self.writer.add_scalar(
                    f"valid_rmse_{random_seed}", valid_rmse, global_step=valid_n_iter
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

                # Handle predictions differently based on task type
                if self.classification:
                    # For binary classification, use the probability of class 1
                    # This ensures predictions has same length as labels
                    if self.device == "cpu":
                        # Take only column 1 (probability of positive class) for binary classification
                        batch_preds = pred.detach().numpy()[:, 1]
                        batch_labels = data.y.detach().numpy()
                    else:
                        batch_preds = pred.cpu().detach().numpy()[:, 1]
                        batch_labels = data.y.cpu().detach().numpy()

                    predictions.extend(batch_preds)
                    labels.extend(batch_labels)
                else:
                    # For regression, denormalize the predictions
                    pred = self.normalizer.denorm(pred)

                    # Extract predictions and flatten them
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

        # Calculate RMSE regardless of task type
        # For classification, this measures how well our probability estimates match the binary labels
        rmse = calculate_rmse(labels, predictions)

        model.train()
        return valid_loss, rmse

    # Note: The evaluate method was removed as it's not used in this script
    # We want to avoid metric calculations on test data since we have no ground truth labels


def process_benchmark(
    benchmark_dir, benchmark_name, output_dir, is_classification=False
):
    """Process a single benchmark dataset with multiple train/val splits"""
    logger.info(f"Processing benchmark: {benchmark_name}")

    # Create category-specific output directories
    category = "classification" if is_classification else "regression"
    category_output_dir = os.path.join(output_dir, category)
    os.makedirs(category_output_dir, exist_ok=True)

    # Create output directory for this benchmark
    benchmark_output_dir = os.path.join(category_output_dir, benchmark_name)
    os.makedirs(benchmark_output_dir, exist_ok=True)

    # Load metadata
    metadata_file = os.path.join(benchmark_dir, f"{benchmark_name}_metadata.json")
    with open(metadata_file, "r") as f:
        metadata = json.load(f)

    # Extract relevant info from metadata
    smiles_column = metadata["smiles_column"]
    target_columns = metadata["target_columns"]
    target_column = target_columns[0]  # For now, we'll use only the first target column

    # Load train and test data
    train_file = os.path.join(benchmark_dir, f"{benchmark_name}_train.csv")
    test_file = os.path.join(benchmark_dir, f"{benchmark_name}_test.csv")

    train_df = pd.read_csv(train_file)
    test_df = pd.read_csv(test_file)

    logger.info(
        f"Loaded {len(train_df)} training samples and {len(test_df)} test samples"
    )

    # Prepare test predictions dataframe which will contain predictions for each seed
    test_predictions = test_df.copy()

    # Train models with 5 different random seeds
    for seed in RANDOM_SEEDS:
        logger.info(f"Training with seed {seed}")

        # Set random seed for reproducibility
        torch.manual_seed(seed)
        np.random.seed(seed)

        # Split training data into train and validation (80/20)
        train_indices, val_indices = train_test_split(
            np.arange(len(train_df)), test_size=0.2, random_state=seed
        )

        # Create datasets
        train_dataset = MolDataset(
            train_df, smiles_column, target_column, classification=is_classification
        )
        test_dataset = MolDataset(
            test_df, smiles_column, classification=is_classification
        )

        # Create data loaders using samplers for train/val split
        train_sampler = SubsetRandomSampler(train_indices)
        val_sampler = SubsetRandomSampler(val_indices)

        train_loader = DataLoader(
            train_dataset,
            batch_size=32,
            sampler=train_sampler,
            num_workers=4,
            drop_last=False,
        )
        val_loader = DataLoader(
            train_dataset,
            batch_size=32,
            sampler=val_sampler,
            num_workers=4,
            drop_last=False,
        )
        test_loader = DataLoader(
            test_dataset, batch_size=32, shuffle=False, num_workers=4, drop_last=False
        )

        # Configure MolCLR model
        model_type = "classification" if is_classification else "regression"
        # Note: GCN model has hardcoded output size of 2 for classification tasks

        # Initialize model, optimizer, etc.
        config = {
            "batch_size": 32,
            "epochs": 50,
            "eval_every_n_epochs": 1,
            "fine_tune_from": "pretrained",
            "log_every_n_steps": 50,
            "init_lr": 0.0005,
            "init_base_lr": 0.0001,
            "weight_decay": "1e-6",
            "gpu": "cuda:0" if torch.cuda.is_available() else "cpu",
            "task_name": f"{benchmark_name}_seed_{seed}",
            "model_type": "gcn",
            "model": {
                "num_layer": 5,
                "emb_dim": 300,
                "feat_dim": 512,
                "drop_ratio": 0.3,
                "pool": "mean",
            },
            "dataset": {"task": model_type, "target": target_column},
            "classification": is_classification,
        }

        # Initialize and train the model
        finetuner = MolCLRFineTuner(config, train_loader, val_loader, test_loader)
        model = finetuner.train(seed)

        # Make predictions on test set
        predictions = []

        with torch.no_grad():
            model.eval()
            for data in test_loader:
                data = data.to(finetuner.device)
                if is_classification:
                    _, logits = model(data)
                    pred = F.softmax(logits, dim=1)
                    # For binary classification, just use the probability of class 1
                    pred = pred[:, 1] if pred.shape[1] == 2 else pred
                else:
                    _, pred = model(data)
                    # Denormalize predictions for regression tasks
                    pred = finetuner.normalizer.denorm(pred)

                # Extract predictions
                if finetuner.device == "cpu":
                    batch_preds = pred.detach().numpy()
                else:
                    batch_preds = pred.cpu().detach().numpy()

                # At this point for binary classification, pred should already be a 1D array
                # For regression, it might need flattening
                if len(batch_preds.shape) > 1:
                    batch_preds = batch_preds.reshape(-1)

                predictions.extend(batch_preds.tolist())

        # Add predictions to the test dataframe
        test_predictions[f"seed_{seed}"] = predictions

        # Save the model checkpoint
        checkpoint_path = os.path.join(benchmark_output_dir, f"model_seed_{seed}.pt")
        torch.save(model.state_dict(), checkpoint_path)
        logger.info(f"Saved model checkpoint to {checkpoint_path}")

    # Save predictions without aggregation
    # We don't calculate any metrics since we don't have the ground truth for test set

    # Create ensemble prediction (mean of all seeds)
    seed_columns = [f"seed_{seed}" for seed in RANDOM_SEEDS]
    # test_predictions["ensemble_mean"] = test_predictions[seed_columns].mean(axis=1)

    # Save final predictions (individual seed predictions and ensemble)
    output_path = os.path.join(
        benchmark_output_dir, f"{benchmark_name}_test_predictions.csv"
    )
    test_predictions.to_csv(output_path, index=False)

    # Save metadata for this benchmark
    metadata_output = {
        "benchmark_name": benchmark_name,
        "is_classification": is_classification,
        "task_type": "classification" if is_classification else "regression",
        "model_type": "MolCLR-GCN",
        "target_column": target_column,
        "smiles_column": smiles_column,
        "seeds": RANDOM_SEEDS,
        "model_path": os.path.abspath(benchmark_output_dir),
        "train_samples": len(train_df),
        "test_samples": len(test_df),
        "timestamp": datetime.datetime.now().isoformat(),
    }

    # Save metadata as JSON
    metadata_path = os.path.join(
        benchmark_output_dir, f"{benchmark_name}_metadata.json"
    )
    with open(metadata_path, "w") as f:
        json.dump(metadata_output, f, indent=2)

    logger.info(f"Saved test predictions to {output_path}")
    logger.info(f"Saved metadata to {metadata_path}")


def create_evaluation_metadata(output_dir):
    """Create metadata file that will help the evaluation script"""
    regression_dir = os.path.join(output_dir, "regression")
    classification_dir = os.path.join(output_dir, "classification")

    # Collect all benchmarks
    all_benchmarks = {"regression": [], "classification": []}

    # Find regression benchmarks
    if os.path.exists(regression_dir):
        for benchmark_dir in os.listdir(regression_dir):
            benchmark_path = os.path.join(regression_dir, benchmark_dir)
            if os.path.isdir(benchmark_path):
                all_benchmarks["regression"].append(benchmark_dir)

    # Find classification benchmarks
    if os.path.exists(classification_dir):
        for benchmark_dir in os.listdir(classification_dir):
            benchmark_path = os.path.join(classification_dir, benchmark_dir)
            if os.path.isdir(benchmark_path):
                all_benchmarks["classification"].append(benchmark_dir)

    # Create summary information
    summary_info = {
        "model_name": "MolCLR-GCN",
        "timestamp": datetime.datetime.now().isoformat(),
        "benchmarks": all_benchmarks,
        "seeds": RANDOM_SEEDS,
        "output_directory": str(output_dir),
    }

    # Save as JSON for easy loading in evaluate script
    eval_metadata_path = os.path.join(output_dir, "evaluation_metadata.json")
    with open(eval_metadata_path, "w") as f:
        json.dump(summary_info, f, indent=2)

    logger.info(f"Created evaluation metadata file at {eval_metadata_path}")
    return eval_metadata_path


if __name__ == "__main__":
    # Parse command line arguments
    if len(sys.argv) < 2:
        print("Usage: python train_model.py OUTPUT_DIR [BENCHMARKS_DIR]")
        sys.exit(1)

    output_dir = Path(sys.argv[1])
    benchmarks_dir = (
        Path(sys.argv[2])
        if len(sys.argv) > 2
        else Path("/home/akshatz/fastprop_foundation/models/molclr/polaris_benchmarks")
    )

    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    # Find all benchmark directories
    regression_dir = os.path.join(benchmarks_dir, "regression")
    classification_dir = os.path.join(benchmarks_dir, "classification")

    logger.info(f"Processing benchmarks from: {benchmarks_dir}")

    # Create output directory structure
    regression_output_dir = os.path.join(output_dir, "regression")
    classification_output_dir = os.path.join(output_dir, "classification")
    os.makedirs(regression_output_dir, exist_ok=True)
    os.makedirs(classification_output_dir, exist_ok=True)

    # Create a summary file
    summary_path = output_dir / "molclr_summary.md"
    with open(summary_path, "w") as summary_file:
        summary_file.write("# MolCLR Model Training Results\n\n")
        summary_file.write(f"Timestamp: {datetime.datetime.now()}\n\n")

        # Process regression benchmarks
        if os.path.exists(regression_dir):
            summary_file.write("## Regression Benchmarks\n\n")
            summary_file.write("| Benchmark | Status | Seeds |\n")
            summary_file.write("|-----------|--------|-------|\n")

            # Find all benchmark train files
            regression_files = [
                f for f in os.listdir(regression_dir) if f.endswith("_train.csv")
            ]

            for train_file in regression_files:
                benchmark_name = train_file.replace("_train.csv", "")
                summary_file.write(
                    f"| {benchmark_name} | Processing | {', '.join(map(str, RANDOM_SEEDS))} |\n"
                )
                process_benchmark(
                    regression_dir, benchmark_name, output_dir, is_classification=False
                )
                # Update status to completed
                summary_file.seek(
                    summary_file.tell()
                    - len(
                        f"| {benchmark_name} | Processing | {', '.join(map(str, RANDOM_SEEDS))} |\n"
                    )
                )
                summary_file.write(
                    f"| {benchmark_name} | Completed | {', '.join(map(str, RANDOM_SEEDS))} |\n"
                )

        # Process classification benchmarks
        if os.path.exists(classification_dir):
            summary_file.write("\n## Classification Benchmarks\n\n")
            summary_file.write("| Benchmark | Status | Seeds |\n")
            summary_file.write("|-----------|--------|-------|\n")

            # Find all benchmark train files
            classification_files = [
                f for f in os.listdir(classification_dir) if f.endswith("_train.csv")
            ]

            for train_file in classification_files:
                benchmark_name = train_file.replace("_train.csv", "")
                summary_file.write(
                    f"| {benchmark_name} | Processing | {', '.join(map(str, RANDOM_SEEDS))} |\n"
                )
                process_benchmark(
                    classification_dir,
                    benchmark_name,
                    output_dir,
                    is_classification=True,
                )
                # Update status to completed
                summary_file.seek(
                    summary_file.tell()
                    - len(
                        f"| {benchmark_name} | Processing | {', '.join(map(str, RANDOM_SEEDS))} |\n"
                    )
                )
                summary_file.write(
                    f"| {benchmark_name} | Completed | {', '.join(map(str, RANDOM_SEEDS))} |\n"
                )

    # Create evaluation metadata file to help the evaluate.py script
    eval_metadata_path = create_evaluation_metadata(output_dir)
    logger.info(
        f"All benchmarks processed. Evaluation metadata saved to {eval_metadata_path}"
    )
