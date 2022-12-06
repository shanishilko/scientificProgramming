import numpy as np


D = 1
# A = np.array([[1,2,3], [4,5,6], [7,8,9]])
A = np.array([[1,0,2],[2,-1,3],[4,1,8]])
# inv is  [[-11,2,2],[-4,0,1],[6,1,1]]

rows_num = A.shape[0]
cols_num = A.shape[1]

Id_mat_to_A_inverse  = np.identity(rows_num)


a = (A[0, 0] / A[:, 0]).reshape(-1,1)

D *= np.prod(a)

B = A * a       # multiplies each number in col with a col
B[1:, :] -= B[0, :]


print(B)
print(D)

