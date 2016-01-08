# 10/7 - Array, DP (M)
# Follow up for "Unique Paths":
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# Note:
#   Iterative (better) V.S. Recursive
class UniquePaths2(object):
    # Test on LeetCode - 836ms
    def unique_paths_with_obstacles_recursive(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid is None:
            return 0
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        return self.count_dp(obstacleGrid, m-1, n-1) >> 1

    # count using DP - from end to start
    # use extra bits to store intermediate results
    def count_dp(self, obstacleGrid, i, j):
        if i < 0 or j < 0:  # out of bounds
            return 0
        if obstacleGrid[i][j] > 1:  # value already set
            return obstacleGrid[i][j]
        if obstacleGrid[i][j] & 1:  # is obstacle
            return 0
        # not obstacle
        if i == 0 and j == 0:  # can not be disjunctive (or) and set to 1, because obstacle can cause 0 path
            obstacleGrid[i][j] = 2  # bit pattern 10
        else:
            obstacleGrid[i][j] = self.count_dp(obstacleGrid, i-1, j) + self.count_dp(obstacleGrid, i, j-1)
        return obstacleGrid[i][j]

    # count using DP - from start to end
    # no need to use extra bits since the result is final
    # however, tricky since not having extra space
    # Test on LeetCode - 40ms
    def unique_paths_with_obstacles_iterative(self, obstacleGrid):
        if obstacleGrid is None:
            return 0
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j]:  # deal with obstacle
                    obstacleGrid[i][j] = 0
                elif i == 0 and j == 0:  # upper left
                    obstacleGrid[i][j] = 1
                elif i == 0:  # row 0
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1] * 1
                elif j == 0:  # column 0
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] * 1
                else:  # i > 0 and j > 0
                    obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
        return obstacleGrid[m-1][n-1]

    # 12/27 - Revisit
    # Test on LeetCode - 72ms
    # Idea:
    #   similar to Unique Paths solution
    #   use row to store results of previous row
    #   Edge cases:
    #       grid[0][0] == 0; grid[0][j] == 0
    def unique_paths_with_obstacles_revisit(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid is None or len(obstacleGrid[0]) == 0 or obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # init first row
        row = [1] * n
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                row[j] = 0
            else:
                row[j] = row[j-1]
        # pascal triangle with obstacles
        for i in range(1, m):
            if row[0] != 0 and obstacleGrid[i][0] == 1:
                row[0] = 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    row[j] = 0
                else:
                    row[j] += row[j-1]
        return row[-1]


def main():
    test = UniquePaths2()
    obstacleGrid1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print test.unique_paths_with_obstacles_recursive(obstacleGrid1)
    #print obstacleGrid1
    obstacleGrid2 = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]
    print test.unique_paths_with_obstacles_recursive(obstacleGrid2)
    #print obstacleGrid2
    obstacleGrid3 = [[1, 0]]
    print test.unique_paths_with_obstacles_recursive(obstacleGrid3)
    #print obstacleGrid3
    obstacleGrid1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print test.unique_paths_with_obstacles_iterative(obstacleGrid1)
    print obstacleGrid1
    obstacleGrid2 = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]
    print test.unique_paths_with_obstacles_iterative(obstacleGrid2)
    print obstacleGrid2
    obstacleGrid3 = [[1, 0]]
    print test.unique_paths_with_obstacles_iterative(obstacleGrid3)
    print obstacleGrid3


if __name__ == '__main__':
    main()
