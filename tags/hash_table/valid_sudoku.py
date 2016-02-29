# 2/20 - Easy, Hash Table
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# Note:
#   A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.


class Solution(object):
    # Idea:
    #   Predefined set to store values.
    #   Mark each value in the set.
    def is_valid_sudoku_nice(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return False

        rows = [[False for _ in range(9)] for __ in range(0, 9)]
        columns = [[False for _ in range(9)] for __ in range(0, 9)]
        blocks = [[False for _ in range(9)] for __ in range(0, 9)]

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    continue
                c = ord(board[i][j]) - ord("1")
                block_index = (i/3) * 3 + j/3
                if rows[i][c] or columns[j][c] or blocks[block_index][c]:
                    return False
                rows[i][c] = True
                columns[j][c] = True
                blocks[block_index][c] = True
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return False

        for i in range(0, 9):
            if not self.is_valid_row(board, i):
                return False

        for j in range(0, 9):
            if not self.is_valid_column(board, j):
                return False

        for i in range(0, 3):
            for j in range(0, 3):
                if not self.is_valid_square(board, i*3, j*3):
                    return False
        return True

    def is_valid_row(self, board, row_index):
        row = board[row_index]
        uniques = set()
        for e in row:
            if e == ".":
                continue
            if e in uniques:
                return False
            uniques.add(e)
        return True

    def is_valid_column(self, board, column_index):
        column = [row[column_index] for row in board]
        uniques = set()
        for e in column:
            if e == ".":
                continue
            if e in uniques:
                return False
            uniques.add(e)
        return True

    def is_valid_square(self, board, i, j):
        ii = (i, i+1, i+2)
        jj = (j, j+1, j+2)
        uniques = set()
        for k in ii:
            for l in jj:
                if board[k][l] == ".":
                    continue
                e = board[k][l]
                if e in uniques:
                    return False
                uniques.add(e)
        return True
