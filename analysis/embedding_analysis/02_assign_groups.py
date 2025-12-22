"""Assign groups to the Tox21 dataset for cross-validation.

Taken from:
 https://github.com/basf/neural-fingerprint-uncertainty/blob/69c4dde201d43c7d5242805e3fcb47af54d0b101/scripts/02_assign_groups.py#L1


MIT License

Copyright (c) 2024 BASF

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# pylint: disable=invalid-name
# pylint: enable=invalid-name

import argparse
from pathlib import Path  # pathmodifications

import numpy as np
import numpy.typing as npt
import pandas as pd
from common import parse_endpoint_input
from molpipeline import Pipeline
from molpipeline.any2mol import SmilesToMol
from molpipeline.error_handling import ErrorFilter, FilterReinserter
from molpipeline.kernel.tanimoto_functions import self_tanimoto_distance
from molpipeline.mol2any import MolToMorganFP, MolToSmiles
from molpipeline.mol2mol import MakeScaffoldGeneric, MurckoScaffold
from sklearn.base import clone
from sklearn.cluster import AgglomerativeClustering
from sklearn.model_selection import StratifiedGroupKFold, StratifiedKFold
from sklearn.preprocessing import FunctionTransformer, OrdinalEncoder


def get_clustering_pipeline(n_jobs: int = 1) -> Pipeline:
    """Get the clustering pipeline.

    Returns
    -------
    Pipeline
        The clustering pipeline.
    """
    clustering_pipeline = Pipeline(
        [
            ("smi2mol", SmilesToMol()),
            ("mol2morgan", MolToMorganFP(return_as="dense")),
            (
                "agg_clustering",
                AgglomerativeClustering(
                    distance_threshold=0.8,
                    linkage="average",
                    metric=self_tanimoto_distance,
                    n_clusters=None,
                ),
            ),
        ],
        n_jobs=n_jobs,
    )
    return clustering_pipeline


def get_scaffold_pipeline(n_jobs: int = 1) -> Pipeline:
    """Get the scaffold pipeline.

    Returns
    -------
    Pipeline
        The scaffold pipeline.
    """
    murcko_scaffold = MurckoScaffold()
    none_filter = ErrorFilter.from_element_list([murcko_scaffold])
    none_filler = FilterReinserter.from_error_filter(none_filter, "")
    scaffold_pipeline = Pipeline(
        [
            ("smi2mol", SmilesToMol()),
            ("murcko_scaffold", murcko_scaffold),
            ("mol2smi", MolToSmiles()),
            ("none_filter", none_filter),
            ("none_filler", none_filler),
            ("reshape2d", FunctionTransformer(func=np.atleast_2d)),
            ("transpose", FunctionTransformer(func=np.transpose)),
            ("scaffold_encoder", OrdinalEncoder()),
            ("reshape1d", FunctionTransformer(func=np.ravel)),
        ],
        n_jobs=n_jobs,
    )
    return scaffold_pipeline


def get_generic_scaffold_pipeline(n_jobs: int = 1) -> Pipeline:
    """Get the generic scaffold pipeline.

    Returns
    -------
    Pipeline
        The generic scaffold pipeline.
    """
    murcko_scaffold2 = MurckoScaffold()
    none_filter2 = ErrorFilter.from_element_list([murcko_scaffold2])
    none_filler2 = FilterReinserter.from_error_filter(none_filter2, "")
    generic_scaffold_pipeline = Pipeline(
        [
            ("smi2mol", SmilesToMol()),
            ("murcko_scaffold", murcko_scaffold2),
            ("generic_scaffold", MakeScaffoldGeneric()),
            ("mol2smi", MolToSmiles()),
            ("none_filter", none_filter2),
            ("none_filler", none_filler2),
            ("reshape2d", FunctionTransformer(func=np.atleast_2d)),
            ("transpose", FunctionTransformer(func=np.transpose)),
            ("scaffold_encoder", OrdinalEncoder()),
            ("reshape1d", FunctionTransformer(func=np.ravel)),
        ],
        n_jobs=n_jobs,
    )
    return generic_scaffold_pipeline


def get_stratified_k_fold_splits(
    data_df: pd.DataFrame, n_splits: int
) -> npt.NDArray[np.int_]:
    """Split the data randomly and stratified.

    Parameters
    ----------
    data_df : pd.DataFrame
        The data to split.
    n_splits : int
        The number of splits.

    Returns
    -------
    npt.NDArray[np.int_]
        The group array.
    """
    skf = StratifiedKFold(n_splits, shuffle=True, random_state=20240320)
    group_array = -np.ones_like(data_df.label.to_numpy())
    for split, (_, test_idx) in enumerate(
        skf.split(data_df.smiles.tolist(), data_df.label.to_numpy())
    ):
        group_array[test_idx] = split
    return group_array


def get_pipeline_splits(
    data_df: pd.DataFrame, n_splits: int, pipeline: Pipeline
) -> npt.NDArray[np.int_]:
    """Split the data using a pipeline.

    Parameters
    ----------
    data_df : pd.DataFrame
        The data to split.
    n_splits : int
        The number of splits.
    pipeline : Pipeline
        The pipeline to use for splitting.

    Returns
    -------
    npt.NDArray[np.int_]
        The group array.
    """
    # Step 1: Clone the pipeline to avoid side effects
    pipeline_copy = clone(pipeline)

    # Step 2: Fit the pipeline to the data
    if hasattr(pipeline_copy, "fit_predict"):
        cluster_label = pipeline_copy.fit_predict(
            data_df.smiles.tolist(), data_df.label.to_numpy()
        )
    else:
        cluster_label = pipeline_copy.fit_transform(
            data_df.smiles.tolist(), data_df.label.to_numpy()
        )

    # Step 3: Split the data using the cluster labels
    sgkf = StratifiedGroupKFold(n_splits, random_state=20240320, shuffle=True)
    group_array = -np.ones_like(data_df.label.to_numpy())
    for split, (_, test_idx) in enumerate(
        sgkf.split(
            data_df.smiles.tolist(),
            data_df.label.to_numpy(),
            groups=cluster_label,
        )
    ):
        group_array[test_idx] = split
    return group_array


def parse_args() -> argparse.Namespace:
    """Parse command line arguments.

    Returns
    -------
    argparse.Namespace
        Parsed command line arguments.
    """
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--n_jobs",
        type=int,
        default=1,
        help="Number of jobs to use for training.",
    )
    argument_parser.add_argument(
        "--n_groups",
        type=int,
        default=5,
    )
    argument_parser.add_argument(
        "--endpoint",
        type=str,
        help="Endpoint to train on.",
        required=True,
    )
    args = argument_parser.parse_args()
    return args


def main() -> None:
    """Assign groups to the Tox21 dataset for cross-validation."""
    # Set up paths
    base_path = Path(__file__).parents[0]
    data_path = base_path / "data"
    save_path = base_path / "data" / "intermediate_data" / "presplit_data"
    save_path.mkdir(parents=True, exist_ok=True)

    # Get arguments
    args = parse_args()

    #  Create the clustering pipelines
    clustering_pipeline = get_clustering_pipeline(args.n_jobs)
    scaffold_pipeline = get_scaffold_pipeline(args.n_jobs)
    generic_scaffold_pipeline = get_generic_scaffold_pipeline(args.n_jobs)
    cluster_dict = {
        "Agglomerative clustering": clustering_pipeline,
        "Murcko scaffold": scaffold_pipeline,
        "Generic scaffold": generic_scaffold_pipeline,
    }

    data_df = pd.read_csv(
        data_path / "intermediate_data" / "ml_ready_data.tsv", sep="\t"
    )

    endpoint_list = parse_endpoint_input(args.endpoint)
    for endpoint in endpoint_list:
        endpoint_df = data_df.loc[data_df.endpoint == endpoint].copy()
        endpoint_df["Random"] = get_stratified_k_fold_splits(endpoint_df, args.n_groups)
        for grouping_name, grouping_pipeline in cluster_dict.items():
            endpoint_df[grouping_name] = get_pipeline_splits(
                endpoint_df, args.n_groups, grouping_pipeline
            )
        endpoint_df.to_csv(
            save_path / f"presplit_data_{endpoint}.tsv", sep="\t", index=False
        )


if __name__ == "__main__":
    main()
