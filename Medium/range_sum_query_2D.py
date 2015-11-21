# 11/21 - DP
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner
# (row1, col1) and lower right corner (row2, col2).
# Note:
#   You may assume that the matrix does not change.
#   There are many calls to sumRegion function.
#   You may assume that row1 <= row2 and col1 <= col2.


# Idea:
#   only calculate the sum for the each row
#   sum the row up to the result. use dictionary.
# Error - List Index Out of Range at line 36???
class NumMatrix(object):
    sum_dict = {}
    matrix = []

    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        NumMatrix.sum_dict = {}
        if len(matrix) > 0:
            num_cols = len(matrix[0])
            for row in matrix:
                NumMatrix.matrix.append([row[0]])
                for i in range(1, num_cols):
                    NumMatrix.matrix[-1].append(row[i] + NumMatrix.matrix[-1][i-1])

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        str_region = self.get_string_representation(row1, col1, row2, col2)
        if str_region in NumMatrix.sum_dict:
            return NumMatrix.sum_dict[str_region]
        result = 0
        for row_num in range(row1, row2+1):
            result += NumMatrix.matrix[row_num][col2]
            if col1 > 0:
                result -= NumMatrix.matrix[row_num][col1-1]
        NumMatrix.sum_dict[str_region] = result
        return result

    def get_string_representation(self, row1, col1, row2, col2):
        return str(row1) + "." + str(col1) + " & " + str(row2) + "." + str(col2)


# Test on LeetCode - 72ms
# Idea:
#   Dynamic Programming
#   pre-calculate the sum and store in the matrix
class NumMatrixDP(object):
    matrix = []

    def __init__(self, matrix):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return

        num_rows, num_cols = len(matrix), len(matrix[0])
        NumMatrixDP.matrix = [[0 for i in range(0, num_cols+1)] for j in range(0, num_rows+1)]
        for i in range(1, num_rows+1):
            for j in range(1, num_cols+1):
                NumMatrixDP.matrix[i][j] = NumMatrixDP.matrix[i-1][j] + NumMatrixDP.matrix[i][j-1] - NumMatrixDP.matrix[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        return NumMatrixDP.matrix[row2+1][col2+1] - NumMatrixDP.matrix[row1][col2+1] - NumMatrixDP.matrix[row2+1][col1] + NumMatrixDP.matrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
numMatrix = NumMatrix([[3, 0, 1, 4, 2],
                       [5, 6, 3, 2, 1],
                       [1, 2, 0, 1, 5],
                       [4, 1, 0, 1, 7],
                       [1, 0, 3, 0, 5]])
print numMatrix.sumRegion(1, 1, 4, 4)
print numMatrix.sumRegion(1, 2, 3, 4)