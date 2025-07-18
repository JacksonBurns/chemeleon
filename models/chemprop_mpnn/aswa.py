import torch
from torch.optim.swa_utils import AveragedModel, update_bn
from lightning.pytorch.callbacks import Callback


class ASWA(Callback):
    def __init__(
        self,
        monitor="val_loss",
        mode="min",
        swa_start=0,
        update_bn=True,
    ):
        """
        Args:
            monitor (str): Validation metric to track.
            mode (str): "min" if lower is better (e.g., for loss), "max" for accuracy.
            swa_start (int): Epoch to start applying ASWA.
            update_bn (bool): Whether to update BatchNorm statistics at the end.
        """
        super().__init__()
        self.monitor = monitor
        self.mode = mode
        self.swa_start = swa_start
        self.update_bn = update_bn

        self.best_score = float("inf") if mode == "min" else -float("inf")
        self.swa_model = None
        self.n_averaged = 0

    def _is_improvement(self, current):
        if self.mode == "min":
            return current < self.best_score
        return current > self.best_score

    def on_validation_end(self, trainer, pl_module):
        current_epoch = trainer.current_epoch
        metrics = trainer.callback_metrics

        if current_epoch < self.swa_start:
            return

        if self.monitor not in metrics:
            return

        current_score = metrics[self.monitor].item()
        if self._is_improvement(current_score):
            self.best_score = current_score
            self._update_swa_model(pl_module)

    def _update_swa_model(self, pl_module):
        device = pl_module.device

        if self.swa_model is None:
            self.swa_model = AveragedModel(pl_module, device=device)
        else:
            self.swa_model.update_parameters(pl_module)

        self.n_averaged += 1
        print(f"ASWA: Updated SWA weights (n={self.n_averaged})")

    def on_train_end(self, trainer, pl_module):
        if self.swa_model is None or self.n_averaged == 0:
            print("ASWA: No weights were averaged, skipping SWA swap.")
            return

        print(f"ASWA: Loading averaged weights into model (n={self.n_averaged})")
        pl_module.load_state_dict(self.swa_model.module.state_dict())

        if self.update_bn:
            print("ASWA: Updating BatchNorm statistics...")
            train_loader = trainer.train_dataloader
            update_bn(train_loader, pl_module)

    def state_dict(self):
        return {}

    def load_state_dict(self, state_dict):
        pass
