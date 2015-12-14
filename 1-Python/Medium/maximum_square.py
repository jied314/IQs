# 10/24 - DP (M)
# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and
# return its area.
# For example, given the following matrix:
#   1 0 1 0 0
#   1 0 1 1 1
#   1 1 1 1 1
#   1 0 0 1 0
# Return 4.

class MaximalSquare(object):
    # Test on LeetCode - 392ms
    # Idea:
    #   for each cell, count its maximal, then move to the next.
    # O(M*N*M*N) Time, O(1) Space
    def maximal_square(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix is None or len(matrix) == 0:
            return 0
        maximum_side = 0

        m, n = len(matrix), len(matrix[0])
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == "1":
                    cur_side = self.count_square(matrix, i, j, m, n)
                    maximum_side = max(maximum_side, cur_side)
        return maximum_side * maximum_side

    # count the maximal square for current cell
    def count_square(self, matrix, i, j, m, n):
        ii, jj, step = i, j, 1
        while jj + step < n and matrix[i][jj + step] == "1" and ii + step < m and matrix[ii + step][j] == "1":
            if self.verify_right_bottom_square(matrix, i, j, step):
                step += 1
            else:
                break
        return step

    # verify the right bottom cells are all 1s
    def verify_right_bottom_square(self, matrix, i, j, step):
        for ii in range(i + 1, i + 1 + step):
            if matrix[ii][j + step] == "0":
                return False
        for jj in range(j + 1, j + step):
            if matrix[i + step][jj] == "0":
                return False
        return True

    # Dynamic Programming - O(M*N) time, O(M*N) space
    # 1. i == 0: P[0][j] = matrix[0][j] (topmost row);
    # 2. j == 0: P[i][0] = matrix[i][0] (leftmost column);
    # 3. For i > 0 and j > 0: if matrix[i][j] = 0, P[i][j] = 0;
    #    if matrix[i][j] = 1, P[i][j] = min(P[i - 1][j], P[i][j - 1], P[i - 1][j - 1]) + 1.
    # Improvement:
    #   1. instead of using O(M*N) space, use O(N) space. - use two vectors to store pre_row and cur_row
    #   2. use one row
    def maximal_square_dp(self, matrix):
        if matrix is not None and len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        ret = [[0] * n] * m
        maximum_side = 0
        for j in range(0, n):
            ret[0][j] = int(matrix[0][j])
            maximum_side = max(maximum_side, ret[0][j])
        for i in range(0, m):
            ret[i][0] = int(matrix[i][0])
            maximum_side = max(maximum_side, ret[i][0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    ret[i][j] = min(ret[i-1][j], ret[i][j-1], ret[i-1][j-1]) + 1
                    maximum_side = max(maximum_side, ret[i][j])
        return maximum_side * maximum_side


def main():
    test = MaximalSquare()
    matrix = [['1', '0', '1', '0', '0'],
              ['1', '0', '1', '1', '1'],
              ['1', '1', '1', '1', '1'],
              ['1', '0', '1', '1', '1']]
    print test.maximal_square(matrix)
    print test.maximal_square_dp(matrix)

if __name__ == '__main__':
    main()