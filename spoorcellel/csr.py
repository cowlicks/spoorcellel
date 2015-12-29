class CSR:
    def __init__(self, nzs, nzi, ci, shape):
        """
        nzs: nonzeros
        nzi: index in the nonzeros
        ci: column indices
        """
        self.nonzeros = nzs
        self.nonzero_indices = nzs
        self.column_indices = ci
        self.shape = shape

    def scalar_elemwise(self, op, args):
        self.nonzeros = op(self.nonzeros, args)
        return self
