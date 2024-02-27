package Graph

import kotlin.collections.ArrayDeque


/**
 * There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
 * You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must
 * take course bi first if you want to take course ai.
 *
 * For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
 * Return the ordering of courses you should take to finish all courses.
 * If there are many valid answers, return any of them.
 * If it is impossible to finish all courses, return an empty array.
 *
 * Solution:
 * 1. Topological sort - iterate over all nodes with 0 in-degree and successful if visited all nodes.
 *    Time Complexity O(V+E) & Space Complexity O(V+E)
 * 2. DFS
 *      Iterate over all nodes and finish recursion once reaching node W/O outgoing edges
 *      Produce reversed topological order.
 *      Track node states - NOT_VISITED, VISITING & VISITED to help detect cycles
 *    Time Complexity O(V+E) & Space Complexity O(V+E)
 */

private fun findOrderTopologicalSort(numCourses: Int, prerequisites: Array<IntArray>): IntArray {
    val topologicalOrder = mutableListOf<Int>() // O(V)
    val zeroInDegreeQueue = ArrayDeque<Int>()   // O(V)
    val inDegreeCount = IntArray(numCourses) { 0 }

    // Create the adjacency list representation of the graph - O(E)
    // Use map if value not fit for array
    val adjacencyList = Array<MutableList<Int>>(numCourses) { mutableListOf() } // O(E)
    for ((post, pre) in prerequisites) {
        adjacencyList[pre].add(post)
        inDegreeCount[post]++
    }

    // Add all vertices with 0 in-degree to the queue - O(V)
    inDegreeCount.forEachIndexed { index, inDegree ->
        if (inDegree == 0) zeroInDegreeQueue.add(index)
    }

    // Process until the Q becomes empty - O(V)
    while (zeroInDegreeQueue.isNotEmpty()) {
        val pre = zeroInDegreeQueue.removeFirst()
        topologicalOrder.add(pre)

        // Reduce the in-degree of each neighbor by 1
       for (post in adjacencyList[pre]) {
            inDegreeCount[post]--
            // If in-degree of a neighbor becomes 0, add it to the Q
            if (inDegreeCount[post] == 0) zeroInDegreeQueue.add(post)
        }
    }

    // Topological sort is possible if iterated over all nodes
    return if (topologicalOrder.count() == numCourses) topologicalOrder.toIntArray() else IntArray(0)
}

private const val NOT_VISITED = 0
private const val VISITING = 1
private const val VISITED = 2
private var isPossible: Boolean = true
private fun findOrderDFS(numCourses: Int, prerequisites: Array<IntArray>): IntArray {
    // Create the adjacency list representation of the graph - O(E)
    val adjacencyList = Array<MutableList<Int>>(numCourses) { mutableListOf() } // O(E)
    for ((post, pre) in prerequisites) {
        adjacencyList[pre].add(post)
    }

    val order = mutableListOf<Int>() // O(V)
    val colors = IntArray(numCourses) { NOT_VISITED }
    for (i in 0..<numCourses) {
        if (colors[i] == NOT_VISITED) dfs(i, colors, adjacencyList, order)
    }

    return if (isPossible) order.asReversed().toIntArray() else IntArray(0)
}

private fun dfs(node: Int, colors: IntArray, adjList: Array<MutableList<Int>>, order: MutableList<Int>) {
    // Don't recurse further if we found a cycle already
    if (!isPossible) return

    // Start the recursion
    colors[node] = VISITING

    // Traverse on neighboring vertices
    for (neighbor in adjList[node]) {
        if (colors[neighbor] == NOT_VISITED) {
            dfs(neighbor, colors, adjList, order)
        } else if (colors[neighbor]== VISITING) {
            // An edge to a VISITING vertex represents a cycle
            isPossible = false
        }
    }

    // Recursion ends. We mark the node as VISITED
    colors[node] = VISITED
    order.add(node)
}

fun main() {
    val prerequisites1 = arrayOf(intArrayOf(1, 0))
    println(findOrderTopologicalSort(2, prerequisites1).contentToString())
    println(findOrderDFS(2, prerequisites1).contentToString())

    val prerequisites2 = arrayOf(intArrayOf(1, 0), intArrayOf(2, 0), intArrayOf(3, 1), intArrayOf(3, 2))
    println(findOrderTopologicalSort(4, prerequisites2).contentToString())
    println(findOrderDFS(4, prerequisites2).contentToString())
}
