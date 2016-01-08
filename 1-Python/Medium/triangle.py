# 10/7 - Array, DP
# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows 
# in the triangle.
# Note:
#   corner cases. len(triangle) == 1
#   len(triangle) = len(triangle[-1])
#
import sys
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

    # 12/26 - Revisit
    # Same Idea
    # Note: no need to keep track of min -> min the last row of triangle
    def minimum_total_revisit(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle is None or len(triangle) == 0:
            return 0
        length = len(triangle)
        if length == 1:
            return triangle[0][0]
        ret = sys.maxint
        for i in range(1, length):
            for j in range(0, len(triangle[i])):
                triangle[i][j] = self.find_min(triangle[i-1], j, triangle[i][j])
                ret = min(ret, triangle[i][j])
        return ret

    def find_min(self, row, index, val):
        ret = sys.maxint
        length = len(row)
        if index > 0:
            ret = min(ret, row[index-1] + val)
        if index < length:
            ret = min(ret, row[index] + val)
        return ret


def main():
    test = Triangle()
    triangle1 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    triangle2 = [[2]]
    print test.minimum_total(triangle1)
    print triangle1
    print test.minimum_total(triangle2)


if __name__ == '__main__':
    main()
