import numpy as np
from spoorcellel import coo
def test_coo_init():
    a = np.ones((10,))
    b = np.ones((10,))
    c = np.ones((10,))
    coo.COO(a, b, c, (10, 10))
