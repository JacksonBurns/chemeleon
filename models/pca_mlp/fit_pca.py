"""
fit_pca.py

Fits a PCA model on the pretraining data and saves it for later use.
This allows for consistent dimensionality reduction across different benchmarks.
"""

import sys
import argparse
from pathlib import Path
import torch
import numpy as np
import zarr
from tqdm import tqdm
from sklearn.decomposition import PCA
from torch.utils.data import DataLoader as TorchDataLoader
from torch.utils.data import Dataset as TorchDataset
from fastprop.data import standard_scale


class ZarrDataset(TorchDataset):
    def __init__(self, zarr_path: str):
        self.z = zarr.open_array(zarr_path)
        self.len = self.z.shape[0]

    def __len__(self):
        return self.len

    def __getitem__(self, batch_idx: list[int]):
        return torch.tensor(self.z[batch_idx], dtype=torch.float32)


def parse_args():
    parser = argparse.ArgumentParser(description="Fit a PCA model on pretraining data")
    parser.add_argument(
        "training_store", type=str, help="Path to zarr array with training data"
    )
    parser.add_argument(
        "output_path", type=str, help="Path to save the fitted PCA model"
    )
    parser.add_argument(
        "--explained-variance",
        type=float,
        default=0.95,
        help="Target explained variance ratio (0-1)",
    )
    parser.add_argument(
        "--batch-size", type=int, default=1024, help="Batch size for loading data"
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=None,
        help="Number of examples to use for fitting (default: all)",
    )
    parser.add_argument(
        "--random-seed", type=int, default=42, help="Random seed for reproducibility"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    training_store = Path(args.training_store)
    output_path = Path(args.output_path)

    # Create output directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Open zarr array to get shape information
    z = zarr.open_array(training_store, mode="r")
    n_features = z.shape[1]
    n_samples = z.shape[0]
    print(f"Dataset has {n_samples} samples with {n_features} features")

    # Load the features for standardization
    cached_means_fpath = f"feature_means_cached_{training_store.stem}.pt"
    cached_vars_fpath = f"feature_vars_cached_{training_store.stem}.pt"

    if not Path(cached_means_fpath).exists() or not Path(cached_vars_fpath).exists():
        print(
            "Error: Feature statistics not found. Run pretrain.py first to generate them."
        )
        sys.exit(1)

    try:
        feature_means = torch.load(
            cached_means_fpath, weights_only=True, map_location="cpu"
        )
        feature_vars = torch.load(
            cached_vars_fpath, weights_only=True, map_location="cpu"
        )
        print(f"Loaded feature statistics from cache files")
    except Exception as e:
        print(f"Error loading feature statistics: {e}")
        sys.exit(1)

    # Create dataset and dataloader
    dataset = ZarrDataset(training_store)

    # Sample if requested
    if args.sample_size and args.sample_size < len(dataset):
        print(f"Sampling {args.sample_size} examples from dataset")
        np.random.seed(args.random_seed)
        indices = np.random.choice(len(dataset), size=args.sample_size, replace=False)
        sampler = torch.utils.data.SubsetRandomSampler(indices)
        dataloader = TorchDataLoader(
            dataset, batch_size=args.batch_size, sampler=sampler
        )
    else:
        print(f"Using all {len(dataset)} examples from dataset")
        dataloader = TorchDataLoader(dataset, batch_size=args.batch_size, shuffle=False)

    # Collect standardized data for PCA
    print("Loading and standardizing data for PCA fitting...")
    all_data = []
    for batch in tqdm(dataloader):
        # Standardize the batch using precomputed statistics
        # standard_scale will handle NaN values automatically
        batch_std = standard_scale(batch, feature_means, feature_vars).clamp(
            min=-6, max=6
        )
        all_data.append(batch_std.cpu().numpy())

    # Concatenate all batches
    X = np.concatenate(all_data, axis=0)
    print(f"Collected {X.shape[0]} samples for PCA fitting")

    # Apply PCA
    try:
        print(
            f"Fitting PCA with target explained variance of {args.explained_variance}"
        )
        pca = PCA(
            n_components=args.explained_variance,
            svd_solver="full",
            random_state=args.random_seed,
        )
        pca.fit(X)

        # Get results
        n_components = pca.n_components_
        explained_variance = pca.explained_variance_ratio_.sum()
        print(f"PCA fit complete:")
        print(f"- Original dimensions: {n_features}")
        print(f"- Reduced dimensions: {n_components}")
        print(
            f"- Dimension reduction: {n_features - n_components} ({(1 - n_components/n_features)*100:.1f}%)"
        )
        print(f"- Total variance explained: {explained_variance*100:.2f}%")

        # Save the model
        torch.save(pca, output_path)
        print(f"PCA model saved to {output_path}")

        # Example of how to use this with evaluate.py
        print("\nTo use this PCA model with evaluate.py, run:")
        print(
            f"python evaluate.py OUTPUT_DIR --pca-method pretrained --pca-model-path {output_path} --gpu"
        )

    except Exception as e:
        print(f"Error during PCA fitting: {e}")
        print("PCA model could not be created.")
        sys.exit(1)
