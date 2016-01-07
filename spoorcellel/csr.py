import numpy as np

from .coo import COO

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
