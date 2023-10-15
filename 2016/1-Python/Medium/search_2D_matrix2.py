# 8/22 - Divide and Conquer, BS
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#   Integers in each row are sorted in ascending from left to right.
#   Integers in each column are sorted in ascending from top to bottom.

class Search2DMatrix2(object):
    # Test on LeetCode - 124ms
    # Idea:
    #   numbers smaller than val should be to its left, larger should be behind
    #   start with the upper right corner, search its left and behind
    # Time Complexity - O(m+n)
    def search_matrix_divide_and_conquer(self, matrix, target):
        num_r = len(matrix)
        if num_r == 0:
            return False
        num_c = len(matrix[0])
        i, j = 0, num_c - 1
        while i < num_r and j >= 0:
            num = matrix[i][j]
            if num == target:
                return True
            elif num < target:
                i += 1
            else:
                j -= 1
        return False

    # Test on LeetCode - 260ms
    # Idea:
    #   search each row using bfs
    # Time Complexity - O(mlg(n))
    def search_matrix_bs(self, matrix, target):
        num_r = len(matrix)
        if num_r == 0:
            return False
        for i in range(0, num_r):
            row = matrix[i]
            if self.bs(row, target):
                return True
        return False

    # binary search
    def bs(self, array, target):
        return self.bs_helper(0, len(array)-1, array, target)

    def bs_helper(self, low, high, array, target):
        while low <= high:
            mid = low + (high - low)/2
            mid_val = array[mid]
            if target == mid_val:
                return True
            elif target < mid_val:
                high = mid - 1
            else:
                low = mid + 1
        return False

    # # Test on LeetCode - 940ms
    # Idea:
    #   divide the search space into quadrants
    #   target < matrix[i][j] -> upper left, upper right and bottom left
    #   target > matrix[i+1][j+1] -> bottom right, upper right and bottom left
    # Time Complexity - T(n) = 3T(n/4) + c, O(N**log(4,3)) N = m * n
    def search_matrix_quadrants(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        num_r = len(matrix)
        if num_r == 0:
            return False
        num_c = len(matrix[0])
        return self.search_matrix_helper(matrix, 0, num_r-1, 0, num_c-1, target)

    def search_matrix_helper(self, matrix, r1, r2, c1, c2, target):
        if r1 > r2 or c1 > c2:
            return False

        rm, cm = r1 + (r2 - r1)/2, c1 + (c2 - c1)/2
        num = matrix[rm][cm]
        if num == target:
            return True
        elif num > target:
            return self.search_matrix_helper(matrix, r1, rm-1, c1, cm-1, target) or \
                   self.search_matrix_helper(matrix, r1, rm-1, cm, c2, target) or \
                   self.search_matrix_helper(matrix, rm, r2, c1, cm-1, target)
        else:
            return self.search_matrix_helper(matrix, rm+1, r2, cm+1, c2, target) or \
                   self.search_matrix_helper(matrix, r1, rm, cm+1, c2, target) or \
                   self.search_matrix_helper(matrix, rm+1, r2, c1, cm, target)


def main():
    test = Search2DMatrix2()
    print test.search_matrix_quadrants([[-5]], -10)
    #print test.search_matrix([[1,3,5]], 1)
    #print test.search_matrix_divide_and_conquer([[-1, 3]], -1)


if __name__ == "__main__":
    main()
