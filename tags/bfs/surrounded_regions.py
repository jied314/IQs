# 12/4 - BFS, Union Find
# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# For example,
#   X X X X
#   X O O X
#   X X O X
#   X O X X
# After running your function, the board should be:
#   X X X X
#   X X X X
#   X X X X
#   X O X X
# Revisit 12/12
#
# Idea:
#   start from Os on boarders, visit all connecting Os, make mark
#   then for the rest Os, change to Xs. The marked ones change back to Os.
#   Use BFS - since DFS stack may overflow
# Note:
#   special cases - need to do boundary check (crucial)
#
import collections


# 1/11 - Revisit
# Test on LC - 164ms 82%
class SurroundedRegions(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0 or len(board) == 1 or len(board[0]) == 1:
            return
        m, n = len(board), len(board[0])
        # visit all boarders
        for i in range(0, m):  # visit fist and last columns
            if board[i][0] == 'O':
                self.mark(board, i, 0)
            if board[i][n-1] == 'O':
                self.mark(board, i, n-1)
        for j in range(1, n-1):  # visit first and last rows
            if board[0][j] == 'O':
                self.mark(board, 0, j)
            if board[m-1][j] == 'O':
                self.mark(board, m-1, j)
        self.flip(board)

    # BFS - visit all zeros that are connected to zeros on boarders
    def mark(self, board, i, j):
        visit = collections.deque()
        visit.append([i, j])
        while len(visit) > 0:
            ii, jj = visit.popleft()
            if board[ii][jj] == 'O':
                board[ii][jj] = '1'
                if ii > 0 and board[ii-1][jj] == 'O':  # top
                    visit.append([ii-1, jj])
                if ii < len(board)-1 and board[ii+1][jj] == 'O':  # bottom
                    visit.append([ii+1, jj])
                if jj > 0 and board[ii][jj-1] == 'O':  # left
                    visit.append([ii, jj-1])
                if jj < len(board[0])-1 and board[ii][jj+1] == 'O':  # right
                    visit.append([ii, jj+1])

    # change the rest Os to Xs, and 1s to Os
    def flip(self, board):
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '1':
                    board[i][j] = 'O'

test = SurroundedRegions()
board = ["OO","OO"]
#board = ["X"]
test.solve(board)
print board
