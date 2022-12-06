import numpy as np
from time import time

# matrix to find inverse
# A = np.array([[1, 0, 1], [0, 1, 1], [1, 1, 1]])

# with open('inv_matrix(1000x1000).txt', 'r') as f:
#     A = np.array([[float(num) for num in line.split(', ')] for line in f])
det=1
A = np.array([[1,0,2],[2,-1,3],[4,1,8]])

n= A.shape[0]
# identity matrix with same shape as A
I = np.identity(n=n)

# form the augmented matrix by concatenating A and I
M = np.concatenate((A, I), axis=1)
tt = time()
# iterate over matrix rows
for i in range(0, n):

    # select pivot value
    pivot = M[i][i]
    det *= M[i][i]

    # extract row
    row = M[i]

    # get 1 along the diagonal
    M[i] = row / pivot

    # iterate over all rows except pivot to get augmented matrix into reduced row echelon form
    for j in [k for k in range(0, n) if k != i]:
        # subtract current row from remaining rows
        M[j] = M[j] - M[i] * M[j][i]
    # extract inverse matrix
    inverse = M[:, n:]
print("Time = ", time() - tt)
print(inverse)
print("det = ", det)