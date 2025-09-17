
from typing import Iterable

import numpy as np
from rdkit import Chem
from sklearn.base import BaseEstimator, TransformerMixin

from .mmf import morgan_mined_fingerprint

class MolFingerprintTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X: Iterable[Chem.Mol], y=None):
        return self

    def transform(self, X: Iterable[Chem.Mol]) -> np.ndarray:
        fps = []
        for mol in X:
            # mol is an array of one element, the Mol
            fps.append(morgan_mined_fingerprint(mol[0]))
        return np.vstack(fps)