import operator
import dask.array as da
import numpy as np

from .coo import COO


def identity(n, chunks=(int(1e4),)):
    nzs = da.ones(n, chunks=chunks)
    nzi = da.arange(n + 1, chunks=chunks)
    ci = da.arange(n, chunks=chunks)
    shape = (n, n)
    return CSR(nzs, nzi, ci, shape)


def elemwise_on_nonzeros(self, op, other):
    """
    Elementwise operation that only effects nonzero values.  So op(0, other)
    must be 0.
    """
    return self.__class__(op(self.nonzeros, other),
                          self.nonzero_indices,
                          self.column_indices,
                          self.shape)


class CSR:
    def __init__(self, nzs, nzi, ci, shape):
        """
        nzs: nonzeros
        nzi: index in the nonzeros
        ci: column indices
        """
        self.nonzeros = nzs
        self.nonzero_indices = nzi
        self.column_indices = ci
        self.shape = shape

        self.nnz = len(self.nonzeros)

    def tocoo(self):
        """
        This must compute:
        self.nonzero_indicies

        Suggestions on avoiding computing this?
        """

        nzi = self.nonzero_indices.compute() # bad
        row_indices= np.empty(self.nnz) # also bad
        for i in range(self.nnz):
            for j in range(nzi[i], nzi[i + 1]):
                row_indices[j] = i

        return COO(self.nonzeros,
                   row_indices,
                   self.column_indices,
                   self.shape)

    def toarray(self):
        return self.tocoo().toarray()

    def __mul__(self, other):
        return elemwise_on_nonzeros(self, operator.mul, other)
