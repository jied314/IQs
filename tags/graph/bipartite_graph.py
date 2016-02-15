# 2/10 - Graph, BFS
# A Bipartite Graph is a graph whose vertices can be divided into two independent sets, U and V such that
# every edge (u, v) either connects a vertex from U to V or a vertex from V to U.
# In other words, for every edge (u, v), either u belongs to U and v to V, or u belongs to V and v to U.
# We can also say that there is no edge that connects vertices of same set.
#
# Refer to: http://www.geeksforgeeks.org/bipartite-graph/
# Solution:
#   1. Assign RED color to the source vertex (putting into set U).
#   2. Color all the neighbors with BLUE color (putting into set V).
#   3. Color all neighbor's neighbor with RED color (putting into set U).
#   4. This way, assign color to all vertices such that it satisfies all the constraints of m way coloring
#      problem where m = 2.
#   5. While assigning colors, if we find a neighbor which is colored with same color as current vertex,
#      then the graph cannot be colored with 2 vertices (or graph is not Bipartite)
from directed_graph import DirectedGraph


class Solution(object):
    def is_bipartite(self, graph):
        """
        :param graph: Graph
        :return: Boolean
        """
        return graph.is_bipartite()
