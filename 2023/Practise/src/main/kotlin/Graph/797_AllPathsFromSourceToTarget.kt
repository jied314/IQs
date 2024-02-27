package Graph

/**
 * Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths
 * from node 0 to node n - 1 and return them in any order.
 *
 * The graph is given as follows: graph[i] is a list of all nodes you can visit from node i
 * (i.e., there is a directed edge from node i to node graph[i][j]).
 *
 * Solutions:
 * 1. Backtracking - similar to DFS, but produce in-order results
 *    O(2^N * N) Time Complexity
 *    O(2^N * N) Space Complexity - O(N) Recursion stack * O(2^N) per stack
 * 2. DFS - produce reversed order results
 * 3. BFS - weird, not fully understand
 * 4. Dynamic Programming
 *
 */


private fun allPathsSourceTargetBacktracking(graph: Array<IntArray>): List<List<Int>> {
    val results: MutableList<List<Int>> = ArrayList()
    // adopt the LinkedList for fast access to the tail element.
    val path = ArrayDeque<Int>()
    path.add(0)
    // kick of the backtracking, starting from the source (node 0)
    backtrack(0, graph.size - 1, path, graph, results)
    return results
}

private fun backtrack(currNode: Int, target: Int, path: ArrayDeque<Int>, graph: Array<IntArray>, results: MutableList<List<Int>>) {
    if (currNode == target) {
        // Note: one should make a deep copy of the path
        results.add(ArrayList(path))
        return
    }
    // explore the neighbor nodes one after another.
    for (nextNode in graph[currNode]) {
        // mark the choice, before backtracking.
        path.add(nextNode)
        backtrack(nextNode, target, path, graph, results)
        // remove the previous choice, to try the next choice
        path.removeLast()
    }
}

private fun allPathsSourceTargetDFS(graph: Array<IntArray>): List<List<Int>> {
    return dfsPath(0, graph.size-1, mutableMapOf(), graph).map { it.reversed() }
}

private fun dfsPath(start: Int, target: Int, visited: MutableMap<Int, MutableList<MutableList<Int>>>, graph: Array<IntArray>): MutableList<MutableList<Int>> {
    if (visited.containsKey(start)) return visited[start]!!
    if (start == target) return mutableListOf(mutableListOf(target))

    val result = mutableListOf<MutableList<Int>>()
    for (next in graph[start]) {
        val nextPaths = dfsPath(next, target, visited, graph)
        if (nextPaths.isEmpty()) continue
        for (path in nextPaths) {
            val pathCopy = path.toMutableList()
            pathCopy.add(start)
            result.add(pathCopy)
        }
    }
    if (result.isNotEmpty()) visited[start] = result
    return result
}

fun main() {
    val graph1 = arrayOf(intArrayOf(1,2), intArrayOf(3), intArrayOf(3), intArrayOf())
    println(allPathsSourceTargetBacktracking(graph1))
    println(allPathsSourceTargetDFS(graph1))

    val graph2 = arrayOf(intArrayOf(4,3,1),intArrayOf(3,2,4),intArrayOf(3),intArrayOf(4),intArrayOf())
    println(allPathsSourceTargetBacktracking(graph2))
    println(allPathsSourceTargetDFS(graph2))
}
