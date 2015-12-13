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
#   Use BFS - since stack may overflow
# Note:
#   special cases - need to do boundary check (crucial)
#
class SurroundedRegions(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0 or len(board) == 1 or len(board[0]) == 1:
            return
        self.visit_side_zeros(board)
        self.fill_xs(board)

    # DFS - visit all zeros that are connected to zeros on boarders
    def visit_side_zeros(self, board):
        num_rows = len(board)
        num_cols = len(board[0])
        i, j = 0, 0
        in_visit = True
        while in_visit:
            # first row
            if i == 0 and j < num_cols - 1:
                if board[i][j] == 'O':
                    self.visit_connecting_zeros(i, j, board, num_rows, num_cols)
                j += 1
            # last column
            elif j == num_cols - 1 and i < num_rows - 1:
                if board[i][j] == 'O':
                    self.visit_connecting_zeros(i, j, board, num_rows, num_cols)
                i += 1
            # last row
            elif i == num_rows - 1 and j > 0:
                if board[i][j] == 'O':
                    self.visit_connecting_zeros(i, j, board, num_rows, num_cols)
                j -= 1
            # first column
            elif j == 0 and i > 0:
                if board[i][j] == 'O':
                    self.visit_connecting_zeros(i, j, board, num_rows, num_cols)
                i -= 1
            if i == 0 and j == 0:
                in_visit = False

    # change connecting Os to 1s
    def visit_connecting_zeros(self, i, j, board, num_rows, num_cols):
        in_visit = [[i, j]]
        while len(in_visit) > 0:
            cell = in_visit.pop()
            ii, jj = cell[0], cell[1]
            if board[ii][jj] == 'O':  # has not visited
                board[ii] = board[ii][:jj] + '1' + board[ii][jj+1:]  # update array, '0' -> '1'
                # expand if possible
                if ii > 0 and board[ii-1][jj] == 'O':  # top
                    in_visit.append([ii-1, jj])
                if ii + 1 < num_rows and board[ii+1][jj] == 'O':  # bottom
                    in_visit.append([ii+1, jj])
                if jj > 0 and board[ii][jj-1] == 'O':  # left
                    in_visit.append([ii, jj-1])
                if jj + 1 < num_cols and board[ii][jj+1] == 'O':  # right
                    in_visit.append([ii, jj+1])

    # change the rest Os to Xs, and 1s to Os
    def fill_xs(self, board):
        num_rows = len(board)
        num_cols = len(board[0])
        for i in range(0, num_rows):
            for j in range(0, num_cols):
                if board[i][j] == '1':
                    board[i] = board[i][:j] + 'O' + board[i][j+1:]
                elif board[i][j] == 'O':
                    board[i] = board[i][:j] + 'X' + board[i][j+1:]

test = SurroundedRegions()
board = ["OO","OO"]
#board = ["X"]
test.solve(board)
print board
