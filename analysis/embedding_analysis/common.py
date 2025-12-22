"""Common utilities for embedding analysis."""

import dataclasses
from pathlib import Path

import yaml


@dataclasses.dataclass(frozen=True)
class RepresentationInfo:
    """Info for a representation."""

    # name of the representation, e.g. morgan
    representation_type: str

    # whether features should be scaled
    need_standardization: bool

    # preferred distance measure, e.g. "jaccard"
    distance_measure: str


REPRESENTATION_INFOS = {
    "morgan": RepresentationInfo(
        representation_type="morgan",
        need_standardization=False,
        distance_measure="jaccard",
    ),
    "morgan_count": RepresentationInfo(
        representation_type="morgan_count",
        need_standardization=False,
        distance_measure="euclidean",
    ),
    "rdkit_physchem": RepresentationInfo(
        representation_type="rdkit_physchem",
        need_standardization=True,
        distance_measure="euclidean",
    ),
    "mordred": RepresentationInfo(
        representation_type="mordred",
        need_standardization=True,
        distance_measure="euclidean",
    ),
    "chemeleon_finetuned": RepresentationInfo(
        representation_type="chemeleon_finetuned",
        need_standardization=False,
        distance_measure="euclidean",
    ),
    "chemeleon_frozen": RepresentationInfo(
        representation_type="chemeleon_frozen",
        need_standardization=False,
        distance_measure="euclidean",
    ),
    "chemprop": RepresentationInfo(
        representation_type="chemprop",
        need_standardization=False,
        distance_measure="euclidean",
    ),
    "chemeleon_no_pretraining": RepresentationInfo(
        representation_type="chemeleon_no_pretraining",
        need_standardization=False,
        distance_measure="euclidean",
    ),
}


def parse_endpoint_input(endpoint_str: str) -> list[str]:
    """Parse the endpoint input string to list of endpoints.

    Parameters
    ----------
    endpoint_str : str
        The endpoint input string. Can be a single endpoint or a path to a YAML file
        containing a list of endpoints.

    Returns
    -------
    list[str]
        The parsed endpoints.
    """
    # check if endpoint is file path
    path = Path(endpoint_str)
    if path.is_file() and path.suffix in [".yml", ".yaml"]:
        with open(path, "r") as file:
            config = yaml.safe_load(file)
        endpoint = config.get("endpoint", None)
        if endpoint is None:
            raise ValueError(f"Endpoint not found in config file: {endpoint_str}")
        return endpoint
    return [endpoint_str]
