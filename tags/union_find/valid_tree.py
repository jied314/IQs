# There are n nodes numbered from 0 to n-1 and a set of edges (undirected).
# Please determine if it is a valid tree.
# For example:
#   n = 5, edge set = {{0,1}, {0,2}, {2,3}, {2,4}}. Result: true
#   n = 5, edge set = {{0,1}, {1,2}, {0,2}, {2,3}, {2,4}}. Result: false
#   n = 4, edge set = {{0,1}, {2,3}}. Result: false
#
# Note:
#   if is a valid tree, the graph has no cycle and it is connected.
#
# Idea:
#   1. DFS - find cycle and whether the graph is connected.
#   2. Union Find - find cycle and total number of connected components
from undirected_graph import UndirectedGraph as Graph


class Solution(object):
    # use Union-Find to find cycle and whether connected
    def valid_tree_uf(self, num_vert, edges):
        graph = Graph(num_vert, edges)
        if graph.has_cycle_uf():
            return False
        return graph.num_sets() == 1

    # use DFS - slight different from has_cycle from undirected_graph
    # only care whether the graph is connected (one set) and contains cycle. (No need to loop through all
    # vertices to do DFS)
    def valid_tree_dfs(self, num_vert, edges):
        graph = Graph(num_vert, edges)
        graph.init_adjs()
        visited = [False] * num_vert
        # check if graph contains cycle
        if self.has_cycle_dfs(graph, 0, visited, -1):
            return False
        # check if all visited
        for i in range(0, num_vert):
            if visited[i] is False:
                return False
        return True

    # similar to has_cycle_dfs in undirected_graph
    def has_cycle_dfs(self, graph, v, visited, parent):
        visited[v] = True
        for adj in graph.adjs[v]:
            if not visited[adj]:
                if self.has_cycle_dfs(graph, adj, visited, v):
                    return True
            # if a visited adjacent and is not parent of current vertex, then there is a cycle.
            elif adj != parent:
                return True
        return False


V = 5
edges1 = [[0, 1], [0, 2], [2, 3], [2, 4]]
edges2 = [[0, 1], [1, 2], [0, 2], [2, 3], [2, 4]]
edges3 = [[0, 1], [2, 3]]

test = Solution()
print test.valid_tree_uf(V, edges1)
print test.valid_tree_uf(V, edges2)
print test.valid_tree_uf(4, edges3)
print test.valid_tree_dfs(V, edges1)
print test.valid_tree_dfs(V, edges2)
print test.valid_tree_dfs(4, edges3)
