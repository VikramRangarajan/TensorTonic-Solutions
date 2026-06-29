import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    x = np.array(x)
    ps = np.array([1-p, p])
    return ps[x], p, p * (1 - p)