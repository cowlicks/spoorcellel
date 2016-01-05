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
