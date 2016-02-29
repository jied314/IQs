# Number of Islands - DFS, BFS
# Idea:
#   exhaust one island before staring another
# Solution:
#   1. record not_visit and in_visit
#   2. utilize the grid to record (concise)
# Note:
#   the recursive nature actually visit all possible nodes before staring another island
#   no need for in_visit
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally
# or vertically. You may assume all four edges of the grid are all surrounded by water.
#
from collections import deque


class Solution:
    def num_islands(self, grid):
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])

        count = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1':
                    self.visit_dfs(grid, i, j)
                    count += 1
        return count

    # Test on LC - 108ms, 88%
    def visit_bfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        queue = deque()
        queue.append([i, j])
        while queue:
            ii, jj = queue.popleft()
            if queue[ii][jj]:  # still not visited
                queue[ii][jj] = '0'
                if ii > 0 and grid[ii-1][jj] == '1':  # top
                    queue.append([ii-1, jj])
                if ii < m-1 and grid[ii+1][jj] == '1':  # bottom
                    queue.append([ii+1, jj])
                if jj > 0 and grid[ii][jj-1] == '1':  # left
                    queue.append([ii, jj-1])
                if jj < n-1 and grid[ii][jj+1] == '1':  # right
                    queue.append([ii, jj+1])

    # Test on LC - 100ms, 93%
    def visit_dfs(self, grid, i, j):
        if not grid[i][j]:  # visited
            return
        grid[i][j] = '0'

        if i > 0 and grid[i-1][j] == '1':
            self.visit_dfs(grid, i-1, j)
        if i < len(grid) - 1 and grid[i+1][j] == "1":
            self.visit_dfs(grid, i+1, j)
        if j > 0 and grid[i][j-1] == "1":
            self.visit_dfs(grid, i, j-1)
        if j < len(grid[0]) - 1 and grid[i][j+1] == "1":
            self.visit_dfs(grid, i, j+1)

    # not change matrix, use another matrix to store visited
    # @param {character[][]} grid
    # @return {integer}
    def num_islands_memory(self, grid):
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        queue = deque()
        count = 0
        for i in range(0, m):
            for j in range(0, n):
                if visited[i][j] or grid[i][j] != '1':
                    continue
                count += 1
                queue.clear()
                queue.append([i, j])
                while queue:
                    ii, jj = queue.popleft()
                    if visited[ii][jj]:  # visited
                        continue
                    visited[ii][jj] = True
                    if ii > 0 and grid[ii-1][jj] == '1':
                        queue.append([ii-1, jj])
                    if ii < m-1 and grid[ii+1][jj] == '1':
                        queue.append([ii+1, jj])
                    if jj > 0 and grid[ii][jj-1] == '1':
                        queue.append([ii, jj-1])
                    if jj < n-1 and grid[ii][jj+1] == '1':
                        queue.append([ii, jj+1])
        return count

    # use Union-Find
    def num_islands_uf(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        uf = UnionFind(m*n)
        zero_count = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1':
                    cur = i * m + j
                    if i < m-1 and grid[i][j] == grid[i+1][j]:
                        down = cur + m
                        uf.union(cur, down)
                    if j < n-1 and grid[i][j] == grid[i][j+1]:
                        right = cur + 1
                        uf.union(cur, right)
                else:
                    zero_count += 1
        return uf.num_set() - zero_count

class UnionFind(object):
    def __init__(self, num_vert):
        self.V = num_vert
        self.parents = []
        self.ranks = []
        for i in range(0, num_vert):
            self.parents.append(i)
            self.ranks.append(0)

    def find(self, x):
        if self.parents[x] == x:  # single element set
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.ranks[x] < self.ranks[y]:
            self.parents[x] = y
        elif self.ranks[x] < self.ranks[y]:
            self.parents[y] = x
        else:  # self.ranks[x] == self.ranks[y]
            self.parents[y] = x
            self.ranks[x] += 1

    def num_set(self):
        count = 0
        for i in range(0, self.V):
            if self.parents[i] == i:
                count += 1
        return count


def main():
    s = Solution()
    grid1 = [['1', '1', '1', '1', '0'],
             ['1', '1', '0', '1', '0'],
             ['1', '1', '0', '1', '0'],
             ['0', '0', '0', '0', '0']]
    grid2 = [['1', '1', '1', '1', '0'],
             ['1', '1', '0', '1', '0'],
             ['1', '1', '0', '1', '0'],
             ['0', '0', '0', '0', '0']]
    grid3 = [['1', '1', '0', '0', '0'],
             ['1', '1', '0', '0', '0'],
             ['0', '0', '1', '0', '0'],
             ['0', '0', '0', '1', '1']]
    grid4 = [['1', '0', '1', '1', '1'],
             ['1', '0', '1', '0', '1'],
             ['1', '1', '1', '0', '1']]
    grid5 = [['1', '1', '1', '1', '1', '1', '1'],
             ['0', '0', '0', '0', '0', '0', '1'],
             ['1', '1', '1', '1', '1', '0', '1'],
             ['1', '0', '0', '0', '1', '0', '1'],
             ['1', '0', '1', '0', '1', '0', '1'],
             ['1', '0', '1', '1', '1', '0', '1'],
             ['1', '1', '1', '1', '1', '1', '1']]

    print s.num_islands_uf(grid1)
    print s.num_islands_memory(grid2)
    print s.num_islands_uf(grid3)
    print s.num_islands_memory(grid4)
    print s.num_islands_uf(grid5)
    print

    grid1 = [['1', '1', '1', '1', '0'],
             ['1', '1', '0', '1', '0'],
             ['1', '1', '0', '1', '0'],
             ['0', '0', '0', '0', '0']]
    grid2 = [['1', '1', '1', '1', '0'],
             ['1', '1', '0', '1', '0'],
             ['1', '1', '0', '1', '0'],
             ['0', '0', '0', '0', '0']]
    grid3 = [['1', '1', '0', '0', '0'],
             ['1', '1', '0', '0', '0'],
             ['0', '0', '1', '0', '0'],
             ['0', '0', '0', '1', '1']]
    grid4 = [['1', '0', '1', '1', '1'],
             ['1', '0', '1', '0', '1'],
             ['1', '1', '1', '0', '1']]
    grid5 = [['1', '1', '1', '1', '1', '1', '1'],
             ['0', '0', '0', '0', '0', '0', '1'],
             ['1', '1', '1', '1', '1', '0', '1'],
             ['1', '0', '0', '0', '1', '0', '1'],
             ['1', '0', '1', '0', '1', '0', '1'],
             ['1', '0', '1', '1', '1', '0', '1'],
             ['1', '1', '1', '1', '1', '1', '1']]

    print s.num_islands(grid1)
    print s.num_islands(grid2)
    print s.num_islands(grid3)
    print s.num_islands(grid4)
    print s.num_islands(grid5)

if __name__ == '__main__':
    main()