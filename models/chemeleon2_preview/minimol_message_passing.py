import torch
import torch.nn as nn
from torch import Tensor

from lightning.pytorch.core.mixins import HyperparametersMixin
from chemprop.data import BatchMolGraph
from chemprop.nn.message_passing.proto import MessagePassing
from chemprop.nn.transforms import ScaleTransform, GraphTransform

class MinimolMessagePassing(MessagePassing, HyperparametersMixin):
    """
    A drop-in MessagePassing block for Chemprop that implements the MiniMol 
    molecular foundation model architecture.
    """
    def __init__(
        self,
        d_v: int,
        d_e: int,
        d_h: int = 300,
        d_vd: int = 0,
        depth: int = 5,
        dropout: float = 0.0,
        backbone_type: str = "gine",  # "gine" or "mpnn++"
        V_d_transform: ScaleTransform | None = None,
        graph_transform: GraphTransform | None = None,
    ):
        super().__init__()
        
        # 1. Handle serialization for PyTorch Lightning / Chemprop
        self.save_hyperparameters(ignore=["V_d_transform", "graph_transform"])
        self.hparams["V_d_transform"] = V_d_transform
        self.hparams["graph_transform"] = graph_transform
        self.hparams["cls"] = self.__class__
        
        self.d_h = d_h

        # 2. Store input transforms (default to Identity so .train() doesn't crash if None)
        self.V_d_transform = V_d_transform if V_d_transform is not None else nn.Identity()
        self.graph_transform = graph_transform if graph_transform is not None else nn.Identity()
        
        # 3. Initial Embeddings 
        self.mlp_x = nn.Sequential(
            nn.Linear(d_v + d_vd, d_h),
            nn.ReLU(),
            nn.Linear(d_h, d_h)
        )
        self.mlp_e = nn.Sequential(
            nn.Linear(d_e, d_h),
            nn.ReLU(),
            nn.Linear(d_h, d_h)
        )
        
        # Only instantiate the global node MLP if the backbone actually uses it
        if backbone_type.lower() == "mpnn++":
            self.mlp_g = nn.Sequential(
                nn.Linear(d_h, d_h),
                nn.ReLU(),
                nn.Linear(d_h, d_h)
            )
        else:
            self.mlp_g = None
        
        # 4. GNN Backbone
        self.layers = nn.ModuleList()
        for i in range(depth):
            is_last = (i == depth - 1)  # <-- Flag the final layer to prevent unused parameters
            if backbone_type.lower() == "gine":
                self.layers.append(MinimolGINELayer(d_h, dropout))
            elif backbone_type.lower() == "mpnn++":
                self.layers.append(MinimolMPNNPlusPlusLayer(d_h, dropout, is_last_layer=is_last))
            else:
                raise ValueError(f"Unrecognized MiniMol backbone: {backbone_type}")

    @property
    def output_dim(self) -> int:
        return self.d_h
                
    def forward(self, bmg: BatchMolGraph, V_d: Tensor | None = None) -> Tensor:
        # Apply Chemprop's standard input normalizations
        bmg = self.graph_transform(bmg)
        if V_d is not None:
            V_d = self.V_d_transform(V_d)

        # Concatenate extra atom descriptors if provided
        V = bmg.V if V_d is None else torch.cat([bmg.V, V_d], dim=-1)
        E = bmg.E
        
        # Calculate initial embeddings
        x = self.mlp_x(V)
        e = self.mlp_e(E)
        
        # Conditionally process the global node
        g = None
        if self.mlp_g is not None:
            batch_size = int(bmg.batch.max().item()) + 1
            g_rand = torch.randn(batch_size, self.d_h, device=V.device)
            g = self.mlp_g(g_rand)
        
        # Pass representations through the backbone
        for layer in self.layers:
            x, e, g = layer(x, e, g, bmg.edge_index, bmg.batch)
            
        return x


class MinimolMPNNPlusPlusLayer(nn.Module):
    """
    Implements the complex MPNN++ layer described in Appendix A.1 of the MiniMol paper,
    incorporating node, edge, and global state updates alongside skip connections.
    """
    def __init__(self, d_h: int, dropout: float = 0.0, is_last_layer: bool = False):
        super().__init__()
        self.is_last_layer = is_last_layer
        
        # Edge update takes [x_u | x_v | e_uv | g^l]
        self.mlp_edge = nn.Sequential(
            nn.Linear(4 * d_h, d_h), nn.ReLU(), nn.Dropout(dropout), nn.Linear(d_h, d_h)
        )
        # Node update takes [x_i | \sum e_ui | \sum e_iv | \sum x_u ; g^l]
        self.mlp_node = nn.Sequential(
            nn.Linear(5 * d_h, d_h), nn.ReLU(), nn.Dropout(dropout), nn.Linear(d_h, d_h)
        )
        
        # Global update takes [g^l | \sum x_j | \sum e_uv]
        # Skip creating this on the final layer to prevent PyTorch DDP "unused parameters" error
        if not self.is_last_layer:
            self.global_proj = nn.Sequential(
                nn.Linear(3 * d_h, d_h), nn.ReLU(), nn.Dropout(dropout), nn.Linear(d_h, d_h)
            )
        else:
            self.global_proj = None

    def forward(self, x: Tensor, e: Tensor, g: Tensor, edge_index: Tensor, batch: Tensor) -> tuple[Tensor, Tensor, Tensor]:
        src, dst = edge_index
        
        # 1. Edge Update
        g_edges = g[batch[src]]
        edge_inputs = torch.cat([x[src], x[dst], e, g_edges], dim=-1)
        e_bar = self.mlp_edge(edge_inputs)
        e_out = e + e_bar  # Skip connection
        
        # 2. Node Update
        # \sum_{(u,i)} e_ui
        e_in_sum = torch.zeros_like(x)
        e_in_sum.scatter_add_(0, dst.unsqueeze(-1).expand_as(e_bar), e_bar)
        
        # \sum_{(i,v)} e_iv
        e_out_sum = torch.zeros_like(x)
        e_out_sum.scatter_add_(0, src.unsqueeze(-1).expand_as(e_bar), e_bar)
        
        # \sum_{(u,i)} x_u
        x_u_sum = torch.zeros_like(x)
        x_u_sum.scatter_add_(0, dst.unsqueeze(-1).expand_as(x[src]), x[src])
        
        g_nodes = g[batch]
        node_inputs = torch.cat([x, e_in_sum, e_out_sum, x_u_sum, g_nodes], dim=-1)
        x_bar = self.mlp_node(node_inputs)
        x_out = x + x_bar  # Skip connection
        
        # 3. Global Update
        if self.is_last_layer:
            g_out = g  # Return untouched g (avoids unused parameters propagating down the graph)
        else:
            x_sum = torch.zeros_like(g)
            x_sum.scatter_add_(0, batch.unsqueeze(-1).expand_as(x_bar), x_bar)
            
            e_sum = torch.zeros_like(g)
            e_sum.scatter_add_(0, batch[src].unsqueeze(-1).expand_as(e_bar), e_bar)
            
            global_inputs = torch.cat([g, x_sum, e_sum], dim=-1)
            g_bar = self.global_proj(global_inputs)
            g_out = g + g_bar  # Skip connection
        
        return x_out, e_out, g_out

class MinimolGINELayer(nn.Module):
    """
    The GINE backbone variant for MiniMol.
    """
    def __init__(self, d_h: int, dropout: float = 0.0, eps: float = 0.0):
        super().__init__()
        self.mlp = nn.Sequential(
            nn.Linear(d_h, d_h),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(d_h, d_h)
        )
        self.eps = nn.Parameter(torch.tensor([eps]))
        
    def forward(self, x: Tensor, e: Tensor, g: Tensor | None, edge_index: Tensor, batch: Tensor) -> tuple[Tensor, Tensor, Tensor | None]:
        src, dst = edge_index
        
        # GINE message computation: ReLU(x_j + e_ij)
        messages = torch.relu(x[src] + e)
        
        # Aggregate messages at destination nodes
        agg_messages = torch.zeros_like(x)
        agg_messages.scatter_add_(0, dst.unsqueeze(-1).expand_as(messages), messages)
        
        # Update node embeddings
        x_out = self.mlp((1 + self.eps) * x + agg_messages)
        
        # Return untouched edge and global features to maintain signature compatibility
        return x_out, e, g
