The stupid name "Spoorcellel" is some weird combination of the words "sparse", "parallel" and "ooc" (as in Out Of Core).

This is an experiment in how sparse matrices can be made out-of core and parallel.
The first step is to implement a good enough form of Compressed Sparse Row (CSR) format, and Coordinate list (COO) format.
Then to play with these to see what is useful, what is not.

CSR and COO were chosen mostly because in Scipy.sparse to go from any sparse matrix to a dense matrix, the code is basically `sparse_format.tocoo().toarray()`
