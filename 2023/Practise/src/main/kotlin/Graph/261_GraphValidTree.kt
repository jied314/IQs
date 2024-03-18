package Graph

import java.util.*
import kotlin.collections.ArrayDeque


/**
 * You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where
 * edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
 *
 * Return true if the edges of the given graph make up a valid tree, and false otherwise.
 *
 * Key point - A graph G is a tree iff the following two conditions are met:
 *     1. G is fully connected. In other words, for every pair of nodes in G, there is a path between them.
 *     2. G contains no cycles. In other words, there is exactly one path between each pair of nodes in G.
 *
 * Solutions:
 * 1. UnionFind
 *    O(1) Time Complexity & O(1) Space Complexity
 *
 * 2. DFS (Iterative & Recursive)
 *    Key: Build an adjacency list and remember parent to avoid trivial cycle (a->b->a)
 *    O(V+E) Time Complexity & O(V+E) Space Complexity
 *
 * 3. Advanced graph theory -> proves the keys points below
 *    a. For the graph to be a valid tree, it must have exactly n - 1 edges. Any less, it can't possibly be
 *       fully connected. And more, it has to contain cycles.
 *    b. Additionally, if the graph is fully connected and contains exactly n - 1 edges, it can't possibly contain
 *       a cycle, and therefore must be a tree!
 *    O(V) Time Complexity & O(V) Space Complexity
 */

private fun validTreeUnionFind(n: Int, edges: Array<IntArray>): Boolean {
    val uf = UnionFind(n)
    for ((a, b) in edges) {
        if (!uf.connected(a, b)) uf.union(a, b)
        else return false
    }
    return uf.getNumGroups() == 1
}

private fun validTreeIterativeDFS(n: Int, edges: Array<IntArray>): Boolean {
    val adjacencyList = Array<MutableList<Int>>(n) { mutableListOf() }
    for (edge in edges) {
        adjacencyList[edge[0]].add(edge[1])
        adjacencyList[edge[1]].add(edge[0])
    }

    val parent: MutableMap<Int, Int> = HashMap()
    val stack = ArrayDeque<Int>()
    parent[0] = -1
    stack.add(0)
    while (!stack.isEmpty()) {
        val node = stack.removeLast()
        for (neighbour in adjacencyList[node]) {
            if (parent[node] == neighbour) { // avoid trivial cycle
                continue
            }
            if (parent.containsKey(neighbour)) { // detects cycle
                return false
            }
            stack.add(neighbour)
            parent[neighbour] = node
        }
    }
    return parent.size == n
}

private val adjacencyList: MutableList<MutableList<Int>> = ArrayList()
private val seen: MutableSet<Int> = HashSet()
fun validTreeRecursiveDFS(n: Int, edges: Array<IntArray>): Boolean {
    if (edges.size != n - 1) return false
    for (i in 0 until n) {
        adjacencyList.add(ArrayList())
    }
    for (edge in edges) {
        adjacencyList[edge[0]].add(edge[1])
        adjacencyList[edge[1]].add(edge[0])
    }

    // We return true iff no cycles were detected,
    // AND the entire graph has been reached.
    return dfs(0, -1) && seen.size == n
}

private fun dfs(node: Int, parent: Int): Boolean {
    if (seen.contains(node)) return false
    seen.add(node)
    for (neighbour in adjacencyList[node]) {
        if (parent != neighbour) { // avoid trivial cycle a->b->a
            if (!dfs(neighbour, node)) return false
        }
    }
    return true
}

private fun validTreeAdvancedTheoryIterativeDFS(n: Int, edges: Array<IntArray>): Boolean {
    if (edges.size != n - 1) return false

    // Make the adjacency list - O(E)
    val adjacencyList = Array<MutableList<Int>>(n) { mutableListOf() }
    for (edge in edges) {
        adjacencyList[edge[0]].add(edge[1])
        adjacencyList[edge[1]].add(edge[0])
    }

    val stack = ArrayDeque<Int>()
    val seen: MutableSet<Int> = HashSet()
    stack.add(0)
    seen.add(0)
    while (!stack.isEmpty()) {
        val node = stack.removeLast()
        for (neighbour in adjacencyList[node]) {
            if (seen.contains(neighbour)) continue
            seen.add(neighbour)
            stack.add(neighbour)
        }
    }

    return seen.size == n
}

fun main () {
    val treeEdges = arrayOf(intArrayOf(0, 1), intArrayOf(0, 2), intArrayOf(0, 3), intArrayOf(1, 4))
    println(validTreeUnionFind(5, treeEdges))
    println(validTreeIterativeDFS(5, treeEdges))
    println(validTreeRecursiveDFS(5, treeEdges))
    println(validTreeAdvancedTheoryIterativeDFS(5, treeEdges))

    val nonTreeEdges = arrayOf(intArrayOf(0, 1), intArrayOf(1, 2), intArrayOf(2, 3), intArrayOf(1, 3), intArrayOf(1, 4))
    println(validTreeUnionFind(5, nonTreeEdges))
    println(validTreeIterativeDFS(5, nonTreeEdges))
    println(validTreeRecursiveDFS(5, nonTreeEdges))
    println(validTreeAdvancedTheoryIterativeDFS(5, nonTreeEdges))
}