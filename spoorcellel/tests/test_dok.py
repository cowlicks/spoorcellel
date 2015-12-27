from __future__ import absolute_import
import pytest
from pdb import set_trace
from spoorcellel import dok
from itertools import product

"""
data_dict = {(i, j): v for (i, j), v in zip(product(range(0, 50, 10),
                                                    range(0, 60, 20)),
                                            range(15))}
"""
data_dict = {(10, 40): 5, (0, 0): 0, (30, 0): 9, (0, 20): 1, (30, 20): 10,
             (20, 20): 7, (30, 40): 11, (20, 0): 6, (40, 40): 14, (10, 20): 4,
             (20, 40): 8, (10, 0): 3, (0, 40): 2, (40, 0): 12, (40, 20): 13}


data_shape = (100, 60)
data = dok.DOK(data_dict, data_shape)



def test_int_index():
    assert 0 == data[(0, 0)]
    assert 13 == data[(40, 20)]

def test_slice_index():
    pass

@pytest.mark.xfail
def test_has_key():
    assert (40, 20) in data
