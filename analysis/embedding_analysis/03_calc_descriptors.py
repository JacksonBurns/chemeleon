"""Calculate molecular descriptors for molecule datasets."""

import argparse
import copy
from functools import partial
from pathlib import Path
from typing import Any, Self

import numpy as np
import pandas as pd
import numpy.typing as npt
from loguru import logger
from molpipeline import Pipeline
from molpipeline.abstract_pipeline_elements.core import InvalidInstance
from molpipeline.abstract_pipeline_elements.mol2any import (
    MolToDescriptorPipelineElement,
)
from molpipeline.any2mol import SmilesToMol
from molpipeline.mol2any import MolToMorganFP, MolToRDKitPhysChem
from molpipeline.utils.molpipeline_types import AnyTransformer, RDKitMol
from mordred import Calculator, descriptors
from sklearn.preprocessing import StandardScaler

from common import parse_endpoint_input


def get_morgan_pipeline(counted: bool, n_jobs: int = 1) -> Pipeline:
    """Get the Morgan fingerprint pipeline.

    Parameters
    ----------
    counted: bool
        Whether to use counted (True) or binary (False) Morgan fingerprints.
    n_jobs: int, optional
        The number of jobs to use for descriptor calculation.
        In case of -1, all available CPUs are used.

    Returns
    -------
    Pipeline
        The Morgan fingerprint pipeline.
    """
    return Pipeline(
        [
            ("auto2mol", SmilesToMol()),
            (
                "morganFP",
                MolToMorganFP(
                    n_bits=2048, radius=2, counted=counted, return_as="dense"
                ),
            ),
        ],
        n_jobs=n_jobs,
    )


def get_rdkit_physchem_pipeline(n_jobs: int = 1) -> Pipeline:
    """Get the RDKit PhysChem descriptor pipeline.

    Parameters
    ----------
    n_jobs: int, optional
        The number of jobs to use for descriptor calculation.
        In case of -1, all available CPUs are used.

    Returns
    -------
    Pipeline
        The RDKit PhysChem descriptor pipeline.
    """
    return Pipeline(
        [
            ("auto2mol", SmilesToMol()),
            (
                "rdkitPhysChem",
                MolToRDKitPhysChem(
                    standardizer=None,  # we avoid standardization at this point
                    return_with_errors=True,
                ),
            ),
        ],
        n_jobs=n_jobs,
    )


MORDRED_DESCRIPTOR_DICT = {
    str(desc): desc for desc in Calculator(descriptors, ignore_3D=True).descriptors
}
MORDRED_DESCRIPTORS = list(MORDRED_DESCRIPTOR_DICT.keys())
DEFAULT_DESCRIPTORS = MORDRED_DESCRIPTORS


class MolToMordred(MolToDescriptorPipelineElement):
    """Pipeline element to calculate Mordred descriptors."""

    _descriptor_list: list[str]

    def __init__(
        self,
        descriptor_list: list[str] | None = None,
        return_with_errors: bool = False,
        standardizer: AnyTransformer | None = StandardScaler(),
        log_exceptions: bool = True,
        name: str = "MolToMordred",
        n_jobs: int = 1,
        uuid: str | None = None,
    ) -> None:
        """Initialize the MolToMordred pipeline element.

        Parameters
        ----------
        descriptor_list: list[str] | None
            List of descriptor names to calculate. If None, DEFAULT_DESCRIPTORS are used.
        return_with_errors: bool
            If True, return descriptor vectors even if some descriptors failed to calculate.
            Failed descriptors will be set to NaN.
        standardizer: AnyTransformer | None
            Standardizer to apply to the descriptor vectors. If None, no standardization is applied.
        log_exceptions: bool
            If True, log exceptions that occur during descriptor calculation.
        name: str
            Name of the pipeline element.
        n_jobs: int
            Number of jobs to use for descriptor calculation.
        uuid: str | None
            UUID of the pipeline element.
        """
        self.descriptor_list = descriptor_list  # type: ignore
        self._feature_names = self._descriptor_list
        self._return_with_errors = return_with_errors
        self._log_exceptions = log_exceptions
        super().__init__(
            standardizer=standardizer,
            name=name,
            n_jobs=n_jobs,
            uuid=uuid,
        )

    @property
    def n_features(self) -> int:
        """Return the number of features."""
        return len(self._descriptor_list)

    @property
    def descriptor_list(self) -> list[str]:
        """Return a copy of the descriptor list. Alias of `feature_names`."""
        return self._descriptor_list[:]

    @descriptor_list.setter
    def descriptor_list(self, descriptor_list: list[str] | None) -> None:
        """Set the descriptor list.

        Parameters
        ----------
        descriptor_list: list[str] | None
            List of descriptor names to calculate. If None, DEFAULT_DESCRIPTORS are used.

        Raises
        ------
        ValueError
            If an unknown descriptor name is used.
        ValueError
            If an empty descriptor_list is used.
        """
        if descriptor_list is None or descriptor_list is DEFAULT_DESCRIPTORS:
            # if None or DEFAULT_DESCRIPTORS are used, set the default descriptors
            self._descriptor_list = DEFAULT_DESCRIPTORS
        elif len(descriptor_list) == 0:
            raise ValueError(
                "Empty descriptor_list is not allowed. Use None for default descriptors."
            )
        else:
            # check all user defined descriptors are valid
            for descriptor_name in descriptor_list:
                if descriptor_name not in MORDRED_DESCRIPTORS:
                    raise ValueError(
                        f"Unknown descriptor function with name: {descriptor_name}"
                    )
            self._descriptor_list = descriptor_list

    def pretransform_single(
        self, value: RDKitMol
    ) -> npt.NDArray[np.float64] | InvalidInstance:
        """Transform a single molecule to a descriptor vector.

        Parameters
        ----------
        value: RDKitMol
            RDKit molecule to transform.

        Returns
        -------
        npt.NDArray[np.float64] | InvalidInstance
            Descriptor vector for given molecule.
            Failure is indicated by an InvalidInstance.
        """
        vec = np.full((len(self._descriptor_list),), np.nan)
        for i, name in enumerate(self._descriptor_list):
            descriptor_func = MORDRED_DESCRIPTOR_DICT[name]
            try:
                vec[i] = descriptor_func(value)
            except Exception:  # pylint: disable=broad-except
                if self._log_exceptions:
                    # loguru logger can't be pickled. Use simple print.
                    print(f"Failed calculating descriptor: {name}")
        if not self._return_with_errors and np.any(np.isnan(vec)):
            return InvalidInstance(self.uuid, "NaN in descriptor vector", self.name)
        return vec

    def get_params(self, deep: bool = True) -> dict[str, Any]:
        """Get the parameters of the pipeline element.

        Parameters
        ----------
        deep: bool
            If true create a deep copy of the parameters

        Returns
        -------
        dict[str, Any]
            Parameter of the pipeline element.
        """
        parent_dict = dict(super().get_params(deep=deep))
        if deep:
            parent_dict["descriptor_list"] = copy.deepcopy(self._descriptor_list)
            parent_dict["return_with_errors"] = copy.deepcopy(self._return_with_errors)
            parent_dict["log_exceptions"] = copy.deepcopy(self._log_exceptions)
        else:
            parent_dict["descriptor_list"] = self._descriptor_list
            parent_dict["return_with_errors"] = self._return_with_errors
            parent_dict["log_exceptions"] = self._log_exceptions
        return parent_dict

    def set_params(self, **parameters: Any) -> Self:
        """Set parameters.

        Parameters
        ----------
        parameters: Any
            Parameters to set

        Returns
        -------
        Self
            Self
        """
        parameters_shallow_copy = dict(parameters)
        params_list = ["descriptor_list", "return_with_errors", "log_exceptions"]
        for param_name in params_list:
            if param_name in parameters:
                setattr(self, f"_{param_name}", parameters[param_name])
                parameters_shallow_copy.pop(param_name)
        super().set_params(**parameters_shallow_copy)
        return self


def get_mordred_pipeline(n_jobs: int = 1) -> Pipeline:
    """Get the Mordred descriptor pipeline.

    Parameters
    ----------
    n_jobs: int, optional
        The number of jobs to use for descriptor calculation.
        In case of -1, all available CPUs are used.

    Returns
    -------
    Pipeline
        The Mordred descriptor pipeline.
    """
    return Pipeline(
        [
            ("auto2mol", SmilesToMol()),
            (
                "mordred",
                MolToMordred(
                    standardizer=None,  # we avoid standardization at this point
                    return_with_errors=True,
                ),
            ),
        ],
        n_jobs=n_jobs,
    )


def parse_args() -> argparse.Namespace:
    """Parse command line arguments.

    Returns
    -------
    argparse.Namespace
        Parsed command line arguments.
    """
    argument_parser = argparse.ArgumentParser(
        description="Calculate molecular descriptors for molecule datasets."
    )
    argument_parser.add_argument(
        "--n_jobs",
        type=int,
        default=16,
        help="Number of jobs to use for processing.",
    )
    argument_parser.add_argument(
        "--endpoint",
        type=str,
        required=True,
        help="Endpoint to calculate descriptors for (can be a single endpoint or a path to a YAML config file).",
    )
    argument_parser.add_argument(
        "--descriptor",
        type=str,
        choices=["morgan", "morgan_count", "rdkit_physchem", "mordred"],
        help="Type of descriptor to calculate.",
        required=True,
    )
    args = argument_parser.parse_args()
    return args


def main(n_jobs: int, endpoint: str, descriptor_type: str) -> None:
    """Calculate molecular descriptors for datasets.

    Parameters
    ----------
    n_jobs : int
        Number of jobs to use for processing.
    endpoint : str
        Endpoint to calculate descriptors for.
    descriptor_type : str
        Type of descriptor to calculate.
    """
    # Set up path variables
    base_path = Path(__file__).parents[0]
    data_path = base_path / "data"

    Path(base_path / "logs").mkdir(exist_ok=True)
    logger.add(base_path / "logs" / f"{Path(__file__).stem}.log")

    endpoint_list = parse_endpoint_input(endpoint)
    logger.info(f"Processing {len(endpoint_list)} endpoint(s).")

    if descriptor_type == "morgan":
        pipeline_func = partial(get_morgan_pipeline, counted=False)
    elif descriptor_type == "morgan_count":
        pipeline_func = partial(get_morgan_pipeline, counted=True)
    elif descriptor_type == "rdkit_physchem":
        pipeline_func = get_rdkit_physchem_pipeline
    elif descriptor_type == "mordred":
        pipeline_func = get_mordred_pipeline
    else:
        raise ValueError(f"Unknown descriptor_type: {descriptor_type}")

    for ep in endpoint_list:
        logger.info(f"Processing endpoint: {ep}")

        # Load data
        endpoint_df = pd.read_csv(
            data_path
            / "intermediate_data"
            / "presplit_data"
            / f"presplit_data_{ep}.tsv",
            sep="\t",
        )
        logger.info(f"Loaded data with {endpoint_df.shape[0]} rows.")

        smiles_list = endpoint_df["smiles"].tolist()

        logger.info(f"Calculating {descriptor_type} descriptors for {ep}...")

        pipeline = pipeline_func(n_jobs=n_jobs)
        descriptors = pipeline.fit_transform(smiles_list)

        # Convert to numpy array if not already
        if not isinstance(descriptors, np.ndarray):
            descriptors = np.array(descriptors)

        logger.info(f"Calculated descriptors with shape: {descriptors.shape}")

        # Create output directory
        output_dir = data_path / "intermediate_data" / "descriptors" / descriptor_type
        output_dir.mkdir(parents=True, exist_ok=True)

        # Save descriptors
        output_path = output_dir / f"{ep}_{descriptor_type}.npy"
        np.save(output_path, descriptors)
        logger.info(f"Saved {descriptor_type} descriptors to {output_path}")


if __name__ == "__main__":
    args = parse_args()
    main(args.n_jobs, args.endpoint, args.descriptor)
