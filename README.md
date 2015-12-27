Spoorcellel is some weird combination of the words "sparse", "parallel" and "ooc" (as in Out Of Core.

Is there value in creating a sparse matrix datastructure which uses dask(array)?

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
