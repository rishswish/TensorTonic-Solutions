import numpy as np

def reshape_array(data: list, operation: str) -> np.ndarray:
    """
    Returns a float64 array with the shape selected by operation.
    """
    data=np.array(data,dtype=np.float64)
    if operation=='flatten':
        return data.flatten()
    if operation=='transpose':
        return data.T

    return np.expand_dims(data,axis=0)

        
