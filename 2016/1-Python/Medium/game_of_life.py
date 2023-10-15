# 10/5 - Array (M)
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). 
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules 
# (taken from the above Wikipedia article):
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state.
#
# Follow up: 
# Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells
# first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems
# when the active area encroaches the border of the array. How would you address these problems?

class GameOfLife(object):
    # Test on LeetCode - 52ms
    def game_of_life(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        for i in range(0, m):  # each row
            for j in range(0, n):  # each column
                value = board[i][j] & 1
                live_count = self.count_live_neighbors(board, i, j, m, n)
                if (value and 3 >= live_count >= 2) or (value == 0 and live_count == 3):
                    board[i][j] += 2
        for i in range(0, m):
            for j in range(0, n):
                board[i][j] >>= 1

    # Note: how to construct [i,j], need to subtract self
    def count_live_neighbors(self, board, i, j, m, n):
        count = 0
        for I in range(max(i-1, 0), min(i+2, m)):
            for J in range(max(j-1, 0), min(j+2, n)):
                count += board[I][J] & 1
        count -= board[i][j]  # subtract self value
        return count

    # initial attempt, not complete!
    def count_live_neighbors_wrong(self, board, i, j, m, n):
        count = 0
        if m - 1 > i > 0 and n - 1 > j > 0:
            count += board[i - 1][j - 1] & 1
            count += board[i - 1][j] & 1
            count += board[i - 1][j + 1] & 1
            count += board[i][j - 1] & 1
            count += board[i][j + 1] & 1
            count += board[i + 1][j - 1] & 1
            count += board[i + 1][j] & 1
            count += board[i + 1][j + 1] & 1
        elif i == 0:  # no top
            if n - 1 > j > 0:  # middle
                count += board[i][j - 1] & 1
                count += board[i][j + 1] & 1
                if i < m - 1:  # count bottom
                    count += board[i + 1][j - 1] & 1
                    count += board[i + 1][j] & 1
                    count += board[i + 1][j + 1] & 1
            elif n - 1 > j == 0:  # left
                count += board[i][j + 1] & 1
                if i < m - 1:  # count bottom
                    count += board[i + 1][j] & 1
                    count += board[i + 1][j + 1] & 1
            else:  # right
                count += board[i][j - 1] & 1
                if i < m - 1:  # count bottom
                    count += board[i + 1][j] & 1
                    count += board[i + 1][j - 1] & 1
        else:  # no bottom
            if n - 1 > j > 0:
                count += board[i][j - 1] & 1
                count += board[i][j + 1] & 1
                if i > 0:  # count top
                    count += board[i - 1][j - 1] & 1
                    count += board[i - 1][j] & 1
                    count += board[i - 1][j + 1] & 1
            elif n - 1 > j == 0:
                count += board[i][j + 1] & 1
                if i > 0:  # count top
                    count += board[i - 1][j] & 1
                    count += board[i - 1][j + 1] & 1
            else:
                count += board[i][j - 1] & 1
                if i > 0:  # count top
                    count += board[i - 1][j] & 1
                    count += board[i - 1][j - 1] & 1
        return count


def main():
    test = GameOfLife()
    board = [[0, 1, 0, 0, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 1], [1, 1, 0, 0, 1, 0, 0]]
    test.game_of_life(board)
    print board


if __name__ == "__main__":
    main()

