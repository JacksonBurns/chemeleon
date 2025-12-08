"""Load and prepare toxcast data provided by molecule net.

Taken from
 https://github.com/basf/neural-fingerprint-uncertainty/blob/69c4dde201d43c7d5242805e3fcb47af54d0b101/scripts/01_preprocess_data.py#L1


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

import argparse
from pathlib import Path

import pandas as pd
from loguru import logger
from molpipeline.any2mol import SmilesToMol
from molpipeline.error_handling import ErrorFilter, FilterReinserter
from molpipeline.mol2any import MolToSmiles
from molpipeline.mol2mol import (
    EmptyMoleculeFilter,
    FragmentDeduplicator,
    MetalDisconnector,
    MixtureFilter,
    SaltRemover,
    StereoRemover,
    TautomerCanonicalizer,
    Uncharger,
)
from molpipeline.mol2mol.filter import ElementFilter
from molpipeline.pipeline import Pipeline


def get_standardization_pipeline(n_jobs: int = 1) -> Pipeline:
    """Get the standardization pipeline.

    Parameters
    ----------
    n_jobs: int, optional
        The number of jobs to use for standardization.
        In case of -1, all available CPUs are used.

    Returns
    -------
    Pipeline
        The standardization pipeline.
    """
    element_filter = ElementFilter(
        allowed_element_numbers=[
            1,  # H
            3,  # Li
            5,  # B
            6,  # C
            7,  # N
            8,  # O
            9,  # F
            11,  # Na
            12,  # Mg
            14,  # Si
            15,  # P
            16,  # S
            17,  # Cl
            19,  # K
            20,  # Ca
            34,  # Se
            35,  # Br
            53,  # I
        ],
    )
    error_filter = ErrorFilter(filter_everything=True)
    # Set up pipeline
    standardization_pipeline = Pipeline(
        [
            ("smi2mol", SmilesToMol()),
            ("element_filter", element_filter),
            ("metal_disconnector", MetalDisconnector()),
            ("salt_remover", SaltRemover()),
            ("uncharge1", Uncharger()),
            ("canonical_tautomer", TautomerCanonicalizer()),
            ("uncharge2", Uncharger()),
            ("stereo_remover", StereoRemover()),
            ("fragment_deduplicator", FragmentDeduplicator()),
            ("mixture_remover", MixtureFilter()),
            ("empty_molecule_remover", EmptyMoleculeFilter()),
            ("mol2smi", MolToSmiles()),
            ("error_filter", error_filter),
            ("error_replacer", FilterReinserter.from_error_filter(error_filter, None)),
        ],
        n_jobs=n_jobs,
    )
    return standardization_pipeline


def main(n_jobs: int = 1) -> None:
    """Run the preprocessing procedure.

    Parameters
    ----------
    n_jobs: int, optional
        The number of jobs to use for standardization.
        In case of -1, all available CPUs are used.
    """
    # Set up path variables
    base_path = Path(__file__).parents[0]
    data_path = base_path / "data"

    Path(base_path / "logs").mkdir(exist_ok=True)
    logger.add(base_path / "logs" / f"{Path(__file__).stem}.log")

    # Set up pipeline
    standardization_pipeline = get_standardization_pipeline(n_jobs=n_jobs)

    # Load data
    data_df = pd.read_csv(data_path / "imported_data" / "toxcast_data.csv.gz")
    nrer_df = pd.read_csv(
        data_path / "imported_data" / "nr-er.smi",
        sep="\t",
        header=None,
        names=["smiles", "id", "nr_er"],
        usecols=["smiles", "nr_er"],
    )
    data_df = data_df.merge(nrer_df, on="smiles", how="outer")
    logger.info(
        f"Loaded data with {data_df.shape[0]} rows and {data_df.shape[1]} columns."
    )
    data_df["standardized_smiles"] = standardization_pipeline.fit_transform(
        data_df["smiles"].tolist()
    )
    logger.warning(
        f"Standardization failed for {data_df.standardized_smiles.isna().sum()} SMILES."
    )
    logger.warning("Dropping rows with failed standardization.")
    data_df = data_df.dropna(subset=["standardized_smiles"])

    # Define endpoint list
    endpoint_list = data_df.columns.tolist()
    endpoint_list.remove("smiles")
    endpoint_list.remove("standardized_smiles")
    logger.info(f"Found {len(endpoint_list)} endpoints.")

    # Create sparse dataframe, each row is a (smiles, endpoint) pair with a binary label
    sparse_df = data_df.melt(
        id_vars="standardized_smiles",
        value_vars=endpoint_list,
        value_name="label",
        var_name="endpoint",
    )
    # Remove rows with missing labels
    sparse_df = sparse_df.query("label.notna()").copy()

    # Cast labels from float to int
    sparse_df["label"] = sparse_df["label"].astype(int)

    # Check each combination of endpoint and SMILES for conflicting labels
    prefinal_list = []
    for (endpoint, smiles), grp_df in sparse_df.groupby(
        ["endpoint", "standardized_smiles"]
    ):
        unique_label = grp_df.label.unique()
        # Only keep SMILES with a single label for a given endpoint
        if len(unique_label) == 1:
            prefinal_list.append(
                {"endpoint": endpoint, "smiles": smiles, "label": unique_label[0]}
            )
    final_df = pd.DataFrame(prefinal_list)

    output_path = data_path / "intermediate_data"
    output_path.mkdir(parents=True, exist_ok=True)
    final_df.to_csv(output_path / "ml_ready_data.tsv", sep="\t", index=False)
    summary_df = final_df.pivot_table(
        index="endpoint",
        columns="label",
        values="smiles",
        aggfunc="nunique",
        fill_value=0,
    )
    summary_df["total"] = summary_df.sum(axis=1)
    summary_df.sort_values("total", ascending=False, inplace=True)
    logger.info(f"\n{summary_df}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load and prepare toxcast data provided by molecule net."
    )
    parser.add_argument(
        "--n_jobs",
        type=int,
        default=1,
        help="Number of CPU cores to use for standardization. Use -1 for all available CPUs.",
    )
    args = parser.parse_args()
    main(n_jobs=args.n_jobs)
