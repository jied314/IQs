# 12/1 - Breadth-first Search, Graph
# For a undirected graph with tree characteristics, we can choose any node as the root.
# The result graph is then a rooted tree. Among all possible rooted trees,
# those with minimum height are called minimum height trees (MHTs).
# Given such a graph, write a function to find all the MHTs and return a list of their root labels.
#
# Format:
#   The graph contains n nodes which are labeled from 0 to n - 1.
#   You will be given the number n and a list of undirected edges (each edge is a pair of labels).
#   You can assume that no duplicate edges will appear in edges.
#   Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
#
# Example 1:
#   Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]
#       0
#       |
#       1
#      / \
#     2   3
#   return [1]
#
# Example 2:
# Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
#    0  1  2
#     \ | /
#       3
#       |
#       4
#       |
#       5
# return [3, 4]
#
# Hint:
# How many MHTs can a graph have at most?
# Note:
#   (1) According to the definition of tree on Wikipedia: "a tree is an undirected graph in which any two vertices
# are connected by exactly one path. In other words, any connected graph without simple cycles is a tree."
#   (2) The height of a rooted tree is the number of edges on the longest downward path between the root
# and a leaf.
#
class MinimumHeightTrees(object):
    def find_min_height_trees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        min_height = n - 1
        adjacent_dict = self.generate_adjacent_list(n, edges)
        for node, adjacent_list in adjacent_dict.iteritems():
            if len(adjacent_list) > 1:
                height = self.find_max_child_height(node, None, adjacent_dict)
                if height == min_height:
                    ret.append(node)
                elif height < min_height:
                    ret = [node]
                    min_height = height
        if len(ret) == 0:
            ret = adjacent_dict.keys()
        return ret

    # generate adjacent list for the undirected graph
    # note edge [0, 1] will be saved as {0: [1], 1: [0]}
    def generate_adjacent_list(self, n, edges):
        adjacent_dict = {}
        for i in range(0, n):
            adjacent_dict[i] = []
        for edge in edges:
            adjacent_dict[edge[0]].append(edge[1])
            adjacent_dict[edge[1]].append(edge[0])
        return adjacent_dict

    # find the maximum height of all children
    def find_max_child_height(self, root, prev, adjacent_dict):
        max_child_height = 0
        for child in adjacent_dict[root]:
            if prev is None or child != prev:
                max_child_height = max(max_child_height, 1 + self.find_max_child_height(child, root, adjacent_dict))
        return max_child_height

    # 12/31 - Revisit
    # Idea:
    #   tree graph, N vertexes, N-1 edges.
    #   leaf vertex has 1 degree, inner vertex has a degree of at least 2.
    #   Work bottom up, from leaves to root, stop when n < 2.
    def find_min_height_trees_revisit(self, n, edges):
        if n == 1:
            return [0]
        adj = [set() for _ in xrange(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [i for i in xrange(n) if len(adj[i]) == 1]

        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    newLeaves.append(j)
            leaves = newLeaves
        return leaves

def main():
    test = MinimumHeightTrees()
    print test.find_min_height_trees(4, [[1, 0], [1, 2], [1, 3]])
    print test.find_min_height_trees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])


if __name__ == "__main__":
    main()

