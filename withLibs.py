# from numpy.linalg import matrix_rank
import numpy as np

mat_3x6 = [[2,3,4,5,6,-7],[18,9,0,1,2,3],[-4,-6,-8,-10,-12,14]]
A = np.array([[1,0,2],[2,-1,3],[4,1,8]])
mat_3x3_1 = [[1,0,0],[0,1,0],[0,0,0]]

# with open('inv_matrix(1000x1000).txt', 'r') as f:
#     A = np.array([[float(num) for num in line.split(', ')] for line in f])

rank = np.linalg.matrix_rank(A)

print("rank =",rank)

det = np.linalg.det(A)

if det:
    inv_A  = np.linalg.inv(A)
    print(np.matrix(inv_A))
    print("det =", det)
else:
    print("matrix has no inverse, det = ", det)