# 10/23 - Array, Backtracking
# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
# horizontally or vertically neighboring. The same letter cell may not be used more than once.
# For example,
# Given board = [['A', 'B', 'C', 'E'],
#                ['S', 'F', 'C', 'S'],
#                ['A', 'D', 'E', 'E']]
# word = "ABCCED", - > returns true,
# word = "SEE", - > returns true,
# word = "ABCB", - > returns false.
# First Trial - Fail


class WordSearch(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board is not None or len(board) < 1 or len(board[0]) < 1:
            return False
        m, n = len(board), len(board[0])
        black_list = {}
        visited = []
        index, length = 0, len(word)
        char_map = self.process_word(word)
        while index < length:
            for i in range(0, m):
                for j in range(0, n):
                    c = board[i][j]
                    if c in char_map:
                        positions = char_map[c]
                        for pos in positions:
                            print


    def process_word(self, word):
        char_map = {}
        length = len(word)
        for i in range(0, length):
            c = word[i]
            if c not in char_map:
                char_map[c] = []
            char_map[c].append(i)
        return char_map

    # Test on LeetCode - 360ms
    # Idea: DFS
    #   start matching from the first character, exhaust all possibilities.
    #   avoid reusing the same cell by setting a special value for the visited cell.
    def process_word_dfs(self, board, word):
        if board is None:
            return False
        m, n = len(board), len(board[0])
        for i in range(0, m):
            for j in range(0, n):
                if self.is_found(board, word, 0, i, j, m, n):
                    return True
        return False

    # Recursive matching
    # find whether word[index:] exist in board, starting with board[i][j]
    def is_found(self, board, word, index, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] == "" or word[index] != board[i][j]:
            return False
        if index == len(word) - 1:  # reach the end
            return True
        c = board[i][j]
        board[i][j] = ""
        if self.is_found(board, word, index + 1, i - 1, j, m, n) or self.is_found(board, word, index + 1, i + 1, j, m,
                                                                                  n) \
                or self.is_found(board, word, index + 1, i, j - 1, m, n) or self.is_found(board, word, index + 1, i,
                                                                                          j + 1, m, n):
            return True
        board[i][j] = c
        return False


def main():
    test = WordSearch()
    board = [['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']]
    # test.process_word("leetcode")
    print test.process_word_dfs(board, "SEE")
    print test.process_word_dfs(board, "ABCCED")
    print test.process_word_dfs(board, "ABCB")


if __name__ == "__main__":
    main()