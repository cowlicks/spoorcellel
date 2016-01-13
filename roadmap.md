This is currently full of random thoughts and notes. It is a mess and notes are out of date.

# Yale

Conside yale format sparse matrix datastructures, they consist of three rows.
Two are of length NNZ, the other is of length m + 1.
Where NNZ is the number of non-zero entries, and m is the number of rows in the matrix.

Perhaps each of the rows in a yale datastructure could be a dask.array.

# Creation formats

We could use mrocklin's chest to implement an ooc DOK datastructure. Would we even need dask?

Actually yeah, it seems so.
If we slice a DOK we can use dask to move elements from one Chest into a new one which we then return.

We can use a "chunksize" here similiar to dask array.
Each task should pull one "chunk" out of the chest and update the new one with it.

# commonalities in formats

COO and CSR/CSC each have three vector like things that store data.
COO and CSR are similiar and useful.
Implementing both of these would provide a nice first pass prototype.

# implement basic coo and csr

These are frequently used together and useful.

## first steps with coo and csr

Implementing coo.toarray and fromarray is handy because it easily allows us to construct and test.
This is done.
So next I should create csr.tocoo, then csr.from/toarray will use this.
Once this is done I can add some elementwise methods to csr.

### csr.tocoo

The nnz and column indices come for free.
But we need to extract the row indices.
In scipy sparse this is done in `_sparsetools.expandptr`

# array creation

Should it be the responsibility of the matrix constructor to create the dask.array?
Or should the, caller of the constructor do this?

# triggering computation

Some functions trigger computation, like `CSR.tocoo`, should the user be informed about this?
If so how?
What are the circumstances where triggering computation is necessary?

# metadata

The arrays should pass around the same data that dask.arrays have pluse dtype.
And possibly nnz.
nnz should be optional, and default to one or something.
If we were to add to spoorcellel arrays we don't know where the data overlaps without computing them.
So we can't always know this.
We would know the bounds of nnz. For addition it would be self.nnz +/- other.nnz
