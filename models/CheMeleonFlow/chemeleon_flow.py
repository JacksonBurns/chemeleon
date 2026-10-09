"""CheMeleonFlow: scikit-learn compatible GP/kernel regressor + classifier
over frozen CheMeleon 2048-dim embeddings.

Drop-in alternative to TabularCheMeleonRegressor (Perceiver transformer) that
uses closed-form Gaussian Process inference instead. Cannot collapse to the
mean predictor. Supports:

  - RBF, Matérn-5/2, Spectral Mixture (MLE), Tanimoto(count-FP) kernels
  - SVD-whitened (Mahalanobis) or raw standardized feature space
  - Heteroscedastic (input-dependent) noise via IRWLS
  - Proper predictive variance -> calibrated uncertainty
  - SMILES input (batch CuikmolmakerMolGraphFeaturizer + frozen CheMeleon MPNN)
    or pre-computed (n, 2048) embeddings
  - Regression (predict, predict_with_uncertainty, score) and
    threshold-based classification (predict_classification, decision_function)

Based on: gp_explore.py results (GP_EXPLORE_REPORT.md).
  Default: RBF on auto-space (white if n<500, else raw) - robust
  with well-calibrated predictive uncertainty. Best point accuracy across the
  9 polaris comes from kernel-selection (beats TabICL v2 on 6/9, prior KRR on
  4/9): use "smk" for data-rich tasks (n>1000), "matern52" for data-scarce.
  SMK's MLE is fragile on very small data; Matérn interpolates near the
  training set (predictive std -> 0), so RBF is the safe all-round default.

Usage:
    from chemeleon_flow import CheMeleonFlowRegressor

    # From SMILES (featurizes internally with CheMeleon)
    reg = CheMeleonFlowRegressor(device="cuda")
    reg.fit(train_smiles, train_y)
    preds = reg.predict(test_smiles)
    preds, stds = reg.predict_with_uncertainty(test_smiles)

    # From pre-computed embeddings
    reg = CheMeleonFlowRegressor(kernel="matern52", space="white")
    reg.fit(X_train_2048, y_train)
    preds = reg.predict(X_test_2048)

    # Classification
    clf = CheMeleonFlowClassifier(threshold=5.0)
    clf.fit(train_smiles, train_y)
    prob_active, pred_class = clf.predict_classification(test_smiles)
"""
from __future__ import annotations

import warnings
from pathlib import Path
from typing import Literal, Optional, Tuple, Union

import numpy as np
from scipy import optimize
from scipy.stats import norm as norm_dist
from sklearn.base import BaseEstimator, ClassifierMixin, RegressorMixin

warnings.filterwarnings("ignore")

# ---------------------------------------------------------------------------
# Kernel primitives (shared with gp_explore.py, self-contained)
# ---------------------------------------------------------------------------

def _sq_dist(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    A2 = (A ** 2).sum(1)[:, None]
    B2 = (B ** 2).sum(1)[None, :]
    return np.clip(A2 + B2 - 2.0 * (A @ B.T), 0.0, None)


def _k_rbf(A, B, l):
    return np.exp(-_sq_dist(A, B) / (2.0 * l * l))


def _k_matern52(A, B, l):
    r = np.sqrt(_sq_dist(A, B))
    sr3 = r * np.sqrt(3.0) / l
    return (1.0 + sr3 + 0.5 * sr3 * sr3) * np.exp(-sr3)


def _k_smk(A, B, amps, widths):
    d2 = _sq_dist(A, B)
    K = np.zeros(d2.shape)
    for a, w in zip(amps, widths):
        K += a * np.exp(-w * d2)
    return K


def _k_tanimoto(A, B):
    """Tanimoto (Jaccard) on non-negative count vectors."""
    ab = A @ B.T
    aa = (A ** 2).sum(1)[:, None]
    bb = (B ** 2).sum(1)[None, :]
    denom = aa + bb - ab
    denom[denom == 0] = 1e-12
    return ab / denom


def _kernel_matrix(name, A, B, l=None, smk_params=None):
    if name == "rbf":
        return _k_rbf(A, B, l)
    if name == "matern52":
        return _k_matern52(A, B, l)
    if name == "smk":
        return _k_smk(A, B, smk_params["amps"], smk_params["widths"]) * smk_params["var"]
    if name == "tanimoto":
        return _k_tanimoto(A, B)
    raise ValueError(f"Unknown kernel: {name}")


def _median_pairwise_dist(X, cap=2000, seed=0):
    rng = np.random.default_rng(seed)
    n = X.shape[0]
    idx = rng.choice(n, size=min(n, cap), replace=False)
    Xs = X[idx]
    d2 = _sq_dist(Xs, Xs)
    iu = np.triu_indices(len(Xs), k=1)
    return float(np.median(np.sqrt(d2[iu])))


# ---------------------------------------------------------------------------
# SVD whitening
# ---------------------------------------------------------------------------

def _whiten_fit(X, rank_frac=0.999):
    mu = X.mean(0)
    Xc = X - mu
    U, s, Vt = np.linalg.svd(Xc, full_matrices=False)
    var = s ** 2
    cum = np.cumsum(var) / max(var.sum(), 1e-12)
    r = int(np.searchsorted(cum, rank_frac) + 1)
    r = max(1, min(r, len(s)))
    V = Vt[:r].T
    return V, s[:r], mu, r


def _whiten_apply(X, V, s, mu):
    return (X - mu) @ V / s


def _standardize_fit(X):
    mu = X.mean(0)
    sd = X.std(0).clip(min=1e-8)
    return mu, sd


def _standardize_apply(X, mu, sd):
    return (X - mu) / sd


# ---------------------------------------------------------------------------
# SMK marginal MLE
# ---------------------------------------------------------------------------

def _fit_smk(X, y, M=3, seed=0):
    dmed = _median_pairwise_dist(X)
    base_w = 1.0 / (2.0 * dmed * dmed)
    lw0 = np.log(np.array([base_w * f for f in [0.1, 1.0, 10.0][:M]]))
    la0 = np.full(M, np.log(1.0 / M))
    x0 = np.concatenate([la0, lw0, [0.0, 0.0]])

    def nll(p):
        amps = np.exp(p[:M])
        widths = np.exp(p[M:2 * M])
        noise = np.exp(p[2 * M])
        var = np.exp(p[2 * M + 1])
        K = _k_smk(X, X, amps, widths) * var + noise * np.eye(len(X))
        try:
            L = np.linalg.cholesky(K)
        except np.linalg.LinAlgError:
            return 1e10
        alpha = np.linalg.solve(L.T, np.linalg.solve(L, y))
        return 0.5 * y @ alpha + np.sum(np.log(np.diag(L))) + 0.5 * len(y) * np.log(2 * np.pi)

    res = optimize.minimize(nll, x0, method="L-BFGS-B",
                            options={"maxiter": 200, "gtol": 1e-5})
    p = res.x
    return {
        "amps": np.exp(p[:M]),
        "widths": np.exp(p[M:2 * M]),
        "noise": float(np.exp(p[2 * M])),
        "var": float(np.exp(p[2 * M + 1])),
    }


# ---------------------------------------------------------------------------
# GP solve (mean + variance)
# ---------------------------------------------------------------------------

def _gp_solve(K, y, noise):
    """Solve (K + noise*I)^{-1} y via Cholesky. Returns alpha, L."""
    A = K.copy()
    if np.isscalar(noise):
        A[np.diag_indices_from(A)] += noise
    else:
        A[np.diag_indices_from(A)] += noise
    try:
        L = np.linalg.cholesky(A)
        alpha = np.linalg.solve(L.T, np.linalg.solve(L, y))
        return alpha, L
    except np.linalg.LinAlgError:
        A += 1e-6 * np.eye(len(A))
        L = np.linalg.cholesky(A)
        alpha = np.linalg.solve(L.T, np.linalg.solve(L, y))
        return alpha, L


# ===========================================================================
# CheMeleonFlowRegressor
# ===========================================================================

class CheMeleonFlowRegressor(BaseEstimator, RegressorMixin):
    """
    Scikit-learn compatible GP regressor over frozen CheMeleon embeddings.

    Replaces the Perceiver transformer in TabularCheMeleonRegressor with
    closed-form Gaussian Process inference. Cannot collapse to the mean
    predictor. Provides calibrated predictive uncertainty.

    Parameters
    ----------
    kernel : {"rbf", "matern52", "smk", "tanimoto"}
        Kernel function. Default "rbf" (robust across data sizes with
        well-calibrated predictive uncertainty). Use "smk" for data-rich
        tasks (n>1000) for the best point accuracy; "matern52" for
        data-scarce tasks where a softer inductive bias helps. Note:
        "matern52" interpolates near training points (predictive std -> 0).
    space : {"raw", "white", "auto"}
        Feature space. "raw" = standardized. "white" = SVD-whitened
        (Mahalanobis). "auto" = white if n_train < 500, else raw.
        Default "auto".
    whiten_rank_frac : float
        Variance cutoff for SVD whitening (keep components until this
        fraction of total variance is captured). Default 0.999.
    smk_components : int
        Number of mixture components for the SMK. Default 3.
    lengthscale_frac : float
        RBF/Matérn lengthscale as a fraction of median pairwise distance.
        Default 1.0. (Ignored for SMK and Tanimoto.)
    noise : float
        Homoscedastic noise variance (in standardized-y space). Default 1e-2.
        (Overridden by SMK's MLE-fitted noise when kernel="smk".)
    heteroscedastic : bool
        If True, fit input-dependent noise via IRWLS (3 iterations).
        Default False (the GP_EXPLORE results showed no clear win).
    hetero_iters : int
        Number of IRWLS iterations for heteroscedastic noise. Default 3.
    device : str or torch.device
        Device for CheMeleon featurization (when input is SMILES).
        Default "cuda" if available, else "cpu".
    embed_type : {"full", "autoencoded"}
        CheMeleon embedding type. Default "full" (2048-dim).
    batch_size : int
        Batch size for SMILES featurization. Default 1024.
    """

    def __init__(
        self,
        kernel: Literal["rbf", "matern52", "smk", "tanimoto"] = "rbf",
        space: Literal["raw", "white", "auto"] = "auto",
        whiten_rank_frac: float = 0.999,
        smk_components: int = 3,
        lengthscale_frac: float = 1.0,
        noise: float = 1e-2,
        heteroscedastic: bool = False,
        hetero_iters: int = 3,
        device: Optional[Union[str, object]] = None,
        embed_type: Literal["full", "autoencoded"] = "full",
        batch_size: int = 1024,
    ):
        self.kernel = kernel
        self.space = space
        self.whiten_rank_frac = whiten_rank_frac
        self.smk_components = smk_components
        self.lengthscale_frac = lengthscale_frac
        self.noise = noise
        self.heteroscedastic = heteroscedastic
        self.hetero_iters = hetero_iters
        self.device = device
        self.embed_type = embed_type
        self.batch_size = batch_size

        # Fitted state (set by fit())
        self.is_fitted_ = False
        self.X_space_: Optional[np.ndarray] = None
        self.y_mean_: float = 0.0
        self.y_scale_: float = 1.0
        self.y_: Optional[np.ndarray] = None
        self.alpha_: Optional[np.ndarray] = None
        self.L_: Optional[np.ndarray] = None
        self.K_: Optional[np.ndarray] = None
        self.kernel_params_: dict = {}
        self.space_meta_: dict = {}
        self._embedder = None

    # ------------------------------------------------------------------
    # Featurization (CuikmolmakerMolGraphFeaturizer + frozen CheMeleon MPNN)
    # ------------------------------------------------------------------

    def _get_embedder(self):
        if self._embedder is None:
            import torch
            from featurize import CheMeleonEmbedder
            dev = self.device if self.device else (
                "cuda" if torch.cuda.is_available() else "cpu"
            )
            self._embedder = CheMeleonEmbedder(device=dev, type=self.embed_type)
        return self._embedder

    def _featurize(self, X) -> np.ndarray:
        """Convert SMILES list to (n, 2048) CheMeleon embeddings."""
        if isinstance(X, (list, tuple)) and len(X) > 0 and isinstance(X[0], str):
            import torch
            embedder = self._get_embedder()
            chunks = []
            for i in range(0, len(X), self.batch_size):
                batch = X[i:i + self.batch_size]
                emb = embedder(batch).to("cpu").float()
                chunks.append(emb)
                torch.cuda.empty_cache()
            return torch.cat(chunks, dim=0).numpy().astype("float64")
        return np.asarray(X, dtype="float64")

    # ------------------------------------------------------------------
    # sklearn interface
    # ------------------------------------------------------------------

    def fit(self, X, y):
        """
        Fit the GP on training data.

        Parameters
        ----------
        X : array-like of shape (n, 2048) or list of str
            CheMeleon embeddings or SMILES strings.
        y : array-like of shape (n,)
            Target values.
        """
        X = self._featurize(X)
        y = np.asarray(y, dtype="float64").ravel()
        n = len(y)

        if X.shape[0] != n:
            raise ValueError(f"X has {X.shape[0]} rows, y has {n} values")

        # Target standardization
        self.y_mean_ = float(y.mean())
        std = float(y.std())
        self.y_scale_ = std if std > 1e-8 else 1.0
        y_s = (y - self.y_mean_) / self.y_scale_

        # Feature space
        space = self.space
        if space == "auto":
            space = "white" if n < 500 else "raw"
        self.space_meta_["resolved"] = space

        if space == "white":
            V, s, mu, r = _whiten_fit(X, self.whiten_rank_frac)
            self.space_meta_["V"] = V
            self.space_meta_["s"] = s
            self.space_meta_["mu"] = mu
            self.space_meta_["rank"] = r
            X_space = _whiten_apply(X, V, s, mu)
        else:
            mu, sd = _standardize_fit(X)
            self.space_meta_["mu"] = mu
            self.space_meta_["sd"] = sd
            X_space = _standardize_apply(X, mu, sd)

        self.X_space_ = X_space
        self.y_ = y_s

        # Kernel fit
        self._fit_kernel(X_space, y_s)

        self.is_fitted_ = True
        return self

    def _fit_kernel(self, X, y_s):
        """Fit kernel hyperparameters and solve the GP linear system."""
        n = len(y_s)

        if self.kernel == "smk":
            params = _fit_smk(X, y_s, M=self.smk_components)
            self.kernel_params_ = params
            K = _k_smk(X, X, params["amps"], params["widths"]) * params["var"]
            noise = params["noise"]
        elif self.kernel == "tanimoto":
            self.kernel_params_ = {"noise": self.noise}
            K = _k_tanimoto(X, X)
            noise = self.noise
        else:
            dmed = _median_pairwise_dist(X)
            l = self.lengthscale_frac * dmed
            self.kernel_params_ = {"l": l, "noise": self.noise}
            K = _kernel_matrix(self.kernel, X, X, l=l)
            noise = self.noise

        # Heteroscedastic noise (IRWLS)
        sigma2 = noise
        if self.heteroscedastic:
            sigma2 = self._fit_heteroscedastic(X, y_s, noise)

        self.K_ = K
        self.alpha_, self.L_ = _gp_solve(K, y_s, sigma2)
        self.kernel_params_["noise_fit"] = float(sigma2) if np.isscalar(sigma2) else None

    def _fit_heteroscedastic(self, X, y_s, init_noise):
        """IRWLS: fit log-sigma2 = w^T [x, 1] by ridge, iterate."""
        sigma2 = np.full(len(y_s), float(init_noise))
        for _ in range(self.hetero_iters):
            if self.kernel == "smk":
                K = _k_smk(X, X, self.kernel_params_["amps"],
                           self.kernel_params_["widths"]) * self.kernel_params_["var"]
            else:
                K = _kernel_matrix(self.kernel, X, X, l=self.kernel_params_.get("l"))
            alpha, _ = _gp_solve(K, y_s, sigma2)
            train_pred = K @ alpha
            resid2 = np.maximum((y_s - train_pred) ** 2, 1e-10)
            Z = np.column_stack([X, np.ones(len(X))])
            lam = 1e-2 * Z.shape[1]
            w = np.linalg.solve(Z.T @ Z + lam * np.eye(Z.shape[1]),
                                Z.T @ np.log(resid2))
            sigma2 = np.exp(Z @ w)
            sigma2 = np.clip(sigma2, 1e-6, None)
        return sigma2

    # ------------------------------------------------------------------
    # Prediction
    # ------------------------------------------------------------------

    def _to_space(self, X) -> np.ndarray:
        """Transform input to the fitted feature space."""
        X = self._featurize(X)
        meta = self.space_meta_
        if meta["resolved"] == "white":
            return _whiten_apply(X, meta["V"], meta["s"], meta["mu"])
        else:
            return _standardize_apply(X, meta["mu"], meta["sd"])

    def _predict_core(self, X_space):
        """GP predictive mean + variance in standardized-y space."""
        kp = self.kernel_params_
        if self.kernel == "smk":
            Ks = _k_smk(X_space, self.X_space_, kp["amps"], kp["widths"]) * kp["var"]
            K_ii = kp["var"] * np.sum(kp["amps"])  # k(x,x) for SMK
        elif self.kernel == "tanimoto":
            Ks = _k_tanimoto(X_space, self.X_space_)
            K_ii = 1.0  # Tanimoto(x,x) = 1
        else:
            l = kp["l"]
            Ks = _kernel_matrix(self.kernel, X_space, self.X_space_, l=l)
            K_ii = 1.0  # RBF/Matérn(x,x) = 1

        # mean = Ks @ alpha
        mean_s = Ks @ self.alpha_

        # var = k(x,x) - k(x,X)^T (K+noise I)^{-1} k(x,X)
        #     = k(x,x) - ||L^{-1} k(x,X)||^2   where K+noise I = L L^T
        W = np.linalg.solve(self.L_, Ks.T)  # (n_train, n_test); col i = L^{-1} k(x*_i, X)
        var_s = K_ii - np.sum(W * W, axis=0)  # (n_test,)
        var_s = np.clip(var_s, 1e-12, None)

        return mean_s, var_s

    def predict(self, X) -> np.ndarray:
        """Predict target values."""
        if not self.is_fitted_:
            raise RuntimeError("Model is not fitted. Call fit(X, y) first.")
        X_space = self._to_space(X)
        mean_s, _ = self._predict_core(X_space)
        return mean_s * self.y_scale_ + self.y_mean_

    def predict_with_uncertainty(self, X) -> Tuple[np.ndarray, np.ndarray]:
        """
        Predict target values with predictive standard deviations.

        Returns
        -------
        mean : (n,) array - predicted values
        std : (n,) array - predictive standard deviations
        """
        if not self.is_fitted_:
            raise RuntimeError("Model is not fitted. Call fit(X, y) first.")
        X_space = self._to_space(X)
        mean_s, var_s = self._predict_core(X_space)
        mean = mean_s * self.y_scale_ + self.y_mean_
        std = np.sqrt(var_s) * self.y_scale_
        return mean, std

    def decision_function(self, X) -> np.ndarray:
        """
        Predictive mean (in original y-scale) + 1/std (confidence weight).
        For classifier use: higher = more confidently positive.
        """
        if not self.is_fitted_:
            raise RuntimeError("Model is not fitted. Call fit(X, y) first.")
        X_space = self._to_space(X)
        mean_s, var_s = self._predict_core(X_space)
        mean = mean_s * self.y_scale_ + self.y_mean_
        std = np.sqrt(np.clip(var_s, 1e-12, None)) * self.y_scale_
        return mean / (std + 1e-12)

    def score(self, X, y, sample_weight=None) -> float:
        """R² score."""
        y_pred = self.predict(X)
        y = np.asarray(y, dtype="float64").ravel()
        sw = np.asarray(sample_weight, dtype="float64") if sample_weight is not None else np.ones(len(y))
        ss_res = np.sum(sw * (y - y_pred) ** 2)
        y_mean_w = np.sum(sw * y) / np.sum(sw)
        ss_tot = np.sum(sw * (y - y_mean_w) ** 2)
        if ss_tot < 1e-8:
            return 0.0
        return float(1.0 - ss_res / ss_tot)

    def fit_predict(self, X_context, y_context, X_query) -> np.ndarray:
        self.fit(X_context, y_context)
        return self.predict(X_query)


# ===========================================================================
# CheMeleonFlowClassifier
# ===========================================================================

class CheMeleonFlowClassifier(BaseEstimator, ClassifierMixin):
    """
    Scikit-learn compatible GP classifier over frozen CheMeleon embeddings.

    Wraps a CheMeleonFlowRegressor and performs threshold-based binary
    classification using the GP predictive distribution:

        P(y > threshold) = 1 - Φ((threshold - μ) / σ)

    where Φ is the standard normal CDF, μ and σ are the GP predictive
    mean and std. This gives calibrated probabilities, not just hard labels.

    Parameters
    ----------
    threshold : float
        Decision threshold in the original y-scale. Predictions above this
        are class 1 (active), below are class 0 (inactive). Default 0.0.
    kernel, space, whiten_rank_frac, smk_components, lengthscale_frac,
    noise, heteroscedastic, hetero_iters, device, embed_type, batch_size :
        Passed through to CheMeleonFlowRegressor. See its docstring.
    """

    def __init__(
        self,
        threshold: float = 0.0,
        kernel: Literal["rbf", "matern52", "smk", "tanimoto"] = "rbf",
        space: Literal["raw", "white", "auto"] = "auto",
        whiten_rank_frac: float = 0.999,
        smk_components: int = 3,
        lengthscale_frac: float = 1.0,
        noise: float = 1e-2,
        heteroscedastic: bool = False,
        hetero_iters: int = 3,
        device: Optional[Union[str, object]] = None,
        embed_type: Literal["full", "autoencoded"] = "full",
        batch_size: int = 1024,
    ):
        self.threshold = threshold
        self.kernel = kernel
        self.space = space
        self.whiten_rank_frac = whiten_rank_frac
        self.smk_components = smk_components
        self.lengthscale_frac = lengthscale_frac
        self.noise = noise
        self.heteroscedastic = heteroscedastic
        self.hetero_iters = hetero_iters
        self.device = device
        self.embed_type = embed_type
        self.batch_size = batch_size

        self.is_fitted_ = False
        self.classes_ = np.array([0, 1])
        self._reg = CheMeleonFlowRegressor(
            kernel=kernel,
            space=space,
            whiten_rank_frac=whiten_rank_frac,
            smk_components=smk_components,
            lengthscale_frac=lengthscale_frac,
            noise=noise,
            heteroscedastic=heteroscedastic,
            hetero_iters=hetero_iters,
            device=device,
            embed_type=embed_type,
            batch_size=batch_size,
        )

    def fit(self, X, y):
        """
        Fit the GP classifier.

        Parameters
        ----------
        X : array-like of shape (n, 2048) or list of str
            CheMeleon embeddings or SMILES.
        y : array-like of shape (n,)
            Continuous target values (the threshold is applied at predict time).
            For binary y in {0, 1}, the threshold defaults to 0.5.
        """
        y = np.asarray(y, dtype="float64").ravel()
        # Auto-set threshold for binary labels
        if self.threshold == 0.0 and set(np.unique(y)).issubset({0, 1}):
            self.threshold = 0.5
        self._reg.fit(X, y)
        self.is_fitted_ = True
        return self

    def predict_proba(self, X) -> np.ndarray:
        """
        Predict class probabilities.

        Returns
        -------
        (n, 2) array : [P(class 0), P(class 1)]
        """
        if not self.is_fitted_:
            raise RuntimeError("Model is not fitted. Call fit(X, y) first.")
        mean, std = self._reg.predict_with_uncertainty(X)
        # P(y > threshold) = 1 - Φ((threshold - mean) / std)
        z = (self.threshold - mean) / (std + 1e-12)
        p_active = 1.0 - norm_dist.cdf(z)
        p_active = np.clip(p_active, 1e-7, 1.0 - 1e-7)
        return np.column_stack([1.0 - p_active, p_active])

    def predict(self, X) -> np.ndarray:
        """Predict class labels (0 or 1)."""
        proba = self.predict_proba(X)
        return (proba[:, 1] >= 0.5).astype(int)

    def predict_classification(self, X) -> Tuple[np.ndarray, np.ndarray]:
        """
        Predict (P(active), class_label) - matches TabularCheMeleonRegressor API.
        """
        proba = self.predict_proba(X)
        p_active = proba[:, 1]
        pred_class = (p_active >= 0.5).astype(int)
        return p_active, pred_class

    def decision_function(self, X) -> np.ndarray:
        """log-odds of P(active)."""
        proba = self.predict_proba(X)
        p = np.clip(proba[:, 1], 1e-7, 1.0 - 1e-7)
        return np.log(p / (1.0 - p))

    def score(self, X, y, sample_weight=None) -> float:
        """Accuracy."""
        y = np.asarray(y).ravel()
        sw = np.asarray(sample_weight, dtype="float64") if sample_weight is not None else np.ones(len(y))
        if set(np.unique(y)).issubset({0, 1}):
            pred = self.predict(X)
            correct = (pred == y).astype(float)
            return float(np.sum(sw * correct) / np.sum(sw))
        y_pred = (self.predict(X) == 1).astype(float)
        y_true = (y >= self.threshold).astype(float)
        correct = (y_pred == y_true).astype(float)
        return float(np.sum(sw * correct) / np.sum(sw))

    def fit_predict(self, X_context, y_context, X_query) -> np.ndarray:
        self.fit(X_context, y_context)
        return self.predict(X_query)
