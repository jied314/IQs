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
class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        for i in range(0, len(grid)):
            grid[i].insert(0, '0')
            grid[i].append('0')
        grid.insert(0, ['0' for i in range(0, len(grid[0]))])
        grid.append(['0' for i in range(0, len(grid[0]))])
        #print grid

        num_rows = len(grid)
        num_columns = len(grid[0])
        not_visit = [[i, j] for i in range(1, num_rows - 1) for j in range(1, num_columns - 1) if grid[i][j] == '1']
        #print not_visit
        in_visit = []
        group_dict = {}
        num_groups = 1
        while not_visit:
            node = not_visit.pop(0)
            in_visit.append(node)
            while in_visit:
                self.visit(in_visit, not_visit, grid, num_groups)
            num_groups += 1
        #print grid
        return num_groups - 1

    def visit(self, in_visit, not_visit, grid, num_groups):
        current = in_visit.pop(0)
        grid[current[0]][current[1]] = num_groups
        neighbors = [[current[0], current[1] - 1], [current[0], current[1] + 1],
                     [current[0] - 1, current[1]], [current[0] + 1, current[1]]]
        for neighbor in neighbors:
            neighbor_value = grid[neighbor[0]][neighbor[1]]
            if neighbor_value == '1':
                not_visit.remove(neighbor)
                in_visit.append(neighbor)
                grid[neighbor[0]][neighbor[1]] = num_groups

    def numIslands_concise(self, grid):
        num_groups = 1
        n = len(grid)
        if n > 0:
            m = len(grid[0])
            for i in range(0, n):
                for j in range(0, m):
                    if grid[i][j] == '1':
                        self.dfs(i, j, grid, num_groups)
                        num_groups += 1
        #print grid
        return num_groups - 1

    def dfs(self, i, j, grid, num_group):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = num_group
        self.dfs(i, j - 1, grid, num_group)
        self.dfs(i, j + 1, grid, num_group)
        self.dfs(i - 1, j, grid, num_group)
        self.dfs(i + 1, j, grid, num_group)


def main():
    s = Solution()
    num_islands1 = s.numIslands_concise([['1', '1', '1', '1', '0'],
                                 ['1', '1', '0', '1', '0'],
                                 ['1', '1', '0', '1', '0'],
                                 ['0', '0', '0', '0', '0']])
    print 'number of islands is: {0}\n'.format(num_islands1)

    num_islands2 = s.numIslands_concise([['1', '1', '0', '0', '0'],
                                 ['1', '1', '0', '0', '0'],
                                 ['0', '0', '1', '0', '0'],
                                 ['0', '0', '0', '1', '1']])
    print 'number of islands is: {0}\n'.format(num_islands2)

    num_islands3 = s.numIslands_concise([['1', '1', '0', '1', '0'],
                                 ['1', '0', '1', '0', '0'],
                                 ['0', '0', '1', '0', '0'],
                                 ['1', '0', '0', '1', '1']])
    print 'number of islands is: {0}\n'.format(num_islands3)

    num_islands4 = s.numIslands([['1', '0', '1', '1', '1'],
                                 ['1', '0', '1', '0', '1'],
                                 ['1', '1', '1', '0', '1']])
    print 'number of islands is: {0}\n'.format(num_islands4)

    num_islands5 = s.numIslands([['1', '1', '1', '1', '1', '1', '1'],
                                 ['0', '0', '0', '0', '0', '0', '1'],
                                 ['1', '1', '1', '1', '1', '0', '1'],
                                 ['1', '0', '0', '0', '1', '0', '1'],
                                 ['1', '0', '1', '0', '1', '0', '1'],
                                 ['1', '0', '1', '1', '1', '0', '1'],
                                 ['1', '1', '1', '1', '1', '1', '1']])
    print 'number of islands is: {0}\n'.format(num_islands5)


if __name__ == '__main__':
    main()