# 2/8 - Important Graph Methods
from collections import deque


class Graph(object):
    def __init__(self, num_vert):
        self._num_vert = num_vert  # number of vertices
        self._adjs = [[] for _ in range(num_vert)]  # adjacent list

    def add_edge(self, v, w):
        assert(0 <= v < self._num_vert and 0 <= w < self._num_vert)
        self._adjs[v].append(w)

    """...........................Graph Traversal........................."""
    # Graph DFS - given a starting vertex
    def dfs_traversal(self, start):
        visited = set()
        ret = []
        self.dfs(start, visited, ret)
        return ret

    def dfs(self, node, visited, ret):
        if node in visited:
            return
        visited.add(node)
        ret.append(node)
        for next in self._adjs[node]:
            self.dfs(next, visited, ret)

    # Graph BFS - given a starting vertex
    def bfs_traversal(self, start):
        ret = []
        visited = set()
        q = deque()
        q.append(q)
        while q:
            cur = q.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            ret.append(cur)
            for adj in self._adjs[cur]:
                q.append(adj)
        return ret

    """........................Topological Sort..........................."""
    # Topological Sort (order must exist)
    # This version returns the reversed order
    def topo_sort(self):
        ret = []
        visited = [False] * self._num_vert
        # visit all non_visited vertex
        for i in range(0, self._num_vert):
            if not visited[i]:
                self.visit(i, visited, ret)
        ret.reverse()
        return ret

    # DFS visit in Topological Sort
    def visit(self, vertex, visited, ret):
        visited[vertex] = True
        for next in self._adjs[vertex]:
            if not visited[next]:
                self.visit(next, visited, ret)
        ret.append(vertex)

    # DFS check cycle (use topological sort)
    def has_cycle(self):
        visited = [False] * self._num_vert
        in_visit = [False] * self._num_vert
        for i in range(self._num_vert):
            if not visited[i] and self.cycle(i, visited, in_visit):
                return True
        return False

    # DFS visit to check whether cycle exists
    def cycle(self, vertex, visited, in_visit):
        if in_visit[vertex]:  # cycle
            return True
        if visited[vertex]:  # already visited
            return False

        in_visit[vertex] = True
        for next in self._adjs[vertex]:
            if not visited[next] and self.cycle(next, visited, in_visit):
                return True
        visited[vertex] = True
        in_visit[vertex] = False
        return False

    """................Graph Connectivity Problem - SCC............................"""

    # return the transpose of this graph
    def get_transpose(self):
        g = Graph(self._num_vert)
        for i in range(0, self._num_vert):
            adjacent_vertices = self._adjs[i]
            for vertex in adjacent_vertices:
                g._adjs[vertex].append(i)
        return g

    # a recursive function to print DFS starting from v
    def dfs_util(self, v, visited):
        visited[v] = True
        print v, " ",
        for adj in self._adjs[v]:
            if not visited[adj]:
                self.dfs_util(adj, visited)

    # the main function that returns true if graph is strongly connected
    def is_strongly_connected(self):
        visited = [False] * self._num_vert
        # DFS starting at 0
        self.dfs_util(0, visited)

        # if DFS traversal doesn't visit all vertices, then return false.
        for visit in visited:
            if visit is False:
                return False

        gr = self.get_transpose()

        for i in range(self._num_vert):
            visited[i] = False
        # do DFS for reversed graph starting from first vertex.
        # Staring Vertex must be same starting point of first DFS
        gr.dfs_util(0, visited)

        # if the second DFS traversal doesn't visit all vertices, then return false.
        for visit in visited:
            if visit is False:
                return False

        return True

    # print all SCCs exist in the graph - Kosaraju's Algorithm
    def printSCCs(self):
        stack = []
        visited = [False] * self._num_vert

        for i in range(self._num_vert):
            if not visited[i]:
                self.fill_order(i, visited, stack)

        gr = self.get_transpose()

        for i in range(self._num_vert):
            visited[i] = False

        while stack:
            v = stack.pop()
            if not visited[v]:
                gr.dfs_util(v, visited)
                print

    def fill_order(self, v, visited, stack):
        visited[v] = True
        for adj in self._adjs[v]:
            if not visited[adj]:
                self.fill_order(adj, visited, stack)
        # all vertices reachable from v are processed by now, push v to Stack
        stack.append(v)

    # check if a graph is a bipartite
    # O(V+E) if using adjacent list; else O(V^2)
    def is_bipartite(self, src):
        RED, BLUE, NULL = 1, 2, -1
        # create a color array to store colors assigned to all vertices.
        colors = [NULL] * self._num_vert
        colors[src] = RED

        # queue for BFS
        queue = deque()
        queue.append(src)

        while queue:
            u = queue.pop()
            for v in self._adjs[u]:
                if colors[v] == NULL:
                    colors[v] = BLUE if colors[u] == RED else RED
                    queue.append(v)
                elif colors[v] == colors[u]:
                    return False
        return True

# Create graphs given in the above diagrams
g1 = Graph(5)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
g1.add_edge(3, 0)
g1.add_edge(2, 4)
g1.add_edge(4, 2)
if g1.is_strongly_connected():
    print "Yes"
else:
    print "No"

g2 = Graph(4)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(2, 3)
if g2.is_strongly_connected():
    print "Yes"
else:
    print "No"

# Create a graph given in the above diagram
g = Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(3, 4)

print "Following are strongly connected components " + "in given graph "
g.printSCCs()

