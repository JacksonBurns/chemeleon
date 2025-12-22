"""KNN evaluation of representations."""

import argparse
from pathlib import Path

import numpy as np
import numpy.typing as npt
import pandas as pd
from common import (REPRESENTATION_INFOS, RepresentationInfo,
                    parse_endpoint_input)
from loguru import logger
from sklearn.metrics import (average_precision_score, balanced_accuracy_score,
                             f1_score, precision_score, recall_score,
                             roc_auc_score)
from sklearn.model_selection import PredefinedSplit
from sklearn.neighbors import KNeighborsClassifier, NearestNeighbors
from sklearn.preprocessing import StandardScaler


def prepare_feat_for_knn(
    feat_train: npt.NDArray[np.float64],
    feat_test: npt.NDArray[np.float64],
    repr_info: RepresentationInfo,
) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]:
    """Prepare features for KNN calculation.

    Parameters
    ----------
    feat_train : npt.NDArray[np.float64]
        Training feature matrix.
    feat_test : npt.NDArray[np.float64]
        Test feature matrix.
    repr_info : RepresentationInfo
        Representation info.

    Returns
    -------
    tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]
        Prepared training and test feature matrices.
    """
    # typically mordred or rdkit physchem can contain nan values for descriptors
    # that could not be calculated. Drop columns with any nan
    valid_col_mask = ~(
        np.isnan(feat_train).any(axis=0) | np.isnan(feat_test).any(axis=0)
    )
    if valid_col_mask.sum() != valid_col_mask.shape[0]:
        logger.info(
            f"dropping {valid_col_mask.shape[0] - valid_col_mask.sum()} columns with "
            f"NaNs for: {repr_info.representation_type}"
        )
    feat_train = feat_train[:, valid_col_mask]
    feat_test = feat_test[:, valid_col_mask]

    if repr_info.need_standardization:
        scaler = StandardScaler()
        feat_train = scaler.fit_transform(feat_train)
        feat_test = scaler.transform(feat_test)

    if repr_info.distance_measure == "jaccard":
        # avoid costly copies on scipy's side and convert them here
        feat_train = feat_train.astype(bool)
        feat_test = feat_test.astype(bool)

    return feat_train, feat_test


def calc_knn(
    feat_train: npt.NDArray[np.float64],
    feat_test: npt.NDArray[np.float64],
    repr_info: RepresentationInfo,
    k: int,
    n_jobs: int,
) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.int64]]:
    """Calculate the k-nearest neighbors and their distances.

    Parameters
    ----------
    feat_train : npt.NDArray[np.float64]
        Training feature matrix.
    feat_test : npt.NDArray[np.float64]
        Test feature matrix.
    repr_info : RepresentationInfo
        Representation info.
    k : int
        Maximum number of neighbors to consider.
    n_jobs : int
        Number of jobs to use.

    Returns
    -------
    tuple[npt.NDArray[np.float64], npt.NDArray[np.int64]]
        Distances and indices of the k-nearest neighbors.
    """
    nn = NearestNeighbors(
        n_neighbors=k, metric=repr_info.distance_measure, n_jobs=n_jobs
    )
    nn.fit(feat_train)
    neigh_dist, neigh_index = nn.kneighbors(feat_test)
    return neigh_dist, neigh_index


def calc_knn_proba(
    neigh_dist: npt.NDArray[np.float64],
    neigh_index: npt.NDArray[np.int64],
    train_labels: npt.NDArray[np.int64],
    weighting_strategy: str,
) -> npt.NDArray[np.float64]:
    """Calculate KNN probabilities for each k.

    Parameters
    ----------
    neigh_dist : npt.NDArray[np.float64]
        Distances to nearest neighbors. Shape: (n_test_samples, k_max)
    neigh_index : npt.NDArray[np.int64]
        Indices of nearest neighbors. Shape: (n_test_samples, k_max)
    train_labels : npt.NDArray[np.int64]
        Labels of training samples. Shape: (n_train_samples,)
    weighting_strategy : str
        Weighting strategy to use. One of "no_weighting", "weighted_inverse",
        "weighted_temperature".
    Returns
    -------
    npt.NDArray[np.float64]
        Probabilities for each test sample and each k. Shape: (n_test_samples, k_max)
    """
    k_max = neigh_index.shape[1]
    probas = np.full((neigh_index.shape[0], k_max), np.nan)

    # Compute metrics for each k
    for k in range(1, k_max + 1):

        k_indices = neigh_index[:, :k]  # shape: (n_test_samples, k)
        k_distances = neigh_dist[:, :k]  # shape: (n_test_samples, k)
        k_labels = train_labels[k_indices]  # shape: (n_test_samples, k)

        if weighting_strategy in ["weighted_inverse", "weighted_temperature"]:
            # Distance-weighted probability calculation
            if weighting_strategy == "weighted_inverse":
                eps = 1e-10
                weights = 1.0 / (k_distances + eps)
            elif weighting_strategy == "weighted_temperature":
                temperature = 0.5
                weights = np.exp(-k_distances / temperature)
            else:
                raise ValueError(f"Unknown weighting strategy {weighting_strategy}")
            # get label 1 weights
            mask = k_labels == 1
            label_1_weights = (weights * mask).sum(axis=1)
            weights_sum = weights.sum(axis=1)
            # Weighted probability of class 1
            probas[:, k - 1] = np.divide(
                label_1_weights,
                weights_sum,
                out=np.zeros_like(probas[:, k - 1]),
                where=weights_sum > 0,
            )
        elif weighting_strategy == "no_weighting":
            probas[:, k - 1] = np.mean(k_labels, axis=1)
    return probas


def calc_metrics(
    probas: npt.NDArray[np.float64],  # shape (n_samples, k,)
    test_labels: npt.NDArray[np.int64],
) -> dict[str, npt.NDArray[np.float64]]:
    """Calculate metrics for KNN probabilities.

    Parameters
    ----------
    probas : npt.NDArray[np.float64]
        KNN probabilities. Shape: (n_samples, k_max)
    test_labels : npt.NDArray[np.int64]
        True labels for test samples. Shape: (n_samples,)

    Returns
    -------
    dict[str, npt.NDArray[np.float64]]
        Dictionary of metrics arrays for each k.
    """
    k_max = probas.shape[1]

    sensitivities = np.full(k_max, np.nan)
    specificities = np.full(k_max, np.nan)
    roc_aucs = np.full(k_max, np.nan)
    pr_aucs = np.full(k_max, np.nan)
    balanced_accuracies = np.full(k_max, np.nan)
    precisions = np.full(k_max, np.nan)
    f1_scores = np.full(k_max, np.nan)

    for i in range(k_max):
        # Convert probabilities to binary predictions
        predictions = (probas[:, i] >= 0.5).astype(np.int64)

        # Calculate metrics
        # Accuracy
        balanced_accuracies[i] = balanced_accuracy_score(test_labels, predictions)

        # Precision, F1
        precisions[i] = precision_score(test_labels, predictions, zero_division=0.0)
        f1_scores[i] = f1_score(test_labels, predictions, zero_division=0.0)
        sensitivities[i] = recall_score(test_labels, predictions, zero_division=0.0)

        # Specificity (True Negative Rate = Recall for class 0)
        # Calculate manually: TN / (TN + FP)
        mask_actual_negative = test_labels == 0
        if np.any(mask_actual_negative):
            tn = np.sum((predictions == 0) & mask_actual_negative)
            fp = np.sum((predictions == 1) & mask_actual_negative)
            specificities[i] = tn / (tn + fp) if (tn + fp) > 0 else 0.0
        else:
            specificities[i] = 0.0

        # ROC AUC (using probabilities)
        roc_aucs[i] = roc_auc_score(test_labels, probas[:, i])
        pr_aucs[i] = average_precision_score(test_labels, probas[:, i])

    return {
        "k": np.arange(1, k_max + 1, dtype=np.float64),
        "sensitivity": sensitivities,
        "specificity": specificities,
        "roc_auc": roc_aucs,
        "pr_auc": pr_aucs,
        "balanced_accuracy": balanced_accuracies,
        "precision": precisions,
        "f1": f1_scores,
    }


def read_feat_split_data(
    repr_info: RepresentationInfo,
    ep: str,
    data_path: Path,
    endpoint_df: pd.DataFrame,
    split_strategy: str,
    classical_representations: set[str],
    learned_representations: set[str],
):
    if repr_info.representation_type in classical_representations:
        # classical representations can be computed independent of the split,
        # however, we still need to split them here
        feature_matrix_path = (
            data_path
            / "intermediate_data"
            / "descriptors"
            / repr_info.representation_type
            / f"{ep}_{repr_info.representation_type}.npy"
        )

        feat_matrix = np.load(feature_matrix_path)

        for fold_i, (train_idx, test_idx) in enumerate(
            PredefinedSplit(endpoint_df[split_strategy]).split()
        ):
            feat_train = feat_matrix[train_idx]
            feat_test = feat_matrix[test_idx]
            yield fold_i, train_idx, test_idx, feat_train, feat_test
    elif repr_info.representation_type in learned_representations:
        # learned representations depend on the split. So they are already
        # in a splitted form
        folds_dir = (
            data_path
            / "intermediate_data"
            / "model_data"
            / repr_info.representation_type
            / ep
            / split_strategy
        )
        for fold_i, (train_idx, test_idx) in enumerate(
            PredefinedSplit(endpoint_df[split_strategy]).split()
        ):
            feat_train = np.load(folds_dir / f"fold_{fold_i}" / "train_fps.npy")
            feat_test = np.load(folds_dir / f"fold_{fold_i}" / "test_fps.npy")
            if len(train_idx) != len(feat_train) or len(test_idx) != len(feat_test):
                raise ValueError("Train and test indices and features inconsistent")
            yield fold_i, train_idx, test_idx, feat_train, feat_test
    else:
        raise ValueError(f"Unknown representation type {repr_info.representation_type}")


def main(n_jobs: int, endpoint: str) -> None:
    """Perform KNN probing.

    Parameters
    ----------
    n_jobs : int
        Number of jobs to use.
    endpoint : str
        Endpoint to probe. Can be endpoint name or path to YAML file with list of
        endpoints.
    """
    base_path = Path(__file__).parents[0]
    data_path = base_path / "data"
    logger.add(base_path / "logs" / f"{Path(__file__).stem}.log")
    endpoint_list = parse_endpoint_input(endpoint)

    k_max = 200
    # weighting_strategy = "no_weighting"
    weighting_strategy = "weighted_inverse"
    # weighting_strategy = "weighted_temperature"

    split_strategy_list = [
        "Random",
        "Agglomerative clustering",
        # "Murcko scaffold",
        #  "Generic scaffold",
    ]

    classical_representations = {"morgan", "morgan_count", "rdkit_physchem", "mordred"}
    learned_representations = {
        "chemeleon_finetuned",
        "chemeleon_frozen",
        "chemprop",
        "chemmprop_large",
    }
    representation_list = [*classical_representations, *learned_representations]

    metrics_df_list = []

    for ep in endpoint_list:
        endpoint_df = pd.read_csv(
            data_path
            / "intermediate_data"
            / "presplit_data"
            / f"presplit_data_{ep}.tsv",
            sep="\t",
        )
        for representation in representation_list:
            repr_info = REPRESENTATION_INFOS[representation]
            for split_strategy in split_strategy_list:
                logger.info(
                    f"Probing endpoint={ep} with representation={representation} using split={split_strategy}"
                )
                for (
                    fold_i,
                    train_idx,
                    test_idx,
                    feat_train,
                    feat_test,
                ) in read_feat_split_data(
                    repr_info,
                    ep,
                    data_path,
                    endpoint_df,
                    split_strategy,
                    classical_representations,
                    learned_representations,
                ):
                    feat_train_prep, feat_test_prep = prepare_feat_for_knn(
                        feat_train, feat_test, repr_info
                    )
                    train_labels = endpoint_df.iloc[train_idx]["label"].to_numpy()
                    test_labels = endpoint_df.iloc[test_idx]["label"].to_numpy()

                    neigh_dist, neigh_index = calc_knn(
                        feat_train=feat_train_prep,
                        feat_test=feat_test_prep,
                        repr_info=repr_info,
                        k=k_max,
                        n_jobs=n_jobs,
                    )
                    probas = calc_knn_proba(
                        neigh_dist, neigh_index, train_labels, weighting_strategy
                    )

                    metrics_dict = calc_metrics(probas, test_labels)
                    metrics_df = pd.DataFrame(metrics_dict)
                    metrics_df["endpoint"] = ep
                    metrics_df["split_strategy"] = split_strategy
                    metrics_df["representation_type"] = representation
                    metrics_df["fold"] = fold_i
                    metrics_df["num_ties"] = (probas == 0.5).sum(axis=0)
                    metrics_df_list.append(metrics_df)

    metrics_df = pd.concat(metrics_df_list)
    metrics_df.to_csv(
        data_path / "intermediate_data" / "knn_probing_metrics.tsv", sep="\t"
    )


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--n_jobs",
        type=int,
        default=1,
        help="Number of jobs to use.",
    )
    argument_parser.add_argument(
        "--endpoint",
        type=str,
        help="Endpoint to train on.",
    )
    args = argument_parser.parse_args()
    main(args.n_jobs, args.endpoint)
