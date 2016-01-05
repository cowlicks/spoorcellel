import dask.array as da
import numpy as np


def fromarray(arr):
    row, col = arr.nonzero()
    data = arr[row, col]
    return COO(data, row, col, arr.shape)

class COO:
    def __init__(self, data, row, col, shape, chunks=None):
        self.data = da.from_array(data, chunks=(int(1e4),))
        self.row = da.from_array(row, chunks=(int(1e4),))
        self.col = da.from_array(col, chunks=(int(1e4),))
        self.shape = shape

    def toarray(self):
        out = np.zeros(self.shape)
        out[self.row.compute(), self.col.compute()] = self.data.compute()
        return out
