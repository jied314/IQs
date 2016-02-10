# 2/8 - Graph
# Given a directed graph, find out whether the graph is strongly connected or not.
# A directed graph is strongly connected if there is a path between any two pair of vertices.
# It is easy for undirected graph, we can just do a BFS and DFS starting from any vertex. If BFS or DFS visits all
# vertices, then the given undirected graph is connected. This approach won't work for a directed graph.
#
# Refer to http://www.geeksforgeeks.org/connectivity-in-a-directed-graph/
#
# Naive:
#   Floyd Min Path - O(V^3)
#   DFS for all vertex - O(V*(V+E))
#
# Strongly Connected Components (SCC) solution - O(V+E)
# Following is Kosaraju's DFS based simple algorithm that does two DFS traversals of graph:
#   1) Initialize all vertices as not visited.
#   2) Do a DFS traversal of graph starting from any arbitrary vertex v. If DFS traversal doesn't visit all vertices,
#      then return false.
#   3) Reverse all arcs (or find transpose or reverse of graph)
#   4) Mark all vertices as not-visited in reversed graph.
#   5) Do a DFS traversal of reversed graph starting from same vertex v (Same as step 2).
#      If DFS traversal doesn't visit all vertices, then return false. Otherwise return true.
#
# The idea is, if every node can be reached from a vertex v, and every node can reach v, then the graph is strongly
# connected. In step 2, we check if all vertices are reachable from v. In step 4, we check if all vertices can reach v
# (In reversed graph, if all vertices are reachable from v, then all vertices can reach v in original graph).
#
# Note:
#   DFS of a graph with only one SCC always produces a tree.
#   The important point to note is DFS may produce a tree or a forest when there are more than one SCCs depending upon
# the chosen starting point.
#
# Kosaraju's algorithm - find all SCCs
#   1) Create an empty stack 'S' and do DFS traversal of a graph.
#      In DFS traversal, after calling recursive DFS for adjacent vertices of a vertex, push the vertex to stack.
#   2) Reverse directions of all arcs to obtain the transpose graph.
#   3) One by one pop a vertex from S while S is not empty. Let the popped vertex be 'v'.
#      Take v as source and do DFS (call DFSUtil(v)). The DFS starting from v prints strongly connected component of v.

from graph import Graph


class Solution(object):
    def is_strongly_connected(self, graph):
        """
        :param graph: Graph
        :return: Boolean
        """
        return graph.is_strongly_connected()

    def find_SCCs(self, graph):
        graph.printSCCs()


