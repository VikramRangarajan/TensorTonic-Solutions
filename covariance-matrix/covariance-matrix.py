import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.array(X)
    if X.shape[0] <= 1 or X.ndim <= 1:
        return None
    X = X - X.mean(axis=0, keepdims=True)
    return X.T @ X / (X.shape[0] - 1)