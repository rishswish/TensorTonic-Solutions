import numpy as np

def filter_and_extract(data: list, row_start: int, row_stop: int, threshold: float) -> np.ndarray:
    """
    Returns matching values in row-major order as a 1D float64 array.
    """
    data=np.array(data,dtype=np.float64)
    f_data=data[row_start:row_stop,:]
    rows,cols=f_data.shape
    ans=[]
    for i in range(rows):
        for j in range(cols):
            if f_data[i,j]>threshold:
                ans.append(f_data[i,j])

    return np.array(ans,dtype=np.float64)
