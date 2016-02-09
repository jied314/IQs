# 2/8 - Graph
# Given a directed graph, find out whether the graph is strongly connected or not.
# A directed graph is strongly connected if there is a path between any two pair of vertices.
# It is easy for undirected graph, we can just do a BFS and DFS starting from any vertex. If BFS or DFS visits all
# vertices, then the given undirected graph is connected. This approach won't work for a directed graph.
#
# Refer to http://www.geeksforgeeks.org/connectivity-in-a-directed-graph/
# Solution - O(V+E)
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

class Solution(object):
    def
