from pathlib import Path
from typing import Literal
import numpy as np
import torch
from chemprop import featurizers, nn
from chemprop.models import MPNN
from chemprop.nn import RegressionFFN


class Encoder(torch.nn.Module):
    def __init__(self, input_dim: int, latent_dims: list[int]):
        super().__init__()
        self.encoder_layers = torch.nn.ModuleList([
            torch.nn.Linear(input_dim if i == 0 else latent_dims[i - 1], latent_dims[i])
            for i in range(len(latent_dims))
        ])

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        h = x
        for i, layer in enumerate(self.encoder_layers):
            h = layer(h)
            if i < len(self.encoder_layers) - 1:
                h = torch.nn.functional.relu(h)
        return h


class CheMeleonEmbedder:
    def __init__(self, device: str | torch.device | None = None, type: Literal["full", "autoencoded"] = "full"):
        ckpt_dir = Path().home() / ".chemprop"
        mp_path = ckpt_dir / "chemeleon_mp.pt"
        self.featurizer = featurizers.CuikmolmakerMolGraphFeaturizer(atom_featurizer_mode="V2")
        agg = nn.MeanAggregation()
        chemeleon_mp = torch.load(mp_path, weights_only=True)
        mp = nn.BondMessagePassing(**chemeleon_mp["hyper_parameters"])
        mp.load_state_dict(chemeleon_mp["state_dict"])
        self.model = MPNN(
            message_passing=mp,
            agg=agg,
            predictor=RegressionFFN(input_dim=mp.output_dim),
        )
        self.model.eval()
        self.device = device
        if self.device is not None:
            self.model.to(device=self.device)

        self.encoder = torch.nn.Identity()
        if type == "autoencoded":
            ae_path = ckpt_dir / "chemeleon_ae.pt"
            ae = torch.load(ae_path, map_location=self.device)
            input_dim = ae["0.weight"].shape[1]
            latent_dims = [ae["0.weight"].shape[0]]
            for i in range(1, len(ae) // 2):
                latent_dims.append(ae[f"{i}.weight"].shape[0])
            self.encoder = Encoder(input_dim=input_dim, latent_dims=latent_dims)
            self.encoder.encoder_layers.load_state_dict(ae)
            self.encoder.to(device=self.device)
            self.encoder.eval()

    @torch.inference_mode()
    def __call__(self, smiles: list[str]) -> torch.Tensor:
        bmg = self.featurizer(smiles)
        bmg.to(self.device)
        return self.encoder(self.model.fingerprint(bmg))

if __name__ == "__main__":
    default_database = Path(__file__).parent.resolve() / "data"/ "cleaned_pubchem_1MM.smiles"

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--type", choices=["full", "autoencoded"], default="full")
    parser.add_argument("--batch-size", type=int, default=1_024)
    parser.add_argument("--smiles-database", type=str, default=default_database)
    parser.add_argument("--output-path", type=str, default=None)
    args = parser.parse_args()

    if args.output_path is None:
        outname = Path("data") / (default_database.stem + f"_embeddings_{args.type}")
    else:
        outname = args.output_path
    outname.mkdir(parents=True, exist_ok=True)

    get_chemeleon_embeddings = CheMeleonEmbedder(device="cuda", type=args.type)

    with open(args.smiles_database, "r") as file:
        smiles = np.array([line.strip() for line in file.readlines()])

    for i in range(0, len(smiles), args.batch_size):
        embeddings = get_chemeleon_embeddings(smiles=smiles[i : (i + args.batch_size if i + args.batch_size <= len(smiles) else len(smiles))]).to("cpu")
        torch.save(embeddings, outname / f"batch_{i // args.batch_size}.pt")
        torch.cuda.empty_cache()
