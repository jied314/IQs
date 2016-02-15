from union_find import UnionFindRank, UnionFindNaive

class UndirectedGraph(object):
    def __init__(self, num_vert, edges):
        self.V = num_vert
        self.edges = edges
        self.uf = UnionFindRank(num_vert)
        self.adjs = []

    # check whether cycle exists in an undirected graph - use UF or DFS
    def has_cycle(self):
        return self.has_cycle_uf()
        # return self.has_cycle_dfs()

    # check whether cycle exists in an undirected graph - use Union Find Rank & Union Find Naive
    # O(ElgV)
    def has_cycle_uf(self):
        # uf_naive = UnionFindNaive(self.V)
        # return self.has_cycle_helper(uf_naive)
        # iterate through all edges of graph, find subset of both vertices of every edge.
        #  if both subsets are same, then there is cycle in graph.
        for x, y in self.edges:
            x = self.uf.find(x)
            y = self.uf.find(y)
            if x == y:
                return True
            self.uf.union(x, y)
        return False

    def num_sets(self):
        return self.uf.num_sets()

    # use DFS to check cycle
    # The assumption of this approach is that there are no parallel edges between any two vertices.
    # Idea:
    #   For every visited vertex 'v', if there is an adjacent 'u' such that u is already visited and u is not
    # parent of v, then there is a cycle in graph. If we don't find such an adjacent for any vertex, we say
    # that there is no cycle.
    # O(V+E)
    def has_cycle_dfs(self, visited=None):
        self.init_adjs()
        if not visited:
            visited = [False] * self.V
        for i in range(0, self.V):
            if not visited[i]:
                if self.dfs_util(i, visited, -1):
                    return True
        return False

    def dfs_util(self, v, visited, parent):
        visited[v] = True
        for adj in self.adjs[v]:
            if not visited[adj]:
                if self.dfs_util(adj, visited, v):
                    return True
            # if a visited adjacent and is not parent of current vertex, then there is a cycle.
            elif adj != parent:
                return True
        return False

    def init_adjs(self):
        self.adjs = [[] for _ in range(self.V)]
        for start, end in self.edges:
            self.adjs[start].append(end)
            self.adjs[end].append(start)


def main():
    edges = [[0, 1], [1, 2], [0, 2]]
    graph = UndirectedGraph(3, edges)
    if graph.has_cycle():
        print "graph contains cycle"
    else:
        print "graph doesn't contain cycle"

if __name__ == "__main__":
    main()