import numpy as np

def normalize(data: list) -> np.ndarray:
    """
    Returns a float64 matrix standardized independently by column.
    """
    data=np.array(data,dtype=np.float64)
    col_mean=data.mean(axis=0)
    col_std=data.std(axis=0)

    normalized=(data-col_mean)/(col_std)

    return normalized
