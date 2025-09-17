#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Fingerprint Explorer – adapted to your CheMeleon‑Binary implementation
======================================================================

* Loads a representative set of molecules
* Generates the 2048‑bit binary fingerprint with `CheMeleonBinaryFingerprint`
* Computes a handful of useful statistics
* Produces a quick visual “fingerprint‑at‑a‑glance”

Dependencies
-------------
  pip install rdkit-pypi torch chemprop numpy pandas seaborn matplotlib \
             scikit-learn umap-learn tqdm

Author   : <your name>
Date     : 2025‑08‑30
"""

# ------------------------------------------------------------------
#  Imports
# ------------------------------------------------------------------
import os, sys, warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
from tqdm import tqdm

import matplotlib.pyplot as plt
import seaborn as sns

import torch
from rdkit import Chem
from rdkit.Chem import Descriptors, MolFromSmiles

# ------------------------------------------------------------------
#  1.  CheMeleon‑Binary Fingerprint class
# ------------------------------------------------------------------
#  The code you supplied had indentation/typo issues – they’re fixed below.
#  It works out‑of‑the‑box on CPU; you can pass a GPU device if you want.

class CheMeleonBinaryFingerprint:
    """
    Wrapper around the pre‑trained CheMeleon‑Binary message‑passing network.
    The model returns a 2048‑dimensional *continuous* vector that we binarise
    later (threshold 0.5).  The network is frozen – it is only used for
    fingerprint extraction.
    """
    def __init__(self, device: str | None = None):
        # Import inside the constructor so the module is only loaded when needed
        from chemprop import featurizers, nn
        from chemprop.featurizers.atom import RIGRAtomFeaturizer
        from chemprop.featurizers.bond import RIGRBondFeaturizer
        from chemprop.data import BatchMolGraph
        from chemprop.nn import RegressionFFN
        from chemprop.models import MPNN
        from sigmoid_step import SigmoidStep  # you already provided this

        # Featuriser (atom + bond)
        rigr_atom_featurizer = RIGRAtomFeaturizer()
        rigr_bond_featurizer = RIGRBondFeaturizer()
        self.featurizer = featurizers.SimpleMoleculeMolGraphFeaturizer(
            atom_featurizer=rigr_atom_featurizer,
            bond_featurizer=rigr_bond_featurizer
        )

        # Normalised message‑passing network
        agg = nn.NormAggregation()
        mp_path = os.path.join(os.path.dirname(__file__), "chemeleon-binary_mp.pt")
        if not os.path.exists(mp_path):
            raise FileNotFoundError(
                f"CheMeleon‑Binary model weights not found at {mp_path}\n"
                "Download the .pt file and place it in the same directory as this script."
            )
        mp_hyper = torch.load(mp_path, weights_only=True)
        mp = nn.BondMessagePassing(**mp_hyper["hyper_parameters"])
        mp.load_state_dict(mp_hyper["state_dict"])

        # MPNN wrapper – predictor is a dummy because we only care about the hidden state
        self.model = MPNN(
            message_passing=mp,
            agg=agg,
            predictor=RegressionFFN(input_dim=mp.output_dim)
        )
        self.model.bn = SigmoidStep()     # custom activation
        self.model.eval()
        # Disable gradients – we never train
        for p in self.model.parameters():
            p.requires_grad = False

        # Device handling
        self.device = torch.device(device or "cpu")
        self.model.to(self.device)

        # For convenience – the `BatchMolGraph` object needs to know the device
        self.BatchMolGraph = BatchMolGraph

    def __call__(self, molecules: list[str | Chem.Mol]) -> np.ndarray:
        """
        Parameters
        ----------
        molecules : list of SMILES strings or RDKit Mol objects

        Returns
        -------
        fingerprints : numpy.ndarray of shape (N, 2048)
            Continuous values in (0, 1); to use as a binary fingerprint,
            threshold at 0.5 afterwards.
        """
        from chemprop.featurizers import SimpleMoleculeMolGraphFeaturizer

        # Convert all inputs to Mol objects
        mols = [
            Chem.MolFromSmiles(m) if isinstance(m, str) else m
            for m in molecules
        ]

        # Build a batched graph
        bmg = self.BatchMolGraph([self.featurizer(m) for m in mols])
        bmg.to(device=self.device)

        # Forward pass – returns a torch.Tensor
        fp_torch = self.model.fingerprint(bmg)
        # Convert to NumPy array
        return fp_torch.cpu().numpy(force=True)

# ------------------------------------------------------------------
#  2.  Load a representative set of molecules
# ------------------------------------------------------------------
def load_demo_smiles(n=500, seed=42):
    """
    Simple helper that returns a DataFrame with 3 columns:
        * smiles – SMILES string
        * mol    – RDKit Mol object
        * logP   – RDKit descriptor (for colouring the embeddings)

    You can replace this with your own data source (CSV, SMILES file, …).
    """
    np.random.seed(seed)
    # We use the RDKit “ChEMBL20” SDF as a convenient public data set.
    # If you prefer a CSV/SMILES list, replace the block below.
    sdfs = Chem.SDMolSupplier("chembl_35.sdf")
    smiles = []
    for mol in sdfs:
        if mol is None: continue
        smiles.append(Chem.MolToSmiles(mol))
        if len(smiles) >= n:
            break

    df = pd.DataFrame({"smiles": smiles})
    df["mol"]   = df["smiles"].apply(Chem.MolFromSmiles)
    df["logP"]  = df["mol"].apply(Descriptors.MolLogP)
    return df

# ------------------------------------------------------------------
#  3.  Compute fingerprints and binarise
# ------------------------------------------------------------------
def compute_fingerprints(df, fp_cls: CheMeleonBinaryFingerprint):
    """
    Adds a column 'fp' to the DataFrame containing a 2048‑bit vector.
    """
    # Batch‑process all SMILES in one go – this is the fastest way
    fp_continuous = fp_cls(df["smiles"].tolist())
    # Binarise – threshold 0.5 (you can adjust if needed)
    fp_binary = (fp_continuous > 0.5).astype(int)
    df["fp"] = list(fp_binary)
    return df

# ------------------------------------------------------------------
#  4.  Statistics & visualisations
# ------------------------------------------------------------------
def bit_count_distribution(df):
    bit_counts = np.array([fp.sum() for fp in df["fp"]])
    plt.figure(figsize=(8,4))
    sns.histplot(bit_counts, bins=30, kde=False)
    plt.title("Distribution of set bits per fingerprint")
    plt.xlabel("Number of bits set")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

def bit_prevalence(df):
    mat = np.vstack(df["fp"].values)
    prevalence = mat.mean(axis=0)
    plt.figure(figsize=(12,4))
    sns.histplot(prevalence, bins=20, kde=False)
    plt.title("Bit prevalence (fraction of molecules with bit=1)")
    plt.xlabel("Prevalence")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()
    return prevalence

def fingerprint_heatmap(df, n_rows=10, n_cols=10):
    mat = np.vstack(df["fp"].values)
    plt.figure(figsize=(12,8))
    sns.heatmap(mat[:n_rows*n_cols,:], cmap="Greys", cbar=False,
                xticklabels=False, yticklabels=False)
    plt.title(f"Fingerprint matrix heatmap (first {n_rows*n_cols} molecules)")
    plt.tight_layout()
    plt.show()

def tanimoto_heatmap(df, max_pairs=2000):
    mat = np.vstack(df["fp"].values)
    if len(mat) > max_pairs:
        idx = np.random.choice(len(mat), max_pairs, replace=False)
    else:
        idx = np.arange(len(mat))
    sub = mat[idx]
    # Jaccard distance = 1 – tanimoto
    from sklearn.metrics import pairwise_distances
    dist = pairwise_distances(sub, metric="jaccard")
    sim = 1 - dist
    plt.figure(figsize=(8,6))
    sns.heatmap(sim, cmap="viridis", xticklabels=False, yticklabels=False)
    plt.title("Tanimoto similarity heatmap (sampled subset)")
    plt.tight_layout()
    plt.show()
    return sim, idx

def tsne_umap_projection(df, method="tsne", n_components=2, random_state=42):
    mat = np.vstack(df["fp"].values)
    from sklearn.manifold import TSNE
    method = "tsne"
    reducer = TSNE(n_components=n_components, perplexity=30,
                       random_state=random_state)
    embed = reducer.fit_transform(mat)
    plt.figure(figsize=(8,6))
    sns.scatterplot(x=embed[:,0], y=embed[:,1], s=30,
                    hue=df["logP"], palette="coolwarm", alpha=0.8, legend="brief")
    plt.title(f"{method.upper()} projection coloured by logP")
    plt.xlabel("Component 1")
    plt.ylabel("Component 2")
    plt.legend()
    plt.tight_layout()
    plt.show()

def bit_property_correlation(df, prop_name="logP"):
    mat = np.vstack(df["fp"].values)
    prop = df[prop_name].values
    corrs = np.array([np.corrcoef(mat[:,i], prop)[0,1] for i in range(mat.shape[1])])
    pos_idx = np.argsort(corrs)[-10:][::-1]
    neg_idx = np.argsort(corrs)[:10]
    plt.figure(figsize=(12,4))
    sns.barplot(x=pos_idx, y=corrs[pos_idx], palette="Reds")
    sns.barplot(x=neg_idx, y=corrs[neg_idx], palette="Blues")
    plt.title(f"Bits most positively/negatively correlated with {prop_name}")
    plt.xlabel("Bit index")
    plt.ylabel("Pearson correlation")
    plt.tight_layout()
    plt.show()
    return corrs

def cluster_heatmap(df, n_clusters=5):
    from sklearn.cluster import KMeans
    mat = np.vstack(df["fp"].values)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(mat)
    df["cluster"] = labels
    ordered = df.sort_values("cluster")
    ordered_mat = np.vstack(ordered["fp"].values)
    plt.figure(figsize=(12,8))
    sns.heatmap(ordered_mat, cmap="Greys", cbar=False,
                xticklabels=False, yticklabels=False)
    plt.title(f"Fingerprint heatmap ordered by k‑means cluster (k={n_clusters})")
    plt.tight_layout()
    plt.show()

# ------------------------------------------------------------------
#  5.  Main workflow
# ------------------------------------------------------------------
def main():
    # 1. Load a set of molecules
    df = load_demo_smiles(n=500)

    # 2. Create the CheMeleon‑Binary fingerprint extractor
    fp_extractor = CheMeleonBinaryFingerprint(device="cpu")

    # 3. Compute fingerprints
    df = compute_fingerprints(df, fp_extractor)

    # 4. Visualise & analyse
    bit_count_distribution(df)
    prevalence = bit_prevalence(df)
    fingerprint_heatmap(df, n_rows=10, n_cols=10)
    tanimoto_heatmap(df)
    tsne_umap_projection(df, method="tsne")
    tsne_umap_projection(df, method="umap")
    bit_property_correlation(df, prop_name="logP")
    cluster_heatmap(df, n_clusters=5)

if __name__ == "__main__":
    main()
