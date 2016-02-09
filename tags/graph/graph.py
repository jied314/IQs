# 2/8 - Important Graph Methods
class Graph(object):
    def __init__(self, num_vert):
        self._num_vert = num_vert  # number of vertices
        self._adjs = [[] for _ in range(num_vert)]  # adjacent list

    def add_edge(self, v, w):
        assert(0 <= v < self._num_vert and 0 <= w < self._num_vert)
        self._adjs[v].append(w)

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

    def visit(self, vertex, visited, ret):
        visited[vertex] = True
        for next in self._adjs[vertex]:
            if not visited[next]:
                self.visit(next, visited, ret)
        ret.append(vertex)

    # DFS check cycle
    def has_cycle(self):
        visited = [False] * self._num_vert
        in_visit = [False] * self._num_vert
        for i in range(self._num_vert):
            if not visited[i] and self.cycle(i, visited, in_visit):
                return True
        return False

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
