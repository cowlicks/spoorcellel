import dask.array as da


class COO:
    def __init__(self, data, row, col, shape, chunks=None):
        self.data = da.from_array(data, chunks=(int(1e4),))
        self.row = da.from_array(row, chunks=(int(1e4),))
        self.col = da.from_array(col, chunks=(int(1e4),))
