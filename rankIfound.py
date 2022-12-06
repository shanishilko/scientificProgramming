from time import time

# Python 3 program to find rank of a matrix
class rankMatrix(object):
    def __init__(self, Matrix):
        self.R = len(Matrix)
        self.C = len(Matrix[0])

    # Function for exchanging two rows of a matrix
    def swap(self, Matrix, row1, row2, col):
        for i in range(col):
            temp = Matrix[row1][i]
            Matrix[row1][i] = Matrix[row2][i]
            Matrix[row2][i] = temp

    # Function to Display a matrix
    def Display(self, Matrix, row, col):
        for i in range(row):
            for j in range(col):
                print(" " + str(Matrix[i][j]))
            print('\n')

    # Find rank of a matrix
    def rankOfMatrix(self, Matrix):
        rank = self.C
        for row in range(0, rank, 1):

            # Before we visit current row
            # 'row', we make sure that
            # mat[row][0],....mat[row][row-1]
            # are 0.

            # Diagonal element is not zero
            if Matrix[row][row] != 0:
                for col in range(0, self.R, 1):
                    if col != row:

                        # This makes all entries of current
                        # column as 0 except entry 'mat[row][row]'
                        multiplier = (Matrix[col][row] /
                                      Matrix[row][row])
                        for i in range(rank):
                            Matrix[col][i] -= (multiplier *
                                               Matrix[row][i])

            # Diagonal element is already zero.
            # Two cases arise:
            # 1) If there is a row below it
            # with non-zero entry, then swap
            # this row with that row and process
            # that row
            # 2) If all elements in current
            # column below mat[r][row] are 0,
            # then remove this column by
            # swapping it with last column and
            # reducing number of columns by 1.
            else:
                reduce = True

                # Find the non-zero element
                # in current column
                for i in range(row + 1, self.R, 1):

                    # Swap the row with non-zero
                    # element with this row.
                    if Matrix[i][row] != 0:
                        self.swap(Matrix, row, i, rank)
                        reduce = False
                        break

                # If we did not find any row with
                # non-zero element in current
                # column, then all values in
                # this column are 0.
                if reduce:

                    # Reduce number of columns
                    rank -= 1

                    # copy the last column here
                    for i in range(0, self.R, 1):
                        Matrix[i][row] = Matrix[i][rank]

                # process this row again
                row -= 1

        # self.Display(Matrix, self.R,self.C)
        return (rank)


# Driver Code
if __name__ == '__main__':
    # Matrix = [[1,0,0],[0,1,0],[0,0,0]]

    with open('inv_matrix(1000x1000).txt', 'r') as f:
        Matrix = [[float(num) for num in line.split(', ')] for line in f]

    tt = time()
    RankMatrix = rankMatrix(Matrix)
    print("Rank of the Matrix is:",
          (RankMatrix.rankOfMatrix(Matrix)))
    print("Time = ", time() - tt)

# This code is contributed by Vikas Chitturi
