import numpy as np

def scale_rows(data: list, weights: list) -> np.ndarray:
    """
    Returns a float64 matrix with each row multiplied by its weight.
    """
    a=np.array(data,dtype=np.float64)
    b=np.array(weights,dtype=np.float64)

    return a*b[:,None]
