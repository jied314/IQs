package Graph

/**
 * There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
 * The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes
 * a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge,
 * and no vertex has an edge to itself.
 *
 * You want to determine if there is a valid path that exists from vertex source to vertex destination.
 *
 * Given edges and the integers n, source, and destination, return true if there is a valid path from source
 * to destination, or false otherwise.
 *
 * Solutions:
 * 1. DFS - recursive & iterative
 *    Time Complexity O(V+E) & Space Complexity O(V+E)
 *    O(E) for building adjacency matrix and O(V) for iterate on the nodes
 * 2. BFS - Time Complexity O(V+E) & Space Complexity O(V+E)
 * 3. Union Find
 */
private fun validPath(n: Int, edges: Array<IntArray>, source: Int, destination: Int): Boolean {
    val adjacencyMatrix = Array<MutableList<Int>>(n) { mutableListOf() }
    for ((i, j) in edges) {
        adjacencyMatrix[i].add(j)
        adjacencyMatrix[j].add(i)
    }
    val seen = BooleanArray(n) { false }
    return validPathDFSIterative(adjacencyMatrix, seen, source, destination)
}

private fun validPathDFSRecursive(adjacencyMatrix: Array<MutableList<Int>>, seen: BooleanArray, source: Int, destination: Int): Boolean {
    if (source == destination) return true
    if (seen[source]) return false
    seen[source] = true
    for (next in adjacencyMatrix[source]) {
        if (validPathDFSRecursive(adjacencyMatrix, seen, next, destination)) return true
    }
    return false
}

private fun validPathDFSIterative(adjacencyMatrix: Array<MutableList<Int>>, seen: BooleanArray, source: Int, destination: Int): Boolean {
    val stack = ArrayDeque<Int> ()
    stack.add(source)
    while (stack.isNotEmpty()) {
        val curr = stack.removeLast()
        if (curr == destination) return true
        if (seen[curr]) continue
        seen[curr] = true
        for (next in adjacencyMatrix[curr]) {
            stack.add(next)
        }
    }
    return false
}

private fun validPathBFS(adjacencyMatrix: Array<MutableList<Int>>, seen: BooleanArray, source: Int, destination: Int): Boolean {
    val queue = ArrayDeque<Int> ()
    queue.add(source)
    while (queue.isNotEmpty()) {
        val curr = queue.removeFirst()
        if (curr == destination) return true
        for (next in adjacencyMatrix[curr]) {
            if (!seen[next]) {
                seen[next] = true
                queue.add(next)
            }
        }
    }
    return false
}

fun main() {
    val graph1 = arrayOf(intArrayOf(0, 1), intArrayOf(1, 2), intArrayOf(2, 0))
    println(validPath(3, graph1, 0, 2))

    val graph2 = arrayOf(intArrayOf(0, 1), intArrayOf(0, 2), intArrayOf(3, 5), intArrayOf(5, 4), intArrayOf(4, 3))
    println(validPath(6, graph2, 0, 5))
}