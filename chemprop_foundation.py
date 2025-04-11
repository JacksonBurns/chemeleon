from typing import Iterable

from lightning import pytorch as pl
import torch
from torch import distributed
import zarr

from rdkit.Chem import MolFromSmiles
from chemprop.nn import Aggregation, ChempropMetric, MessagePassing, Predictor
from fastprop.data import standard_scale
from chemprop.featurizers import SimpleMoleculeMolGraphFeaturizer
from chemprop.data import Datum
from chemprop.models import MPNN


class WinsorizeStdevN(torch.nn.Module):
    def __init__(self, n: float) -> None:
        super().__init__()
        self.n = n

    def forward(self, batch: torch.Tensor):
        return torch.clamp(batch, min=-self.n, max=self.n)

    def extra_repr(self) -> str:
        return f"n={self.n}"


# mock the default chemprop dataset class to load y's incrementally
class ChemPropZarrDataset(torch.utils.data.Dataset):
    def __init__(self, smiles: list[str], zarr_store: str):
        self.smiles = smiles
        self.len = len(smiles)
        self.z = zarr.open_array(zarr_store)
        self.molgraph_generator = SimpleMoleculeMolGraphFeaturizer()

    def __len__(self):
        return self.len
    
    def __getitem__(self, idx: int):
        mg = self.molgraph_generator(MolFromSmiles(self.smiles[idx]))
        return Datum(mg, None, None, self.z[idx, :], None, None, None)     


class MaskedDescriptorsMPNN(MPNN):
    def __init__(
        self,
        message_passing: MessagePassing,
        agg: Aggregation,
        predictor: Predictor,
        metrics: Iterable[ChempropMetric],
        masking_ratio: float,
        feature_means: torch.Tensor,
        feature_vars: torch.Tensor,
        winsorization_factor: int = 6,
    ):
        super().__init__(message_passing, agg, predictor, False, metrics)
        self.masking_ratio = masking_ratio
        self.register_buffer("feature_means", feature_means)
        self.register_buffer("feature_vars", feature_vars)
        self.winsorization = WinsorizeStdevN(winsorization_factor)

    def training_step(self, batch, batch_idx):
        # overrides parent method to ranomly mask (evaluate only masked descriptors) during training
        batch_size = self.get_batch_size(batch)
        bmg, V_d, X_d, targets, weights, lt_mask, gt_mask = batch
        targets = standard_scale(targets, self.feature_means, self.feature_vars)
        targets = self.winsorization(targets)
        mask = (torch.rand_like(targets) < self.masking_ratio).bool()
        Z = self.fingerprint(bmg, V_d, X_d)
        preds = self.predictor.train_step(Z)
        l = self.criterion(preds, targets, mask, weights, lt_mask, gt_mask)
        self.log("train/masked_loss", self.criterion, batch_size=batch_size, prog_bar=True, on_epoch=True, sync_dist=distributed.is_initialized())
        return l


if __name__ == "__main__":
    from chemprop.nn import MeanAggregation, BondMessagePassing
    
    zarr_store = "/datag/pubchem_1MM.zarr"
    
    # get the smiles corresponding to the rows of this zarr arr...
    # /home/jwburns/fastprop_foundation/pubchem_1MM.smiles
    # but apply the filtering steps used in the features.py script
    
    dataset = ChemPropZarrDataset(
        None,
        zarr_store,
    )

    mdm = MaskedDescriptorsMPNN(
        BondMessagePassing(),
        MeanAggregation(),
        predictor=None,
        metrics=[],
        masking_ratio=0.15,
        feature_means=None,
        feature_vars=None,
        winsorization_factor=6,
    )
    
    # lightning training code from other script
    ...
    train_dataset, val_dataset, test_dataset = None, None, None
