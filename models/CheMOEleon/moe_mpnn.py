"""
=============================================================================
Adaptive Mixture of Local Experts Message Passing (MoE-MPNN)
=============================================================================
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor
from typing import Optional, Union

from lightning.pytorch.core.mixins import HyperparametersMixin
from chemprop.conf import DEFAULT_ATOM_FDIM, DEFAULT_BOND_FDIM, DEFAULT_HIDDEN_DIM
from chemprop.data import BatchMolGraph
from chemprop.nn.message_passing.proto import MessagePassing
from chemprop.nn.message_passing import BondMessagePassing
from chemprop.nn.transforms import ScaleTransform, GraphTransform

class AdaptiveMixtureMessagePassing(MessagePassing, HyperparametersMixin):
    """
    An Adaptive Mixture of Local Experts (MoE) Message Passing encoder.
    
    This architecture initializes `n_experts` independent message passing networks 
    (e.g., BondMessagePassing) along with a single `gate` message passing network. 
    The gate network computes node-level attention logits, which are softmaxed 
    into weights to dynamically blend the node representations from each expert.
    """
    def __init__(
        self,
        n_experts: int = 4,
        d_v: int = DEFAULT_ATOM_FDIM,
        d_e: int = DEFAULT_BOND_FDIM,
        d_h: int = DEFAULT_HIDDEN_DIM,
        d_vd: Optional[int] = None,
        depth: int = 3,
        dropout: float = 0.0,
        activation: Union[str, nn.Module] = "relu",
        undirected: bool = False,
        bias: bool = False,
        V_d_transform: Optional[ScaleTransform] = None,
        graph_transform: Optional[GraphTransform] = None,
    ):
        super().__init__()
        
        # Suppress PyTorch Lightning warnings regarding module state_dict saves
        ignore_list = ["V_d_transform", "graph_transform", "activation"]
        self.save_hyperparameters(ignore=ignore_list)
        self.hparams["V_d_transform"] = V_d_transform
        self.hparams["graph_transform"] = graph_transform
        self.hparams["activation"] = activation
        self.hparams["cls"] = self.__class__
        
        self.n_experts = n_experts
        self.d_h = d_h
        
        self.V_d_transform = V_d_transform if V_d_transform is not None else nn.Identity()
        self.graph_transform = graph_transform if graph_transform is not None else nn.Identity()

        # Instantiate standard message passing experts
        # Note: We pass None to their transforms so we can manage transforms centrally 
        # at the MoE block level to avoid duplicate scaling operations.
        self.experts = nn.ModuleList([
            BondMessagePassing(
                d_v=d_v,
                d_e=d_e,
                d_h=d_h,
                d_vd=d_vd,
                depth=depth,
                dropout=dropout,
                activation=activation,
                undirected=undirected,
                bias=bias,
            )
            for _ in range(n_experts)
        ])
        
        # Instantiate the gating MPNN
        self.gate_mpnn = BondMessagePassing(
            d_v=d_v,
            d_e=d_e,
            d_h=d_h,
            d_vd=d_vd,
            depth=depth,
            dropout=dropout,
            activation=activation,
            undirected=undirected,
            bias=bias,
        )
        
        # Linear projection to compute the expert mixture weights for each node
        self.gate_proj = nn.Linear(self.gate_mpnn.output_dim, n_experts)

        # For analysis and interpretability
        self._last_gate_weights: Optional[Tensor] = None

    @property
    def output_dim(self) -> int:
        return self.experts[0].output_dim
        
    def forward(self, bmg: BatchMolGraph, V_d: Optional[Tensor] = None) -> Tensor:
        """
        Executes the Mixture of Experts forward pass over a BatchMolGraph.
        """
        # 1. Centrally apply transforms once
        bmg = self.graph_transform(bmg)
        
        # Chemprop handles V_d differently depending on training phase, so we apply it manually here
        # to ensure it is only transformed once before being handed off to all experts.
        if V_d is not None and not isinstance(self.V_d_transform, nn.Identity):
            V_d = self.V_d_transform(V_d)
            
        # 2. Extract node representations from all experts
        expert_outputs = torch.stack([expert(bmg, V_d) for expert in self.experts], dim=1)  
        # shape: [num_nodes, n_experts, d_h]
        
        # 3. Compute local node-level gating weights
        gate_rep = self.gate_mpnn(bmg, V_d)           # [num_nodes, gate_d_h]
        gate_logits = self.gate_proj(gate_rep)        # [num_nodes, n_experts]
        gate_weights = F.softmax(gate_logits, dim=-1) # [num_nodes, n_experts]
        
        # Save gating weights for interpretability 
        # (e.g., visualizing which atoms route to which expert MPNN)
        self._last_gate_weights = gate_weights.detach()
        
        # 4. Blend the expert representations dynamically per node
        out = torch.einsum("ne,neh->nh", gate_weights, expert_outputs)
        
        return out
