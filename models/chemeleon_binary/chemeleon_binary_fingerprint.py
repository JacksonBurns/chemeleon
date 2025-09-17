# chemeleon_binary_fingerprint.py
# 
# this is adapted from chemeleon_fingerprint.py to use the binary version of CheMeleon (CheMeleon-Binary)
from pathlib import Path

import torch
from chemprop import featurizers, nn
from chemprop.featurizers.atom import RIGRAtomFeaturizer
from chemprop.featurizers.bond import RIGRBondFeaturizer
from chemprop.data import BatchMolGraph
from chemprop.nn import RegressionFFN
from chemprop.models import MPNN
from rdkit.Chem import MolFromSmiles, Mol
import numpy as np

from sigmoid_step import SigmoidStep


class CheMeleonBinaryFingerprint:
    def __init__(self, device: str | torch.device | None = None):
        rigr_atom_featurizer = RIGRAtomFeaturizer()
        rigr_bond_featurizer = RIGRBondFeaturizer()
        self.featurizer = featurizers.SimpleMoleculeMolGraphFeaturizer(atom_featurizer=rigr_atom_featurizer, bond_featurizer=rigr_bond_featurizer)
        agg = nn.NormAggregation()

        mp_path = Path("chemeleon-binary_mp.pt")
        if not mp_path.exists():
            exit(1)
        chemeleon_mp = torch.load(mp_path, weights_only=True)
        mp = nn.BondMessagePassing(**chemeleon_mp['hyper_parameters'])
        mp.load_state_dict(chemeleon_mp['state_dict'])
        self.model = MPNN(
            message_passing=mp,
            agg=agg,
            predictor=RegressionFFN(input_dim=mp.output_dim),  # not actually used
        )
        self.model.bn = SigmoidStep()
        self.model.eval()
        assert self.model.bn.training == False
        if device is not None:
            self.model.to(device=device)

    def __call__(self, molecules: list[str | Mol]) -> np.ndarray:
        bmg = BatchMolGraph([self.featurizer(MolFromSmiles(m) if isinstance(m, str) else m) for m in molecules])
        bmg.to(device=self.model.device)
        with torch.no_grad():
            return self.model.fingerprint(bmg).numpy(force=True)


if __name__ == "__main__":
    chemeleon_fingerprint = CheMeleonBinaryFingerprint()
    chemeleon_fingerprint(["C", "CC", MolFromSmiles("CCC")])
