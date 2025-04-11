import math
from itertools import chain
from typing import Tuple

import torch
from fastprop.data import standard_scale
from lightning import LightningModule
from torch import distributed
from rtdl_num_embeddings import PeriodicEmbeddings

from utils.dyt import DynamicTanh


# code for the SNN has been adapted from the author's demo notebook on GitHub:
# https://github.com/bioinf-jku/SNNs/blob/master/Pytorch/SelfNormalizingNetworks_MLP_MNIST.ipynb


class WinsorizeStdevN(torch.nn.Module):
    def __init__(self, n: float) -> None:
        super().__init__()
        self.n = n

    def forward(self, batch: torch.Tensor):
        return torch.clamp(batch, min=-self.n, max=self.n)

    def extra_repr(self) -> str:
        return f"n={self.n}"


class fastpropFoundation(LightningModule):
    def __init__(
        self,
        feature_means: torch.Tensor,
        feature_vars: torch.Tensor,
        num_features: int = 1613,
        winsorization_factor=None,
        hidden_sizes: Tuple[int, ...] = (1024,),
        decoder_sizes: Tuple[int, ...] = (256,),
        encoding_size: int = 256,
        learning_rate: float = 0.001,
        masking_ratio: float = 0.15,
        embedding_dim: int = 8,
    ):
        super().__init__()
        self.register_buffer("feature_means", feature_means)
        self.register_buffer("feature_vars", feature_vars)
        self.learning_rate = learning_rate
        self.winsorize = False
        self.masking_ratio = masking_ratio
        if winsorization_factor is not None:
            self.winsorize = WinsorizeStdevN(winsorization_factor)
        modules = []
        # embeddings
        modules.append(PeriodicEmbeddings(num_features, d_embedding=embedding_dim, lite=False))
        modules.append(torch.nn.Flatten())
        # encoder
        modules.append(torch.nn.Linear(num_features * embedding_dim, hidden_sizes[0]))
        modules.append(torch.nn.LeakyReLU())
        for i in range(len(hidden_sizes)-1):
            modules.append(torch.nn.Linear(hidden_sizes[i], hidden_sizes[i+1]))
            modules.append(torch.nn.LeakyReLU())
        modules.append(torch.nn.Linear(hidden_sizes[-1], encoding_size))
        self.encoder = torch.nn.Sequential(*modules)
        # decoder
        modules = []
        if len(decoder_sizes) > 0:
            modules.append(torch.nn.Linear(encoding_size, decoder_sizes[0]))
            modules.append(torch.nn.LeakyReLU())
            for i in range(len(decoder_sizes)-1):
                modules.append(torch.nn.Linear(decoder_sizes[i], decoder_sizes[i+1]))
                modules.append(torch.nn.LeakyReLU())
            modules.append(torch.nn.Linear(decoder_sizes[-1], num_features))
        else:
            modules.append(torch.nn.Linear(encoding_size, num_features))
        self.decoder = torch.nn.Sequential(*modules)

        self.save_hyperparameters()
    
    def configure_optimizers(self):
        """See https://lightning.ai/docs/pytorch/stable/common/optimization.html

        Returns:
            dict: Optimizer name and instance.
        """
        return {"optimizer": torch.optim.AdamW(self.parameters(), lr=self.learning_rate)}

    def log(self, name, value, **kwargs):
        """Wrap the parent PyTorch Lightning log function to automatically detect DDP."""
        return super().log(name, value, sync_dist=distributed.is_initialized(), **kwargs)
    
    def _scale(self, x: torch.Tensor):
        x = standard_scale(x, self.feature_means, self.feature_vars)
        if not self.winsorize:
            return x
        else:
            return self.winsorize(x) 
    
    def encode(self, descriptors: torch.Tensor):
        """Public facing encode function
        
        Ensure model has been loaded from a pre-trained model and model is in eval mode

        Args:
            descriptors (torch.Tensor): Input unscaled descriptors

        Returns:
            torch.Tensor: Encoded descriptors
        """
        descriptors = self._scale(descriptors)
        return self._encode(descriptors)

    def _encode(self, x):
        return self.encoder(x)

    def _decode(self, x):
        return self.decoder(x)

    def forward(self, desccriptors):
        return self._decode(self._encode(desccriptors))

    def _step(self, descriptors, name):
        descriptors = self._scale(descriptors)
        reconstruction = self(descriptors)
        loss = torch.nn.functional.mse_loss(reconstruction, descriptors, reduction="mean")
        self.log(f"{name}/loss", loss)
        return loss

    def training_step(self, batch, batch_idx):
        descriptors = self._scale(batch)
        mask = (torch.rand_like(descriptors) < self.masking_ratio).int()
        descriptors *= mask
        reconstruction = self(descriptors)
        loss = torch.nn.functional.mse_loss(reconstruction[mask.bool()], descriptors[mask.bool()], reduction="mean")
        self.log("train/masked_loss", loss)
        return loss

    def validation_step(self, batch, batch_idx):
        return self._step(batch, "validation")

    def test_step(self, batch, batch_idx):
        return self._step(batch, "test")

if __name__ == "__main__":
    # test batch of 4
    features = torch.rand((4, 1613))

    model = fastpropFoundation(
        feature_means=features.mean(),
        feature_vars=features.var(),
        num_features=1613,
        hidden_sizes=(2048, 1448, 1024, 724, 512, 362, 256, 181, 128, 90),
        encoding_size=64,
    )
    print(model)
    print(model(features))
