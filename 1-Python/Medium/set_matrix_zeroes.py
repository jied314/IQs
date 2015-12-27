# 7/8 - Array
class SetMatrixZero:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.

    # Test on LeetCode 204ms
    # Memory - O(m+n)
    # Idea: record 0 columns and rows
    def set_zeroes(self, matrix):
        if matrix:
            columns, rows = set(), set()
            for i in range(0, len(matrix)):
                for j in range(0, len(matrix[0])):
                    if matrix[i][j] == 0:
                        rows.add(i)
                        columns.add(j)
            for j in columns:
                for i in range(0, len(matrix)):
                    matrix[i][j] = 0
            for i in rows:
                for j in range(0, len(matrix[0])):
                    matrix[i][j] = 0

    # Test on LeetCode 200ms
    # Memory - O(n)
    # Use first column and first row to record information
    def set_zeroes_constant_space(self, matrix):
        if matrix and matrix[0]:
            # check whether the first row and column has zeroes
            has_zero_in_first_row = False
            has_zero_in_first_column = False
            for j in range(0, len(matrix[0])):
                if matrix[0][j] == 0:
                    has_zero_in_first_row = True
            for i in range(0, len(matrix)):
                if matrix[i][0] == 0:
                    has_zero_in_first_column = True

            # record information in the first row and column
            for i in range(1, len(matrix)):
                for j in range(1, len(matrix[0])):
                    if matrix[i][j] == 0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0

            # set zeroes
            for i in range(1, len(matrix)):
                for j in range(1, len(matrix[0])):
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0

            # set zeroes in the first row and column if necessary
            if has_zero_in_first_row:
                for j in range(0, len(matrix[0])):
                    matrix[0][j] = 0
            if has_zero_in_first_column:
                for i in range(0, len(matrix)):
                    matrix[i][0] = 0

    # Test on LeetCode 184ms
    # Still two scans, however much shorter
    # Note:
    #   1. use one variable col0 to track zero in the first column
    #   2. the second scan is bottom-up fashion (top-down is wrong)
    def set_zeroes_constant_shorter(self, matrix):
        if matrix and matrix[0]:
            rows = len(matrix)
            columns = len(matrix[0])
            col0 = False  # track whether has 0
            for i in range(0, rows):
                if matrix[i][0] == 0:
                    col0 = True
                for j in range(1, columns):
                    if matrix[i][j] == 0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
            for i in range(rows-1, -1, -1):
                for j in range(columns-1, 0, -1):
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
                if col0:
                    matrix[i][0] = 0

