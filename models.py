import math
from itertools import chain
from types import SimpleNamespace
from typing import List, Tuple

import torch
import numpy as np
from torchmetrics.functional import pearson_corrcoef
from fastprop.data import standard_scale, inverse_standard_scale
from fastprop.model import fastprop
from fastprop.metrics import SCORE_LOOKUP

from lightning import LightningModule
from torch import distributed



# code for the SNN has been adapted from the author's demo notebook on GitHub:
# https://github.com/bioinf-jku/SNNs/blob/master/Pytorch/SelfNormalizingNetworks_MLP_MNIST.ipynb


class fastpropFineTuner(fastprop):
    def __init__(
        self,
        pretrained_checkpoint,
        fine_tune_layers: Tuple[int, ...] = (
            1800,
            1800,
        ),
        readout_size: int = 1,
        num_tasks: int = 1,
        problem_type: str = "regression",
        learning_rate: float = 0.0001,
        target_names: List[str] = [],
        target_means: torch.Tensor = None,
        target_vars: torch.Tensor = None,
        freeze_pretrained: bool = True,
    ):
        pretrained: fastpropAutoEncoder = fastpropAutoEncoder.load_from_checkpoint(pretrained_checkpoint)
        super().__init__(
            input_size=1,  # we will overwrite this
            hidden_size=1,  # and this
            fnn_layers=0,  # and this
            readout_size=1,  # and this
            num_tasks=num_tasks,
            learning_rate=learning_rate,
            problem_type=problem_type,
            target_names=target_names,
            feature_means=pretrained.feature_means,
            feature_vars=pretrained.feature_vars,
            target_means=target_means,
            target_vars=target_vars,
        )
        del self.fnn
        del self.readout
        if freeze_pretrained:
            for param in pretrained.model_weights.values():
                param.requires_grad_(False)
        self.pretrained_encoder = lambda x: pretrained._encode(x)
        mlp_modules = []
        for curr_size, next_size in zip(chain([pretrained.hparams['encoding_size']], fine_tune_layers), fine_tune_layers):
            mlp_modules.extend((torch.nn.Linear(curr_size, next_size), torch.nn.SELU()))
        if len(mlp_modules) > 2:  # remove the last activation for MLPs
            mlp_modules.pop()
        self.mlp = torch.nn.Sequential(*mlp_modules)
        self.readout = torch.nn.Linear(pretrained.hparams['encoding_size'] if not fine_tune_layers else fine_tune_layers[-1], readout_size)

        self._reset_parameters()
        self.save_hyperparameters()

    def _reset_parameters(self):
        for param in chain(self.mlp.parameters(), self.readout.parameters()):
            # biases zero
            if len(param.shape) == 1:
                torch.nn.init.constant_(param, 0)
            # others using lecun-normal initialization
            else:
                torch.nn.init.kaiming_normal_(param, mode='fan_in', nonlinearity='linear')

    def forward(self, x):
        x = standard_scale(x, self.feature_means, self.feature_vars)
        x = self.pretrained_encoder(x)
        x = self.mlp(x)
        x = self.readout(x)
        return x

class fastpropFoundation(LightningModule):
    def __init__(
        self,
        feature_means: torch.Tensor,
        feature_vars: torch.Tensor,
        num_features: int = 1613,
        hidden_sizes: Tuple[int, ...] = (1024,),
        encoding_size: int = 256,
        learning_rate: float = 0.001,
    ):
        """Implements a mordred-descriptor based Self Normalizing Denoising autoencoder with tied weights.

        Args:
            feature_means (torch.Tensor): Means of input features.
            feature_vars (torch.Tensor): Variances of input features.
            num_features (int, optional): Number of input features. Defaults to 1613.
            hidden_sizes (Tuple[int, ...], optional): Tuple of sizes for hidden layers. Defaults to (1024,).
            encoding_size (int, optional): Size of final encoding. Defaults to 256.
            learning_rate (float, optional): Learning rate for optimizer. Defaults to 0.001.
        """
        super().__init__()
        self.n_layers = 1 + len(hidden_sizes)
        self.register_buffer("feature_means", feature_means)
        self.register_buffer("feature_vars", feature_vars)
        self.learning_rate = learning_rate
        self.dropout_80 = torch.nn.AlphaDropout(p=0.80)
        self.dropout_50 = torch.nn.AlphaDropout(p=0.50)
        self.model_weights = torch.nn.ParameterList()
        for i, in_features, out_features in zip(
            range(len(hidden_sizes) + 1),  # layer counter
            chain([num_features], hidden_sizes),  # input -> last hidden layer
            chain(hidden_sizes, [encoding_size]),  # first hidden layer -> readout
        ):
            # opposite of expected order since torch.nn.functional.linear will transpose the weights
            self.model_weights.append(torch.empty(out_features, in_features, dtype=torch.float32))
        self._reset_parameters()
        self.save_hyperparameters()
    
    def configure_optimizers(self):
        """See https://lightning.ai/docs/pytorch/stable/common/optimization.html

        Returns:
            dict: Optimizer name and instance.
        """
        return {"optimizer": torch.optim.Adam(self.parameters(), lr=self.learning_rate)}

    def log(self, name, value, **kwargs):
        """Wrap the parent PyTorch Lightning log function to automatically detect DDP."""
        return super().log(name, value, sync_dist=distributed.is_initialized(), **kwargs)

    def _reset_parameters(self):
        for weight in chain(self.model_weights,):
            # zero out biases
            if len(weight.shape) == 1:
                torch.nn.init.constant_(weight, 0)
            else:
                # lecun-normal initialization for weights
                torch.nn.init.kaiming_normal_(weight, mode="fan_in", nonlinearity="linear")
    
    def _scale(self, x: torch.Tensor):
        return standard_scale(x, self.feature_means, self.feature_vars)
    
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
            x = torch.nn.functional.selu(x)
            x = self.dropout_50(x)
        x = torch.nn.functional.linear(x, self.model_weights[-1], bias=None)
        return x

    def _decode(self, x):
        for i in reversed(range(1, self.n_layers)):
            x = torch.nn.functional.selu(torch.nn.functional.linear(x, self.model_weights[i].T, bias=None))
        x = torch.nn.functional.linear(x, self.model_weights[0].T, bias=None)
        return x

    def forward(self, desccriptors):
        return self._decode(self._encode(desccriptors))

    def _step(self, descriptors, name):
        descriptors = self._scale(descriptors)
        reconstruction = self(descriptors)
        loss = torch.nn.functional.huber_loss(reconstruction, descriptors, reduction="mean")
        self.log(f"{name}/loss", loss)
        return loss

    def training_step(self, batch, batch_idx):
        return self._step(batch, "train")

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
