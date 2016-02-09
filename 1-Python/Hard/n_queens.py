# 1/13 - BackTracking
# The n-queens puzzle is the problem of placing n queens on an n * n chessboard such that no two queens attack each
# other. (no two are in the same row, column, or diagonal)
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.'
# both indicate a queen and an empty space respectively.
# For example,
#   There exist two distinct solutions to the 4-queens puzzle:
# [
#   [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#   ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]


class Solution(object):
    # Test on LC - 168ms, 54%
    # is_promising is the key function (used to prune the search space)
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ret = []
        self.queens(0, n, [0]*n, ret)
        puzzles = []
        for solution in ret:
            puzzles.append(self.build_puzzle(n, solution))
        return puzzles

    def queens(self, i, n, col, ret):
        if i == n:
            ret.append(list(col))
        else:
            for j in range(0, n):
                if self.is_promising(i, j, col):
                    col[i] = j
                    self.queens(i+1, n, col, ret)

    # check if current position [i, j] is promising
    # not on the same column and not diagonal
    def is_promising(self, i, j, col):
        k = 0
        flag = True
        while k < i and flag:
            if j == col[k] or i - k == abs(j - col[k]):
                flag = False
            k += 1
        return flag

    def build_puzzle(self, n, solution):
        puzzle = []
        for i in range(0, n):
            row = ["."] * n
            row[solution[i]] = "Q"
            puzzle.append(''.join(row))
        return puzzle

test = Solution()
print test.solveNQueens(4)