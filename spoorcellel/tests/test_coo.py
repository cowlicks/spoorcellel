import numpy as np
from spoorcellel import coo
def test_coo_init():
    a = np.ones((10,))
    b = np.ones((10,))
    c = np.ones((10,))
    coo.COO(a, b, c, (10, 10))

def test_coo_fromarray():
    a = np.arange(100).reshape(10, 10)
    res = coo.fromarray(a)
    assert res.shape == (10, 10)

def test_coo_toarray():
    a = np.arange(100).reshape(10, 10)
    b = coo.fromarray(a)
    np.testing.assert_array_equal(b.toarray(), a)
