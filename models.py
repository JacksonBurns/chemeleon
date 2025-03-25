import math
from itertools import chain
from typing import Tuple

import torch
from fastprop.data import standard_scale
from lightning import LightningModule
from torch import distributed

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
        encoding_size: int = 256,
        learning_rate: float = 0.001,
        snn: bool = True,
    ):
        """Implements a mordred-descriptor based Self Normalizing Denoising autoencoder with tied weights.

        Args:
            feature_means (torch.Tensor): Means of input features.
            feature_vars (torch.Tensor): Variances of input features.
            num_features (int, optional): Number of input features. Defaults to 1613.
            winsorization_factor (int, optional): # of stdev to cutoff rescaled inputs. Defaults to None (i.e. disabled).
            hidden_sizes (Tuple[int, ...], optional): Tuple of sizes for hidden layers. Defaults to (1024,).
            encoding_size (int, optional): Size of final encoding. Defaults to 256.
            learning_rate (float, optional): Learning rate for optimizer. Defaults to 0.001.
            snn (bool, optional): Use self-normalizing architecture. Default True.
        """
        super().__init__()
        self.n_layers = 1 + len(hidden_sizes)
        self.register_buffer("feature_means", feature_means)
        self.register_buffer("feature_vars", feature_vars)
        self.learning_rate = learning_rate
        self.act = torch.nn.SELU() if snn else torch.nn.LeakyReLU()
        self.dropout_80 = torch.nn.AlphaDropout(p=0.80) if snn else torch.nn.Dropout(p=0.8)
        self.dropout_50 = torch.nn.AlphaDropout(p=0.50) if snn else torch.nn.Dropout(p=0.5)
        self.winsorize = False
        if winsorization_factor is not None:
            self.winsorize = WinsorizeStdevN(winsorization_factor)
        self.model_weights = torch.nn.ParameterList()
        for i, in_features, out_features in zip(
            range(len(hidden_sizes) + 1),  # layer counter
            chain([num_features], hidden_sizes),  # input -> last hidden layer
            chain(hidden_sizes, [encoding_size]),  # first hidden layer -> readout
        ):
            # opposite of expected order since torch.nn.functional.linear will transpose the weights
            self.model_weights.append(torch.empty(out_features, in_features, dtype=torch.float32))
        self._reset_parameters(snn)
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

    def _reset_parameters(self, snn):
        for weight in chain(self.model_weights,):
            if snn:
                torch.nn.init.kaiming_normal_(weight, mode="fan_in", nonlinearity="linear")
            else:
                torch.nn.init.kaiming_uniform_(weight, a=math.sqrt(5))
    
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
        x = self.dropout_80(x)
        for i in range(self.n_layers - 1):
            x = torch.nn.functional.linear(x, self.model_weights[i], bias=None)
            x = self.act(x)
            x = self.dropout_50(x)
        x = torch.nn.functional.linear(x, self.model_weights[-1], bias=None)
        return x

    def _decode(self, x):
        for i in reversed(range(1, self.n_layers)):
            x = self.act(torch.nn.functional.linear(x, self.model_weights[i].T, bias=None))
        x = torch.nn.functional.linear(x, self.model_weights[0].T, bias=None)
        return x

    def forward(self, desccriptors):
        return self._decode(self._encode(desccriptors))

    def _step(self, descriptors, name):
        descriptors = self._scale(descriptors)
        reconstruction = self(descriptors)
        loss = torch.nn.functional.mse_loss(reconstruction, descriptors, reduction="mean")
        self.log(f"{name}/loss", loss)
        return loss

    def training_step(self, batch, batch_idx):
        return self._step(batch, "train")

    def validation_step(self, batch, batch_idx):
        return self._step(batch, "validation")

    def test_step(self, batch, batch_idx):
        return self._step(batch, "test")

class fastpropFoundationMaskedDAE(LightningModule):
    def __init__(
        self,
        feature_means: torch.Tensor,
        feature_vars: torch.Tensor,
        num_features: int = 1613,
        winsorization_factor=None,
        hidden_sizes: Tuple[int, ...] = (1024,),
        encoding_size: int = 256,
        learning_rate: float = 0.001,
        masking_ratio: float = 0.15,
    ):
        """Implements a mordred-descriptor based Self Normalizing Denoising autoencoder with tied weights.

        Args:
            feature_means (torch.Tensor): Means of input features.
            feature_vars (torch.Tensor): Variances of input features.
            num_features (int, optional): Number of input features. Defaults to 1613.
            winsorization_factor (int, optional): # of stdev to cutoff rescaled inputs. Defaults to None (i.e. disabled).
            hidden_sizes (Tuple[int, ...], optional): Tuple of sizes for hidden layers. Defaults to (1024,).
            encoding_size (int, optional): Size of final encoding. Defaults to 256.
            learning_rate (float, optional): Learning rate for optimizer. Defaults to 0.001.
            snn (bool, optional): Use self-normalizing architecture. Default True.
        """
        super().__init__()
        self.register_buffer("feature_means", feature_means)
        self.register_buffer("feature_vars", feature_vars)
        self.learning_rate = learning_rate
        self.winsorize = False
        self.masking_ratio = masking_ratio
        if winsorization_factor is not None:
            self.winsorize = WinsorizeStdevN(winsorization_factor)
        modules = []
        for i in range(len(hidden_sizes)):
            modules.append(torch.nn.Linear(num_features if i == 0 else hidden_sizes[i], hidden_sizes[i]))
            modules.append(torch.nn.LeakyReLU())
        modules.append(torch.nn.Linear(hidden_sizes[-1], encoding_size))
        self.encoder = torch.nn.Sequential(*modules)
        self.decoder = torch.nn.Linear(encoding_size, num_features)
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
        mask = (torch.rand_like(descriptors) > self.masking_ratio).float()
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
