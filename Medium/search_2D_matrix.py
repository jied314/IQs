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


def main():
    test = Search2DMatrix()
    print test.search_matrix([
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 24)


if __name__ == '__main__':
    main()


