# 7/8 - Array, BS
# Note:
#   convert matrix to a sorted list, then do BS directly
#   not good due to:
#       1. no performance improvement
#       2. m * n can potentially cause overflow
#       3. use of % and / (to calculate the right index) can be computationally expensive
class Search2DMatrix:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}

    # Test on LeetCode - 52ms
    # Complexity - O(mlg(n))
    def search_matrix(self, matrix, target):
        columns = len(matrix[0])
        exist = False
        row = None
        for i in range(0, len(matrix)):
            if matrix[i][0] <= target <= matrix[i][columns-1]:
                row = i
                break
        if row is not None:
            nums = matrix[row]
            low, high = 0, columns-1
            while low <= high:
                mid = (low + high) / 2
                if target == nums[mid]:
                    exist = True
                    return exist
                elif target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return exist

    # Test on LeetCode - 48ms
    # Idea: bs on the first column to locate search row, then bs
    # Complexity - O(lg(m) * lg(n))
    def search_matrix_bs(self, matrix, target):
        num_r = len(matrix)
        if num_r == 0:
            return False
        num_c = len(matrix[0])
        first_column = [matrix[i][0] for i in range(0, num_r)]
        c1, c2 = 0, num_r-1
        while c1 <= c2:
            cm = c1 + (c2 - c1)/2
            cm_val = first_column[cm]
            if cm_val == target:
                return True
            elif cm_val < target:
                c1 = cm + 1
            else:
                c2 = cm - 1
        row_index = c1 - 1
        return self.bs(matrix[row_index], target)

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

def main():
    test = Search2DMatrix()
    """print test.search_matrix_bs([
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 25)"""
    print test.search_matrix_bs([[1],[3]], 3)


if __name__ == '__main__':
    main()


