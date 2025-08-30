# chemeleon_fingerprint.py
# 
# this file contains the class CheMeleonFingerprint which can be instantiated
# and called to generate the CheMeleon learned embeddings for a list of SMILES
# strings and/or RDKit Mols. you may wish to simply copy or download this file directly for use,
# or adapt the code for your own purposes. No other files are required for it
# to work, though you must `pip install 'chemprop>=2.2.0'` for this to run.
#
# run `python chemeleon_fingerprint.py` for a quick usage demo, otherwise you
# should `import` the CheMeleonFingerprint class into your other code and use
# it there (following the example at the bottom of this file) to generate
# your learned fingerprints
from pathlib import Path
from urllib.request import urlretrieve

import torch
from chemprop import featurizers, nn
from chemprop.data import BatchMolGraph
from chemprop.nn import RegressionFFN
from chemprop.models import MPNN
from rdkit.Chem import MolFromSmiles, Mol
import numpy as np


class CheMeleonFingerprint:
    def __init__(self, device: str | torch.device | None = None):
        self.featurizer = featurizers.SimpleMoleculeMolGraphFeaturizer()
        agg = nn.MeanAggregation()
        ckpt_dir = Path().home() / ".chemprop"
        ckpt_dir.mkdir(exist_ok=True)
        mp_path = ckpt_dir / "chemeleon_mp.pt"
        if not mp_path.exists():
            urlretrieve(
                r"https://zenodo.org/records/15460715/files/chemeleon_mp.pt",
                mp_path,
            )
        chemeleon_mp = torch.load(mp_path, weights_only=True)
        mp = nn.BondMessagePassing(**chemeleon_mp['hyper_parameters'])
        mp.load_state_dict(chemeleon_mp['state_dict'])
        self.model = MPNN(
            message_passing=mp,
            agg=agg,
            predictor=RegressionFFN(input_dim=mp.output_dim),  # not actually used
        )
        self.model.eval()
        if device is not None:
            self.model.to(device=device)

    def __call__(self, molecules: list[str | Mol]) -> np.ndarray:
        bmg = BatchMolGraph([self.featurizer(MolFromSmiles(m) if isinstance(m, str) else m) for m in molecules])
        bmg.to(device=self.model.device)
        with torch.no_grad():
            return self.model.fingerprint(bmg).numpy(force=True)


if __name__ == "__main__":
    chemeleon_fingerprint = CheMeleonFingerprint()
    chemeleon_fingerprint(["C", "CC", MolFromSmiles("CCC")])
