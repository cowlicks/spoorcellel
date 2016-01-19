## Update -- why this implementation won't work

The original naive design of spoorcellel sparse matrices was to use dask arrays to hold the internal data for sparse matrix datastructures.
For example a Compressed Sparse row matrix basically consists of 3 vectors:

 * nonzero data vector
 * Indices in the nonzero data vector of the start of the data in each row of the matrix (if this doesn't make sense don't worry about it)
 * the column index of each element in the nonzero data vector

Dask arrays carry around their shape as metadata, but not the value of every element in the array.
This is not calculated until `dask.array.compute` is called.

So suppose I add two CSR sparse matrices (with the same shape so this make sense).

What is the shape of the nonzero data vector dask array in the result?

Well, It depends on the location of the data in the input sparse matrices.
If two elements in the inputs matrices had the same location they could result in 1 or 0 nonzero elements in the output sparse matrix.
So, we have to inspect the location of all the data in input matrices, which requires computing the dask arrays in the input matrices.

I don't think this implementation can be useful if we can't do something as simple as add two spoorcellel sparse matrices without computing the intermediate dask arrays.

### Other implementations?

Maybe something like a dask.array, but a vector with arbitrary length could be used to represent vectors needed for sparse matrix datastructures.
Does this arbitrary length thing sound like "streaming" dask workflows other people have asked for?

<hr>

The stupid name "Spoorcellel" is some combination of the words "sparse", "parallel" and "ooc" (as in Out Of Core).

This is an experiment in how sparse matrices can be made out-of core and parallel.
The first step is to implement a good enough form of Compressed Sparse Row (CSR) format, and Coordinate list (COO) format.
Then to play with these to see what is useful, what is not.

CSR and COO were chosen mostly because in Scipy.sparse to go from any sparse matrix to a dense matrix, the code is basically `sparse_format.tocoo().toarray()`.
And these two formats together can applied to most problems.
