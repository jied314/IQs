# 2/13 - Union Find
# Given a n,m which means the row and column of the 2D matrix and an array of pair A(size k).
# Originally, the 2D matrix is all 0 which means there is only sea in the matrix.
# The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can
# change the grid matrix[A[i].x][A[i].y] from sea to island.
# Return how many island are there in the matrix after each operator.
#
# Example
#   Given n = 3, m = 3, array of pair A = [(0,0),(0,1),(2,2),(2,1)].
#   return [1,1,2,2].
#
# Note:
#   0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them
# in the same island. We only consider up/down/left/right adjacent.
#
# Solution:
#   Variation of Union-Find
#   1. instead of passing in number of vertices to UnionFind, pass in a dictionary {pos: pos}.
#   2. instead of using num_serts() from UnionFind, update count if two cells have different parent.

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :param m: int
        :param n: int
        :param positions: List[List[int]]
        :return: List<int>
        """
        if positions is None or len(positions) == 0:
            return []

        map = {}
        for i, j in positions:
            p = i * m + j
            map[p] = p
        uf = UnionFind(map)

        pos_set = set()  # keep track which position is land so far
        count = 0  # count the current number of islands
        ret = []
        ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # for visiting 4 neighbors
        for i, j in positions:
            cur_pos = i * m + j
            pos_set.add(cur_pos)
            count += 1  # always increase count now, check later
            # check if neighbors are land
            for d in ds:
                ii, jj = i + d[0], j + d[1]
                if ii < 0 or ii >= m or jj < 0 or jj >= n:
                    continue
                neighbor_pos = ii * m + jj
                if neighbor_pos not in pos_set:  # neighbor is water
                    continue
                # current land actually connects to another land, count -= 1
                if uf.find(cur_pos) != uf.find(neighbor_pos):
                    count -= 1
                    uf.union(cur_pos, neighbor_pos)
            ret.append(count)
        return ret


class UnionFind(object):
    def __init__(self, map):
        self.parent_map = map
        self.ranks = {}
        for key in map.keys():
            self.ranks[key] = 0

    def find(self, x):
        if self.parent_map[x] != x:
            self.parent_map[x] = self.find(self.parent_map[x])
        return self.parent_map[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if self.ranks[x] < self.ranks[y]:
            self.parent_map[x] = y
        elif self.ranks[x] > self.ranks[y]:
            self.parent_map[y] = x
        else:
            self.parent_map[y] = x
            self.ranks[x] += 1



test = Solution()
print test.numIslands2(3, 3, [[0, 0], [0, 1], [0, 2], [2, 2], [2, 1], [1, 1], [1, 2]])

