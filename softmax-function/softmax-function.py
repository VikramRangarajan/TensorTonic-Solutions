import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.array(x)
    reduce = x.ndim == 1
    if reduce:
        x = x[None]
    x = x - x.max(axis=1, keepdims=True)
    exp = np.exp(x)
    x = exp / exp.sum(axis=1, keepdims=True)
    if reduce: return x[0]
    return x