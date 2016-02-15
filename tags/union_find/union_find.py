# 2/11 - Union Find
#
# Naive O(N) - http://www.geeksforgeeks.org/union_find/
# Union By Rank O(logN) - http://www.geeksforgeeks.org/union_find-algorithm-set-2-union-by-rank/
#
# Find: Determine which subset a particular element is in. This can be used for determining if two elements
# are in the same subset.
# Union: Join two subsets into a single subset.
#
# UF can be used to check whether an undirected graph contains cycle or not.


class UnionFindRank(object):
    def __init__(self, num_vert):
        self.parents = []
        self.ranks = []
        for i in range(num_vert):
            self.parents.append(i)
            self.ranks.append(0)
        self.num = num_vert

    # find the set that element x belongs to
    # flatten the tree - uses path compression technique O(lgV)
    def find(self, x):
        # find root and make root as parent of x (path compression)
        if x == self.parents[x]:  # x is the parent
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    # union of two sets of x and y
    # always attach smaller depth tree under the root of the deeper tree - uses union by rank, O(lgV)
    def union(self, x, y):
        # find the parents of x and y
        x = self.find(x)
        y = self.find(y)

        # attach smaller rank tree under root of high rank tree (Union by Rank)
        if self.ranks[x] < self.ranks[y]:
            self.parents[x] = y
        elif self.ranks[x] > self.ranks[y]:
            self.parents[y] = x
        # if ranks are the same, then make one as root and increment its rank by one
        else:
            self.parents[y] = x  # x is the root
            self.ranks[x] += 1  # increase the rank of x

    def num_sets(self):
        count = 0
        for i in range(self.num):
            if self.parents[i] == i:
                count += 1
        return count

class UnionFindNaive(object):
    def __init__(self, num_vert):
        self.parents = [-1] * num_vert

    # Note - parents are initialized as -1 here.
    # find the subset that x belongs to - O(N)
    def find(self, x):
        if self.parents[x] == -1:
            return x
        return self.find(self.parents[x])

    # union two subsets x and y - O(N)
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        self.parents[x] = y


