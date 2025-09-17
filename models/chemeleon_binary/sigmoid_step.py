import torch
import torch.nn as nn

class SigmoidStepSTE(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x):
        # compute sigmoid for backward use
        s = torch.sigmoid(x)
        ctx.save_for_backward(s)
        # forward: hard step
        return (s > 0.5).float()

    @staticmethod
    def backward(ctx, grad_output):
        (s,) = ctx.saved_tensors
        # backward: use derivative of sigmoid
        grad_input = grad_output * s * (1 - s)
        return grad_input


class SigmoidStep(nn.Module):
    """
    Forward: sigmoid(x) -> threshold at 0.5
    Backward: gradient as if sigmoid (straight-through trick)
    """
    def forward(self, x):
        return SigmoidStepSTE.apply(x)
