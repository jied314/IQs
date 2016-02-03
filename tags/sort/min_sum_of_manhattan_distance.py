# 2/1 - Sort
# Given N points on a plane, find a point P that has the minimum Manhattan distance to all other points.
# Manhattan Distance: |x0-x1| + |y0-y1|
# Idea - O(n log n):
#   1. sort according to x coordinates
#   2. scan from left to right, for each point, compute the total Manhattan distance on x from it to the rest of points
#     (O(n) time for the left most point and O(1) for each of the rest)
#      use two arrays: left & right
#      left[i] = x[1] + x[2] + ... + x[i-1]
#      right[i] = x[i+1] + x[i+2] ... + x[n]
#      sum[i] = x[i] * i - left[i] + right[i] - (n - 1 - i) * x[i]
#   3. do 1 and 2 for y coordinates
#   4. add up the distances on x and y for each point and locate the minimum
#
# Note:
#   Manhattan Distance is related to the relative positions between points.
#   if one dimension, O(N), since only need to find the N/2th Point;
#   if multiple dimensions, O(NlgN), because cannot determine the position of the point, has to find the minimum sum
# for all dimensions.

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution(object):
    def min_mht_dis(self, pts):
        """
        :param pts: List[Point]
        :return: int
        """
        if pts is None or len(pts) == 0:
            return 0
        # calculate manhattan distance for x axis
        sorted_pts = sorted(pts, key=lambda pt: pt.x)
        x_sums = self.mht_sum(sorted_pts, True)
        # calculate manhattan distance for y axis
        sorted_pts = sorted(pts, key=lambda pt: pt.y)
        y_sums = self.mht_sum(sorted_pts, True)
        # find the sum of mhd_x + mhd_y
        ret = (1 << 31) - 1
        for i in range(0, len(pts)):
            ret = min(ret, x_sums[(pts[i].x, pts[i].y)] + y_sums[(pts[i].x, pts[i].y)])
        return ret

    # calculate the manhattan distance for all points
    # Trick - use left & right to record the the left_sum and right_sum
    #         note pts is sorted, that's why it works.
    def mht_sum(self, pts, is_x):
        """
        :param pts: List[Point]
        :param is_x: Boolean
        :return:  Dict{(int, int): int}
        """
        length = len(pts)
        left, right = [0] * length, [0] * length
        # record the left sum
        left_sum = 0
        for i in range(0, length):
            left[i] = left_sum
            left_sum += pts[i].x if is_x else pts[i].y
        # record the right sum
        right_sum = 0
        for i in range(length-1, -1, -1):
            right[i] = right_sum
            right_sum += pts[i].x if is_x else pts[i].y
        # record the manhattan distance for each point, use tuple as key
        ret = {}
        for i in range(0, length):
            p = pts[i].x if is_x else pts[i].y
            ret[(pts[i].x, pts[i].y)] = p * i - left[i] + right[i] - (length-1-i) * p
        return ret