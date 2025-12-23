"""KNN evaluation of representations."""

import argparse
from pathlib import Path

import numpy as np
import numpy.typing as npt
import pandas as pd
from loguru import logger
from sklearn.metrics import (average_precision_score, balanced_accuracy_score,
                             f1_score, precision_score, recall_score,
                             roc_auc_score)
from sklearn.model_selection import PredefinedSplit
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

from common import (REPRESENTATION_INFOS, RepresentationInfo,
                    parse_endpoint_input)

# ---------------------------------------------------------------------
# Feature & Metric Calculation (Original Logic)
# ---------------------------------------------------------------------
def prepare_feat_for_knn(
    feat_train: npt.NDArray[np.float64],
    feat_test: npt.NDArray[np.float64],
    repr_info: RepresentationInfo,
) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]:
    valid_col_mask = ~(np.isnan(feat_train).any(axis=0) | np.isnan(feat_test).any(axis=0))
    feat_train = feat_train[:, valid_col_mask]
    feat_test = feat_test[:, valid_col_mask]

    if repr_info.need_standardization:
        scaler = StandardScaler()
        feat_train = scaler.fit_transform(feat_train)
        feat_test = scaler.transform(feat_test)

    if repr_info.distance_measure == "jaccard":
        feat_train = feat_train.astype(bool)
        feat_test = feat_test.astype(bool)

    return feat_train, feat_test

def calc_knn(feat_train, feat_test, repr_info, k, n_jobs):
    nn = NearestNeighbors(n_neighbors=k, metric=repr_info.distance_measure, n_jobs=n_jobs)
    nn.fit(feat_train)
    neigh_dist, neigh_index = nn.kneighbors(feat_test)
    return neigh_dist, neigh_index

def calc_knn_proba(neigh_dist, neigh_index, train_labels, weighting_strategy):
    k_max = neigh_index.shape[1]
    probas = np.full((neigh_index.shape[0], k_max), np.nan)
    for k in range(1, k_max + 1):
        k_indices = neigh_index[:, :k]
        k_distances = neigh_dist[:, :k]
        k_labels = train_labels[k_indices]

        if weighting_strategy == "weighted_inverse":
            weights = 1.0 / (k_distances + 1e-10)
            mask = k_labels == 1
            label_1_weights = (weights * mask).sum(axis=1)
            weights_sum = weights.sum(axis=1)
            probas[:, k - 1] = np.divide(label_1_weights, weights_sum, out=np.zeros_like(probas[:, k - 1]), where=weights_sum > 0)
        else:
            probas[:, k - 1] = np.mean(k_labels, axis=1)
    return probas

def calc_metrics(probas, test_labels):
    k_max = probas.shape[1]
    sensitivities, specificities, roc_aucs, pr_aucs = [np.full(k_max, np.nan) for _ in range(4)]
    balanced_accuracies, precisions, f1_scores = [np.full(k_max, np.nan) for _ in range(3)]

    for i in range(k_max):
        predictions = (probas[:, i] >= 0.5).astype(np.int64)
        balanced_accuracies[i] = balanced_accuracy_score(test_labels, predictions)
        precisions[i] = precision_score(test_labels, predictions, zero_division=0.0)
        f1_scores[i] = f1_score(test_labels, predictions, zero_division=0.0)
        sensitivities[i] = recall_score(test_labels, predictions, zero_division=0.0)
        mask_neg = test_labels == 0
        if np.any(mask_neg):
            specificities[i] = np.sum((predictions == 0) & mask_neg) / np.sum(mask_neg)
        roc_aucs[i] = roc_auc_score(test_labels, probas[:, i])
        pr_aucs[i] = average_precision_score(test_labels, probas[:, i])

    return {
        "k": np.arange(1, k_max + 1, dtype=np.float64),
        "sensitivity": sensitivities, "specificity": specificities, "roc_auc": roc_aucs,
        "pr_auc": pr_aucs, "balanced_accuracy": balanced_accuracies, "precision": precisions, "f1": f1_scores,
    }

# ---------------------------------------------------------------------
# File Reader (Updated for Best/Last Suffixes)
# ---------------------------------------------------------------------
def read_feat_split_data(
    repr_info: RepresentationInfo,
    ep: str,
    data_path: Path,
    endpoint_df: pd.DataFrame,
    split_strategy: str,
    classical_representations: set[str],
    learned_representations: set[str],
    ckpt_type: str,
):
    if repr_info.representation_type in classical_representations:
        feature_matrix_path = data_path / "intermediate_data" / "descriptors" / repr_info.representation_type / f"{ep}_{repr_info.representation_type}.npy"
        feat_matrix = np.load(feature_matrix_path)
        for fold_i, (train_idx, test_idx) in enumerate(PredefinedSplit(endpoint_df[split_strategy]).split()):
            yield fold_i, train_idx, test_idx, feat_matrix[train_idx], feat_matrix[test_idx]

    elif repr_info.representation_type in learned_representations:
        folds_dir = data_path / "intermediate_data" / "model_data" / repr_info.representation_type / ep / split_strategy
        
        # Frozen model has no suffix; others use _best or _last
        is_frozen = repr_info.representation_type == "chemeleon_frozen"
        suffix = "" if is_frozen else f"_{ckpt_type}"

        for fold_i, (train_idx, test_idx) in enumerate(PredefinedSplit(endpoint_df[split_strategy]).split()):
            feat_train = np.load(folds_dir / f"fold_{fold_i}" / f"train_fps{suffix}.npy")
            feat_test = np.load(folds_dir / f"fold_{fold_i}" / f"test_fps{suffix}.npy")
            yield fold_i, train_idx, test_idx, feat_train, feat_test

# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------
def main(n_jobs: int, endpoint: str, ckpt_type: str) -> None:
    base_path = Path(__file__).parents[0]
    data_path = base_path / "data"
    logger.add(base_path / "logs" / f"{Path(__file__).stem}.log")
    endpoint_list = parse_endpoint_input(endpoint)

    k_max = 200
    weighting_strategy = "weighted_inverse"
    split_strategy_list = ["Random", "Agglomerative clustering"]
    classical_representations = {"morgan", "morgan_count", "rdkit_physchem", "mordred"}
    learned_representations = {"chemeleon_finetuned", "chemeleon_frozen", "chemprop", "chemprop_large"}
    representation_list = [*classical_representations, *learned_representations]

    metrics_df_list = []

    for ep in endpoint_list:
        endpoint_df = pd.read_csv(data_path / "intermediate_data" / "presplit_data" / f"presplit_data_{ep}.tsv", sep="\t")
        for representation in representation_list:
            repr_info = REPRESENTATION_INFOS[representation]
            for split_strategy in split_strategy_list:
                logger.info(f"EP={ep} | Repr={representation} | Split={split_strategy} | Mode={ckpt_type}")
                
                gen = read_feat_split_data(repr_info, ep, data_path, endpoint_df, split_strategy, classical_representations, learned_representations, ckpt_type)

                for fold_i, train_idx, test_idx, feat_train, feat_test in gen:
                    feat_train_prep, feat_test_prep = prepare_feat_for_knn(feat_train, feat_test, repr_info)
                    train_labels = endpoint_df.iloc[train_idx]["label"].to_numpy()
                    test_labels = endpoint_df.iloc[test_idx]["label"].to_numpy()

                    neigh_dist, neigh_index = calc_knn(feat_train_prep, feat_test_p := feat_test_prep, repr_info, k_max, n_jobs)
                    probas = calc_knn_proba(neigh_dist, neigh_index, train_labels, weighting_strategy)

                    metrics_dict = calc_metrics(probas, test_labels)
                    metrics_df = pd.DataFrame(metrics_dict)
                    
                    # COLUMNS KEPT EXACTLY AS ORIGINAL
                    metrics_df["endpoint"] = ep
                    metrics_df["split_strategy"] = split_strategy
                    metrics_df["representation_type"] = representation
                    metrics_df["fold"] = fold_i
                    metrics_df["num_ties"] = (probas == 0.5).sum(axis=0)
                    metrics_df_list.append(metrics_df)

    if metrics_df_list:
        final_df = pd.concat(metrics_df_list)
        # Use dynamic filename to distinguish runs without changing internal schema
        output_file = data_path / "intermediate_data" / f"knn_probing_metrics_{ckpt_type}.tsv"
        final_df.to_csv(output_file, sep="\t", index=False)
        logger.info(f"Results saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_jobs", type=int, default=-1)
    parser.add_argument("--endpoint", type=str, required=True)
    parser.add_argument("--ckpt-type", type=str, choices=["best", "last"], default="best")
    args = parser.parse_args()
    main(args.n_jobs, args.endpoint, args.ckpt_type)