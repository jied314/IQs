# 10/7 - Array, DP
# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows 
# in the triangle.
# Note:
#   corner cases. len(triangle) == 1
#   len(triangle) = len(triangle[-1])
#   
class Triangle(object):
    # Test on LeetCode - 64ms, Space O(n)
    # Idea:
    #   top-down DP
    #   only keep the previous resule - Space O(1)
    #   thread unsafe because modify inputs - should use O(n) space to store intermediate result
    #   try use bottom-up dp
    def minimum_total(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        length = len(triangle)
        if length == 0:
            return 0
        elif length == 1:
            return min(triangle[0])
        row = []
        for i in range(1, length):
            pre = triangle[i - 1]
            row = triangle[i]
            row_length = len(pre)
            row[0] += pre[0]
            for j in range(1, row_length):
                row[j] += min(pre[j-1], pre[j])
            row[-1] += pre[-1]
        return min(row)


def main():
    test = Triangle()
    triangle1 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    triangle2 = [[2]]
    print test.minimum_total(triangle1)
    print triangle1
    print test.minimum_total(triangle2)


if __name__ == '__main__':
    main()
