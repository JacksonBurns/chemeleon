"""
=============================================================================
Graph Transformer Encoder for Chemprop
=============================================================================

Author/Generator: Google Gemini (AI Assistant)

Description:
This module implements a Graph Transformer architecture adapted specifically 
for the Chemprop library. It acts as a drop-in replacement for Chemprop's 
standard Directed Message Passing Neural Network (D-MPNN) encoder. 

To achieve compatibility and remove external dependencies, the following 
modifications were made by the AI:
1. Ported the core Graph Transformer convolution logic from PyTorch Geometric
   (PyG) into native PyTorch.
2. Implemented a custom `scatter_softmax` function to handle sparse attention 
   over graphs without relying on PyG's scatter routines.
3. Restructured the forward pass to natively ingest Chemprop's `BatchMolGraph` 
   data structures.
4. Integrated Chemprop's descriptor concatenation (`V_d`) directly into the 
   Transformer's readout phase.
5. Added optional weight-tying across message passing depths.

Original Source Attribution:
The foundational architecture and logic for this model are based on the 
`gt-pyg` repository:
Source: https://github.com/pgniewko/gt-pyg
License: MIT License

MIT License Summary:
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
=============================================================================
"""

import math
import torch
from torch import nn, Tensor
from typing import Optional

from lightning.pytorch.core.mixins import HyperparametersMixin
from chemprop.conf import DEFAULT_ATOM_FDIM, DEFAULT_BOND_FDIM, DEFAULT_HIDDEN_DIM
from chemprop.data import BatchMolGraph
from chemprop.nn.message_passing.proto import MessagePassing
from chemprop.nn.transforms import ScaleTransform, GraphTransform
from chemprop.nn.ffn import MLP


def scatter_softmax(src: Tensor, index: Tensor, dim_size: int) -> Tensor:
    """
    Computes a sparsely evaluated softmax.
    
    Parameters
    ----------
    src : Tensor
        The source tensor of shape [num_edges, num_heads]
    index : Tensor
        The destination indices for each edge of shape [num_edges]
    dim_size : int
        The total number of destination nodes
        
    Returns
    -------
    Tensor
        The softmax-normalized tensor of shape [num_edges, num_heads]
    """
    # 1. Find the maximum value per destination node for numerical stability
    max_val = torch.zeros(dim_size, src.size(1), dtype=src.dtype, device=src.device)
    # Uses amax to find the max logit per node. 
    max_val.scatter_reduce_(0, index.unsqueeze(1).expand_as(src), src, reduce="amax", include_self=False)
    max_val_gathered = max_val[index]

    # 2. Compute exponentials safely
    exp_src = torch.exp(src - max_val_gathered)

    # 3. Sum the exponentials per destination node
    sum_exp = torch.zeros(dim_size, src.size(1), dtype=src.dtype, device=src.device)
    sum_exp.scatter_add_(0, index.unsqueeze(1).expand_as(exp_src), exp_src)
    sum_exp_gathered = sum_exp[index]

    # 4. Normalize
    return exp_src / (sum_exp_gathered + 1e-16)


class AttentionAtomMessagePassingLayer(nn.Module):
    """
    Native PyTorch implementation of the GTConv layer from gt-pyg.
    """
    def __init__(
        self,
        node_in_dim: int,
        hidden_dim: int,
        edge_in_dim: Optional[int] = None,
        num_heads: int = 8,
        gate: bool = False,
        qkv_bias: bool = False,
        dropout: float = 0.1,
        act: str = "gelu",
        update_edges: bool = True,
    ):
        super().__init__()
        if hidden_dim % num_heads != 0:
            raise ValueError(f"hidden_dim ({hidden_dim}) must be divisible by num_heads ({num_heads})")

        self.num_heads = num_heads
        self.hidden_dim = hidden_dim
        self.head_dim = hidden_dim // num_heads
        self.edge_in_dim = edge_in_dim
        self.gate = gate
        self.update_edges = update_edges

        # Node Projections
        self.WQ = nn.Linear(node_in_dim, hidden_dim, bias=qkv_bias)
        self.WK = nn.Linear(node_in_dim, hidden_dim, bias=qkv_bias)
        self.WV = nn.Linear(node_in_dim, hidden_dim, bias=qkv_bias)
        self.WO = nn.Linear(hidden_dim, node_in_dim, bias=True)

        if edge_in_dim is not None:
            self.WE_logits = nn.Linear(edge_in_dim, num_heads, bias=True)
            self.WE_value = nn.Linear(edge_in_dim, hidden_dim, bias=True)
            self.norm0e = nn.LayerNorm(edge_in_dim)
            
            # Conditionally instantiate edge update network
            if update_edges:
                self.WOe = nn.Linear(hidden_dim, edge_in_dim, bias=True)
                edge_ffn_hidden = max(hidden_dim, 2 * edge_in_dim)
                self.ffn_e = MLP.build(input_dim=edge_in_dim, output_dim=edge_in_dim, hidden_dim=edge_ffn_hidden, dropout=dropout, activation=nn.GELU() if act == "gelu" else nn.ReLU())
                self.norm1e = nn.LayerNorm(edge_in_dim)
            else:
                self.WOe = None
                self.ffn_e = None
                self.norm1e = None
        else:
            self.WE_logits = None
            self.WE_value = None
            self.WOe = None
            self.ffn_e = None
            self.norm0e = None
            self.norm1e = None

        self.norm1 = nn.LayerNorm(node_in_dim)
        self.norm2 = nn.LayerNorm(node_in_dim)

        # Gating Projections
        if gate:
            self.n_gate = nn.Linear(node_in_dim, hidden_dim, bias=True)
            if edge_in_dim is not None:
                self.e_gate = nn.Linear(edge_in_dim, num_heads, bias=True)
            else:
                self.register_parameter("e_gate", None)
        else:
            self.register_parameter("n_gate", None)
            self.register_parameter("e_gate", None)

        self.dropout_layer = nn.Dropout(p=dropout)
        self.attn_dropout = nn.Dropout(p=dropout)

        node_ffn_hidden = max(hidden_dim, 4 * node_in_dim)
        self.ffn = MLP.build(input_dim=node_in_dim, output_dim=edge_in_dim, hidden_dim=node_ffn_hidden, dropout=dropout, activation=nn.GELU() if act == "gelu" else nn.ReLU())

    def forward(self, V: Tensor, E: Optional[Tensor], edge_index: Tensor) -> tuple[Tensor, Optional[Tensor]]:
        """
        Parameters
        ----------
        V : Tensor [num_nodes, node_in_dim]
        E : Tensor [num_edges, edge_in_dim] or None
        edge_index : Tensor [2, num_edges] 
            edge_index[0] is source node, edge_index[1] is target node.
        """
        V_res = V
        E_res = E

        # 1. Pre-norm for Nodes
        V_norm = self.norm1(V)
        num_nodes = V_norm.size(0)

        Q = self.WQ(V_norm).view(-1, self.num_heads, self.head_dim)
        K = self.WK(V_norm).view(-1, self.num_heads, self.head_dim)
        V_proj = self.WV(V_norm).view(-1, self.num_heads, self.head_dim)

        # Map indices to sources and destinations
        src, dst = edge_index[0], edge_index[1]
        
        Q_dst = Q[dst]   # [num_edges, num_heads, head_dim]
        K_src = K[src]
        V_src = V_proj[src]

        if self.gate and self.n_gate is not None:
            G = self.n_gate(V_norm).view(-1, self.num_heads, self.head_dim)
            G_src = G[src]
        else:
            G_src = None

        # 2. Edge values and biases
        if self.edge_in_dim is not None and E is not None:
            E_norm = self.norm0e(E)
            E_val = self.WE_value(E_norm).view(-1, self.num_heads, self.head_dim)
            E_bias = self.WE_logits(E_norm) # [num_edges, num_heads]
        else:
            E_val = None
            E_bias = 0.0

        # 3. Compute Attention Logits
        # Q_dst * K_src element-wise, then sum over head_dim
        logits_vec = (Q_dst * K_src) / math.sqrt(self.head_dim) 
        logits = logits_vec.sum(dim=-1) + E_bias # [num_edges, num_heads]

        # 4. Modify Values with Edges and Gates
        if E_val is not None:
            V_src = V_src + E_val
            
        if self.gate and G_src is not None:
            V_src = V_src * torch.sigmoid(G_src)

        if self.gate and self.e_gate is not None and E is not None:
            e_gate = self.e_gate(E_norm)
            logits = logits * torch.sigmoid(e_gate)

        # 5. Softmax and Attention Weighting
        alpha = scatter_softmax(logits, dst, dim_size=num_nodes) # [num_edges, num_heads]
        alpha = self.attn_dropout(alpha)
        
        message = alpha.view(-1, self.num_heads, 1) * V_src # [num_edges, num_heads, head_dim]

        # 6. Aggregate messages to destination nodes
        out = torch.zeros(num_nodes, self.num_heads, self.head_dim, device=V.device)
        out.scatter_add_(0, dst.view(-1, 1, 1).expand_as(message), message)
        out = out.view(-1, self.hidden_dim) # Flatten heads: [num_nodes, hidden_dim]

        # 7. Node Output and Residual
        attn_out = self.WO(out)
        attn_out = self.dropout_layer(attn_out)
        V1 = V_res + attn_out

        V1_norm = self.norm2(V1)
        ffn_out = self.ffn(V1_norm)
        ffn_out = self.dropout_layer(ffn_out)
        V_out = V1 + ffn_out

        # 8. Edge Updates
        if self.edge_in_dim is None or E is None or not self.update_edges:
            E_out = E
        else:
            eij = logits_vec * E_val # [num_edges, num_heads, head_dim]
            e_context = eij.view(-1, self.hidden_dim)
            e_attn = self.WOe(e_context)
            e_attn = self.dropout_layer(e_attn)

            E1 = E_res + e_attn
            E1_norm = self.norm1e(E1)
            E_ffn = self.ffn_e(E1_norm)
            E_ffn = self.dropout_layer(E_ffn)
            E_out = E1 + E_ffn

        return V_out, E_out


class AttentionAtomMessagePassing(MessagePassing, HyperparametersMixin):
    """
    A Graph Transformer Message Passing block designed to drop-in to Chemprop's registry.
    It replaces the Directed Message Passing Neural Network (D-MPNN) encoder.
    """
    def __init__(
        self,
        d_v: int = DEFAULT_ATOM_FDIM,
        d_e: int = DEFAULT_BOND_FDIM,
        d_h: int = DEFAULT_HIDDEN_DIM,
        num_layers: int = 10,
        num_heads: int = 8,
        dropout: float = 0.1,
        gate: bool = False,
        qkv_bias: bool = False,
        tied_weights: bool = False,
        d_vd: int | None = None,
        V_d_transform: ScaleTransform | None = None,
        graph_transform: GraphTransform | None = None,
    ):
        super().__init__()
        # Ignore variables handled externally or manually to suppress Lightning warnings
        self.save_hyperparameters(ignore=["V_d_transform", "graph_transform"])
        self.hparams["V_d_transform"] = V_d_transform
        self.hparams["graph_transform"] = graph_transform
        self.hparams["cls"] = self.__class__
        
        self.d_h = d_h
        self.d_vd = d_vd
        self.num_layers = num_layers
        self.tied_weights = tied_weights
        self.V_d_transform = V_d_transform if V_d_transform is not None else nn.Identity()
        self.graph_transform = graph_transform if graph_transform is not None else nn.Identity()

        # Input Encoders
        self.node_emb = nn.Linear(d_v, d_h, bias=False)
        self.edge_emb = nn.Linear(d_e, d_h, bias=False) if d_e else None

        self.input_norm = nn.LayerNorm(d_h)
        self.input_dropout = nn.Dropout(dropout)

        # Transformer Blocks
        if self.tied_weights:
            self.shared_layer = AttentionAtomMessagePassingLayer(
                node_in_dim=d_h,
                hidden_dim=d_h,
                edge_in_dim=d_h if d_e else None,
                num_heads=num_heads,
                gate=gate,
                qkv_bias=qkv_bias,
                dropout=dropout,
                update_edges=True  # Must keep updating edges so they cascade down the depths
            )
        else:
            self.layers = nn.ModuleList([
                AttentionAtomMessagePassingLayer(
                    node_in_dim=d_h,
                    hidden_dim=d_h,
                    edge_in_dim=d_h if d_e else None,
                    num_heads=num_heads,
                    gate=gate,
                    qkv_bias=qkv_bias,
                    dropout=dropout,
                    update_edges=(i < num_layers - 1)
                ) for i in range(num_layers)
            ])

        # Readout Projection (to combine with extra descriptors V_d if they exist)
        if d_vd is not None:
            self.W_d = nn.Linear(d_h + d_vd, d_h + d_vd)
        else:
            self.W_d = None

    @property
    def output_dim(self) -> int:
        return self.W_d.out_features if self.W_d is not None else self.d_h

    def forward(self, bmg: BatchMolGraph, V_d: Tensor | None = None) -> Tensor:
        """
        Executes the Graph Transformer forward pass over a BatchMolGraph.
        
        Parameters
        ----------
        bmg : BatchMolGraph
            The batched molecular graph input.
        V_d : Tensor, optional
            Additional vertex descriptors, by default None
            
        Returns
        -------
        Tensor
            The processed node representations ready for global pooling.
        """
        bmg = self.graph_transform(bmg)

        # 1. Embed node features
        V = self.node_emb(bmg.V)
        V = self.input_norm(V)
        V = self.input_dropout(V)

        # 2. Embed edge features
        if self.edge_emb is not None:
            E = self.edge_emb(bmg.E)
        else:
            E = None

        # 3. Message Passing over Transformer Layers
        if self.tied_weights:
            for _ in range(self.num_layers):
                V, E = self.shared_layer(V, E, bmg.edge_index)
        else:
            for layer in self.layers:
                V, E = layer(V, E, bmg.edge_index)

        # 4. Finalize with extra descriptors (matching Chemprop's API expectations)
        if V_d is not None and self.W_d is not None:
            V_d = self.V_d_transform(V_d)
            V = self.W_d(torch.cat((V, V_d), dim=1))
            V = self.input_dropout(V)

        return V
