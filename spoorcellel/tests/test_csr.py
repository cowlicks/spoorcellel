import numpy as np
import dask.array as da

from spoorcellel import csr

def test_toarray():
    # create 5x5 csr identity matrix
    nzs = da.from_array(np.ones(5), chunks=(5,))
    nzi = da.from_array(np.arange(6), chunks=(6,))
    ci = da.from_array(np.arange(5), chunks=(5,))
    shape = (5, 5)
    arr = csr.CSR(nzs, nzi, ci, shape)

    expected = np.identity(5)
    np.testing.assert_array_equal(arr.toarray(), expected)


def test_identity():
    expected = np.identity(10)
    result = csr.identity(10)
    np.testing.assert_array_equal(result.toarray(), expected)

def test_mul():
    expected = np.identity(10) * 5
    result = csr.identity(10) * 5
    np.testing.assert_array_equal(result.toarray(), expected)
