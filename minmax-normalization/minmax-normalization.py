import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.array(X)
    if X.ndim == 1:
        X = X[:, None]
    xmin = np.min(X, axis=axis, keepdims=True)
    xmax = np.max(X, axis=axis, keepdims=True)
    diff = xmax - xmin
    diff = np.where(diff < eps, float("inf"), diff)
    return (X - xmin)/diff