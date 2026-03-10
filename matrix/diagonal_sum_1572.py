class Solution:
    def diagonalSum(mat):
        row = len(mat)
        col = len(mat[0])
        sum = 0
        for i in range(row):
            for j in range(col):
                if i == j:
                    sum+=mat[i][j]
                if i+j == row-1:
                    sum+=mat[i][j]

        if row%2==1:
            ans = mat[row//2][row//2]
            sum -=ans
        return sum