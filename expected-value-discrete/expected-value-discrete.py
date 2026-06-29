import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    p = np.array(p)
    if abs(p.sum() - 1) > 1e-6:
        raise ValueError()
    return np.dot(x, p)
