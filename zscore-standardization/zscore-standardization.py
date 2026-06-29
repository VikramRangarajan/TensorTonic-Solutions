import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.array(X)
    if X.ndim == 1:
        X = X[:, None]
    mean = X.mean(axis=axis, keepdims=True)
    std = X.std(axis=axis, keepdims=True)+eps
    return (X - mean) / std