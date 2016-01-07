import numpy as np
import dask.array as da

from spoorcellel import csr

# create 5x5 csr identity matrix
nzs = da.from_array(np.ones(5), chunks=(5,))
nzi = da.from_array(np.arange(6), chunks=(6,))
ci = da.from_array(np.arange(5), chunks=(5,))
shape = (5, 5)

arr = csr.CSR(nzs, nzi, ci, shape)

def test_toarray():
    expected = np.identity(5)
    np.testing.assert_array_equal(arr.toarray(), expected)
