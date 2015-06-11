# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally
# or vertically. You may assume all four edges of the grid are all surrounded by water.

class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        total_groups_h = 0
        total_groups_v = 0
        if len(grid) > 0:
            total_groups_h = self.count(grid)
            print
            total_groups_v = self.count([list(i) for i in zip(*grid)])
        return min(total_groups_h, total_groups_v)

    def count(self, grid):
        total_groups = self.count_groups(grid[0], None)
        for i in range(1, len(grid)):
            total_groups += self.count_groups(grid[i], grid[i-1])
        return total_groups

    def count_groups(self, current, above):
        groups = {}
        group_index = []
        num_groups = 0
        current.insert(0, '0')
        current.append('0')
        for i in range(1, len(current)):
            if current[i] == '1':
                group_index.append(i - 1)
            if current[i] == '0' and current[i - 1] == '1':
                groups[num_groups] = group_index
                num_groups += 1
                group_index = []
        print groups

        current.pop()
        del current[0]
        if above is not None:
            for group_index in groups:
                for index in group_index:
                    if above[index] == '1':
                        num_groups -= 1
                        break

        print num_groups
        return num_groups


def main():
    s = Solution()
    """num_islands1 = s.numIslands([['1', '1', '1', '1', '0'],
                                 ['1', '1', '0', '1', '0'],
                                 ['1', '1', '0', '1', '0'],
                                 ['0', '0', '0', '0', '0']])
    print 'number of islands is: {0}\n'.format(num_islands1)

    num_islands2 = s.numIslands([['1', '1', '0', '0', '0'],
                                 ['1', '1', '0', '0', '0'],
                                 ['0', '0', '1', '0', '0'],
                                 ['0', '0', '0', '1', '1']])
    print 'number of islands is: {0}\n'.format(num_islands2)

    num_islands3 = s.numIslands([['1', '1', '0', '1', '0'],
                                 ['1', '0', '1', '0', '0'],
                                 ['0', '0', '1', '0', '0'],
                                 ['1', '0', '0', '1', '1']])
    print 'number of islands is: {0}\n'.format(num_islands3)

    num_islands4 = s.numIslands([['1', '0', '1', '1', '1'],
                                 ['1', '0', '1', '0', '1'],
                                 ['1', '1', '1', '0', '1']])
    print 'number of islands is: {0}\n'.format(num_islands4)"""

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