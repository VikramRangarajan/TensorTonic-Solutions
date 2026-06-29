import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.array(x)
    exp = np.exp(x)
    nexp = np.exp(-x)
    return (exp - nexp)/(exp + nexp)