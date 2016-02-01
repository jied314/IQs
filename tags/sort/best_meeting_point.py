# 1/28 - not in LC
# A group of two or more people wants to meet and minimize the total travel distance.
# You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group.
# The distance is calculated using Manhattan Distance,
# where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
#
# For example, given three people living at (0,0), (0,4), and (2,2):
#   1 - 0 - 0 - 0 - 1
#   |   |   |   |   |
#   0 - 0 - 0 - 0 - 0
#   |   |   |   |   |
#   0 - 0 - 1 - 0 - 0
# The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal.
# So return 6.
#
# Hint:
#   Try to solve it in one dimension first. How can this solution apply to the two dimension case?
# Idea:
#   Since the distance is computed using the Manhattan Distance, we can decompose this 2-d problem
# into two 1-d problems and combine (add) their solutions. In fact, the best meeting point is just
# the point that comprised by the two best meeting points in each dimension.
# For the 1d case, the best meeting point is just the median point.
# Proof:
#   Suppose we have a set S of real numbers. Show that the sum of |s - x| is minimal if x is equal to the median.
# The median minimizes the sum of absolute deviations.


class Solution(object):
    def min_total_distance(self, grid):
        """
        :param grid: List[List[int]]
        :return: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        ii, jj = [], []
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 1:  # is home
                    ii.append(i)
                    jj.append(j)

        # only need to sort jj. ii is already sorted (the sequence visiting)
        jj.sort()
        size = len(ii)
        ret = 0
        im, jm = ii[size/2], jj[size/2]
        for i in ii:
            ret += abs(i - im)
        for j in jj:
            ret += abs(j - jm)
        return ret