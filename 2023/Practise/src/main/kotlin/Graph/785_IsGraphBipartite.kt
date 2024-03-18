package Graph

/**
 * There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1.
 * You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to.
 * More formally, for each v in graph[u], there is an undirected edge between node u and node v.
 * The graph has the following properties:
 *     1. There are no self-edges (graph[u] does not contain u).
 *     2. There are no parallel edges (graph[u] does not contain duplicate values).
 *     3. If v is in graph[u], then u is in graph[v] (the graph is undirected).
 *     4. The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
 *     5. A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that
 *        every edge in the graph connects a node in set A and a node in set B.
 *
 * Return true if and only if it is bipartite.
 *
 * Solutions:
 *  DFS - use a color array to track states (visited or which set it belongs to)
 *  Time Complexity O(V + E) - visit all nodes and edges
 *  Space Complexity O(N) for storing color array
 */

private const val GREY = 0
private const val RED = 1
private const val BLUE = -1

private fun isBipartite(graph: Array<IntArray>): Boolean {
    val count = graph.size
    val colors = IntArray(count) { GREY }

    for (i in graph.indices) {
        if (colors[i] != GREY) continue // skip already colored nodes
        val stack = ArrayDeque<Int>()
        stack.add(i)
        colors[i] = RED
        while (stack.isNotEmpty()) {
            val node = stack.removeLast()
            for (neighbor in graph[node]) {
                if (colors[neighbor] == GREY) { // un-visited node
                    stack.add(neighbor)
                    colors[neighbor] = colors[node] * BLUE
                } else if (colors[neighbor] == colors[node]) {
                    return false
                }
            }
        }
    }
    return true
}

fun main() {
    val graph1 = arrayOf(intArrayOf(1), intArrayOf(0), intArrayOf(4), intArrayOf(4), intArrayOf(2,3))
    println(isBipartite(graph1))
}
