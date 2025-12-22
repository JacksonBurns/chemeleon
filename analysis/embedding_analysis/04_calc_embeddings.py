"""Calculate embeddings for molecule datasets."""

import argparse
from pathlib import Path
from urllib.request import urlretrieve

import numpy as np
import pandas as pd
import torch
from chemprop.data import (
    MoleculeDatapoint,
    MoleculeDataset,
    build_dataloader,
    BatchMolGraph,
)
from chemprop.models import MPNN
from sklearn.model_selection import train_test_split
from lightning.pytorch.callbacks import EarlyStopping
from lightning.pytorch.callbacks import ModelCheckpoint
from chemprop.nn import BondMessagePassing, MeanAggregation, BinaryClassificationFFN
from lightning import seed_everything, Trainer
from lightning.pytorch.loggers import TensorBoardLogger
from loguru import logger
from sklearn.model_selection import PredefinedSplit

from common import parse_endpoint_input


def from_chemeleon(no_weights: bool = False) -> BondMessagePassing:
    """Load CheMeleon foundation model for message passing block initialization.

    See https://github.com/chemprop/chemprop/blob/751102dec3c5186d348b6cc80822e3c31cf39840/chemprop/cli/train.py#L1251

    Returns
    -------
    BondMessagePassing
        Message passing block initialized with CheMeleon weights.
    """
    ckpt_dir = Path().home() / ".chemprop"
    ckpt_dir.mkdir(exist_ok=True)
    model_path = ckpt_dir / "chemeleon_mp.pt"
    if not model_path.exists():
        logger.info(
            f"Downloading CheMeleon Foundation model from Zenodo (https://zenodo.org/records/15460715) to {model_path}"
        )
        urlretrieve(
            r"https://zenodo.org/records/15460715/files/chemeleon_mp.pt", model_path
        )
    else:
        logger.info(f"Loading cached CheMeleon from {model_path}")
    logger.info(
        "Please cite DOI: 10.48550/arXiv.2506.15792 when using CheMeleon in published work"
    )
    chemeleon_mp = torch.load(model_path, weights_only=True)

    mp_block = BondMessagePassing(**chemeleon_mp["hyper_parameters"])
    if not no_weights:
        mp_block.load_state_dict(chemeleon_mp["state_dict"])
    return mp_block


def smiles_table_to_chemprop_molecule_datapoints(
    df_data: pd.DataFrame,
    smiles_col: str,
    label_cols: list[str],
) -> list[MoleculeDatapoint]:
    """Convert a SMILES table to a list of Chemprop's MoleculeDatapoints.

    Parameters
    ----------
    df_data : pd.DataFrame
        DataFrame containing the data.
    smiles_col : str
        Name of the column containing SMILES strings.
    label_cols : list[str]
        Names of the columns containing labels.

    Returns
    -------
    list[MoleculeDatapoint]
        List of Chemprop MoleculeDatapoint objects.
    """
    # remove rows with missing values in relevant columns.
    df_data_ref = df_data.dropna(subset=[smiles_col, *label_cols], how="any")

    smiles = df_data_ref.loc[:, smiles_col].to_numpy()
    ys = df_data_ref.loc[:, label_cols].to_numpy()

    datapoints = [
        MoleculeDatapoint.from_smi(smi, y) for smi, y in zip(smiles, ys, strict=True)
    ]
    return datapoints


def smiles_table_to_chemprop_molecule_dataset(
    df_data: pd.DataFrame,
    smiles_col: str,
    label_cols: list[str],
) -> MoleculeDataset:
    """Convert a SMILES table to a Chemprop MoleculeDataset.

    Parameters
    ----------
    df_data : pd.DataFrame
        DataFrame containing the data.
    smiles_col : str
        Name of the column containing SMILES strings.
    label_cols : list[str]
        Names of the columns containing labels.

    Returns
    -------
    MoleculeDataset
        Table as MoleculeDataset.
    """
    return MoleculeDataset(
        smiles_table_to_chemprop_molecule_datapoints(df_data, smiles_col, label_cols)
    )


def main(n_jobs: int, endpoint: str, model_name: str, random_state: int | None) -> None:
    """Calculate embeddings for on datasets using different encodings.

    Parameters
    ----------
    n_jobs : int
        Number of jobs to use for data loading.
    endpoint : str
        Endpoint to train on. Can be a single endpoint or a path to a YAML file
        containing a list of endpoints.
    model_name : str
        Name of base architecture. One of ["chemprop", "chemeleon_finetuned", "chemeleon_frozen", "chemeleon_no_pretraining"].
    random_state : int | None
        Random seed for all randomizations (default: None)
    """
    base_path = Path(__file__).parents[0]
    data_path = base_path / "data"
    logger.add(base_path / "logs" / f"{Path(__file__).stem}.log")
    endpoint_list = parse_endpoint_input(endpoint)

    epochs = 50

    logger.info(f"random_state: {random_state}")
    logger.info(f"n_jobs: {n_jobs}")
    logger.info(f"model_name: {model_name}")
    logger.info(f"epochs: {epochs}")

    # Set seeds for reproducibility using best practices
    deterministic = False
    if random_state is not None:
        torch.manual_seed(random_state)
        deterministic = True
        seed_everything(random_state, workers=True)

    split_strategy_list = [
        "Random",
        "Agglomerative clustering",
        # "Murcko scaffold",
        #  "Generic scaffold",
    ]

    for ep in endpoint_list:
        logger.info(f"Calculating embeddings for endpoint: {ep}.")

        endpoint_df = pd.read_csv(
            data_path
            / "intermediate_data"
            / "presplit_data"
            / f"presplit_data_{ep}.tsv",
            sep="\t",
        )

        prediction_df_list = []
        for split_strategy in split_strategy_list:
            for trial, (train_idx, test_idx) in enumerate(
                PredefinedSplit(endpoint_df[split_strategy]).split()
            ):
                split_dir = (
                    data_path
                    / "intermediate_data"
                    / "model_data"
                    / model_name
                    / ep
                    / split_strategy
                    / f"fold_{trial}"
                )

                train_df = endpoint_df.iloc[train_idx]
                test_df = endpoint_df.iloc[test_idx].copy()


                # Split train_df into train and val (90:10)
                if model_name != "chemeleon_frozen":
                    train_df_split, val_df = train_test_split(
                        train_df,
                        test_size=0.1,
                        random_state=random_state,
                        shuffle=True,
                    )
                else:
                    train_df_split = train_df
                    val_df = None

                train_dataset = smiles_table_to_chemprop_molecule_dataset(
                    train_df_split,
                    smiles_col="smiles",
                    label_cols=["label"],
                )

                if val_df is not None:
                    val_dataset = smiles_table_to_chemprop_molecule_dataset(
                        val_df,
                        smiles_col="smiles",
                        label_cols=["label"],
                    )
                    val_dataloader = build_dataloader(
                        val_dataset, num_workers=n_jobs, shuffle=False
                    )
                else:
                    val_dataloader = None

                test_dataset = smiles_table_to_chemprop_molecule_dataset(
                    test_df,
                    smiles_col="smiles",
                    label_cols=["label"],
                )

                train_dataloader = build_dataloader(
                    train_dataset, num_workers=n_jobs, shuffle=True
                )
                test_dataloader = build_dataloader(
                    test_dataset, num_workers=n_jobs, shuffle=False
                )

                if model_name == "chemeleon_finetuned":
                    mp = from_chemeleon()
                elif model_name == "chemeleon_frozen":
                    mp = from_chemeleon()
                elif model_name == "chemeleon_no_pretraining":
                    mp = from_chemeleon(no_weights=True)
                elif model_name == "chemprop":
                    mp = BondMessagePassing()
                else:
                    raise ValueError(f"{model_name} is not a valid model")
                agg = MeanAggregation()
                output_transform = None
                fnn = BinaryClassificationFFN(
                    output_transform=output_transform,
                    input_dim=mp.output_dim,
                    hidden_dim=300,
                )
                model = MPNN(
                    mp,
                    agg,
                    fnn,
                )

                tensorboard_logger = TensorBoardLogger(
                    split_dir,
                    name="tensorboard_logs",
                    default_hp_metric=False,
                )

                # Setup callbacks for early stopping and checkpointing
                callbacks = []
                if val_dataloader is not None:
                    callbacks = [
                        EarlyStopping(
                            monitor="val_loss",
                            mode="min",
                            verbose=False,
                            patience=5,
                        ),
                        ModelCheckpoint(
                            monitor="val_loss",
                            save_top_k=2,
                            mode="min",
                            dirpath=split_dir / "checkpoints",
                        ),
                    ]

                trainer = Trainer(
                    max_epochs=epochs,
                    logger=tensorboard_logger,
                    log_every_n_steps=1,
                    enable_checkpointing=True,
                    check_val_every_n_epoch=1,
                    deterministic=deterministic,
                    callbacks=callbacks,
                )

                if model_name == "chemeleon_frozen":
                    # Freeze all model parameters
                    for param in model.parameters():
                        param.requires_grad = False
                else:
                    trainer.fit(model, train_dataloader, val_dataloaders=val_dataloader)

                # save test set predictions
                predictions = (
                    torch.vstack(trainer.predict(model, test_dataloader))
                    .numpy(force=True)
                    .flatten()
                )
                test_df["proba"] = predictions
                test_df["prediction"] = test_df["proba"] > 0.5
                test_df["endpoint"] = ep
                test_df["trial"] = trial
                test_df["Split strategy"] = split_strategy
                test_df["model"] = model_name
                prediction_df_list.append(test_df)

                # save fingerprints
                with torch.inference_mode():
                    train_mol_graphs = [data_point.mg for data_point in train_dataset]
                    train_fingerprints = (
                        model.fingerprint(BatchMolGraph(train_mol_graphs))
                        .detach()
                        .cpu()
                        .numpy()
                    )
                    test_mol_graphs = [data_point.mg for data_point in test_dataset]
                    test_fingerprints = (
                        model.fingerprint(BatchMolGraph(test_mol_graphs))
                        .detach()
                        .cpu()
                        .numpy()
                    )

                # sanity checks
                if len(train_fingerprints) != train_df.shape[0]:
                    raise ValueError("Invalid shapes in train fingerprints")
                if len(test_fingerprints) != test_df.shape[0]:
                    raise ValueError("Invalid shapes in train fingerprints")

                np.save(
                    split_dir / "train_fps.npy", train_fingerprints, allow_pickle=False
                )
                np.save(
                    split_dir / "test_fps.npy", test_fingerprints, allow_pickle=False
                )

        prediction_df = pd.concat(prediction_df_list)
        prediction_df.to_csv(
            data_path
            / "intermediate_data"
            / "model_data"
            / model_name
            / ep
            / "test_predictions.tsv",
            sep="\t",
            index=False,
        )


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--n_jobs",
        type=int,
        default=1,
        help="Number of jobs to use for training.",
    )
    argument_parser.add_argument(
        "--endpoint",
        type=str,
        help="Endpoint to train on.",
    )
    argument_parser.add_argument(
        "--model-name",
        required=True,
        type=str,
        choices=["chemprop", "chemeleon_finetuned", "chemeleon_frozen", "chemeleon_no_pretraining"],
        help="Name of base architecture.",
    )
    argument_parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random seed for all randomizations (default: None)",
    )
    args = argument_parser.parse_args()
    main(args.n_jobs, args.endpoint, args.model_name, args.seed)
