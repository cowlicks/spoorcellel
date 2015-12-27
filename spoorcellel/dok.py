from chest import Chest
from itertools import product

def slice_to_indices(s):
    """
    >>> slice_to_indices(slice(0, 5, 2))
    (0, 2, 4)
    """
    return tuple(range(s.start, s.stop, s.step))

def get_chunk(dok, i_slice, j_slice):
    i_idxs = slice_to_indices(i_slice)
    j_idxs = slice_to_indices(j_slice)

    idxs = product(i_idxs, j_idxs)
    return {(i, j): dok(i, j) for i, j in idxs if dok.has_key((i, j))}



class DOK:
    def __init__(self, arg1, shape=None, chunksize=(int(1e4), int(1e4)),
                 dtype=None):
        if shape is None:
            raise ValueError('Demand shape for now')
        if not isinstance(arg1, dict):
            raise TypeError('support other things later')

        self.shape = shape
        self.chunksize = chunksize
        self.the_dict = Chest(arg1)

    def __getitem__(self, index):
        """If key=(i,j) is a pair of integers, return the corresponding
        element.  
        
        TODO:
        If either i or j is a slice or sequence, return a new sparse
        matrix with just these elements.

        MUSINGS ON THIS:
        How can we construct a new DOK in a parallel out of core way?

        We need to create a new Chest with elements of another, moving them through memory.
        This sounds like a perfect job for dask!
        """
        if ((isinstance(index, tuple)) and (len(index) == 2) and 
                (all(map(lambda x: isinstance(x, int), index)))):
            return self.the_dict[index]
        if isinstance(index, slice):
            pass

    def __contains__(self, key):
        return self.the_dict.__contains__(key)
