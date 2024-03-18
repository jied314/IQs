package Graph

import kotlin.collections.ArrayDeque
import kotlin.collections.ArrayList
import kotlin.collections.HashMap
import kotlin.collections.MutableMap
import kotlin.collections.arrayListOf
import kotlin.collections.isNotEmpty
import kotlin.collections.mutableMapOf
import kotlin.collections.removeLast
import kotlin.collections.set

/**
 * Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
 *
 * Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
 *
 * Solutions:
 * 1. DFS - Iterative & Recursive
 *    O(V+E) Time Complexity & O(V) Space Complexity
 *
 * 2. BFS
 *    O(V+E) Time Complexity & O(V) Space Complexity
 */

// Definition for a Node.
class Node(var num: Int) {
    var neighbors = ArrayList<Node?>()
}

private fun cloneGraphIterativeDFS(node: Node?): Node? {
    if (node == null) return null

    val nodeCopyMap = mutableMapOf<Node, Node>()
    val stack = ArrayDeque<Node?>()
    stack.add(node)
    cloneNodeIfNecessary(node, nodeCopyMap)
    while (stack.isNotEmpty()) {
        val curr = stack.removeLast() ?: continue
        // clone its neighbors
        for (neighbor in curr.neighbors) {
            if (neighbor == null) continue
            if (!nodeCopyMap.containsKey(neighbor)) {
                stack.add(neighbor)
                cloneNodeIfNecessary(neighbor, nodeCopyMap)
            }
            nodeCopyMap[curr]!!.neighbors.add(nodeCopyMap[neighbor])
        }
    }
    return nodeCopyMap[node]
}

private fun cloneNodeIfNecessary(node: Node, nodeCopyMap: MutableMap<Node, Node>): Node {
    if (nodeCopyMap.containsKey(node)) return nodeCopyMap[node]!!
    val nodeCopy = Node(node.num)
    nodeCopy.neighbors = ArrayList()
    nodeCopyMap[node] = nodeCopy
    return nodeCopy
}

private fun cloneGraphRecursiveDFS(node: Node?): Node? {
    return cloneGraphRecursiveDFS(node, mutableMapOf())
}

private fun cloneGraphRecursiveDFS(node: Node?, nodeCopyMap: MutableMap<Node, Node>): Node? {
    if (node == null) return null
    if (nodeCopyMap.containsKey(node)) return nodeCopyMap[node]

    val nodeCopy = Node(node.num)
    nodeCopy.neighbors = ArrayList()
    nodeCopyMap[node] = nodeCopy

    for (neighbor in node.neighbors) {
        nodeCopy.neighbors.add(cloneGraphRecursiveDFS(neighbor))
    }
    return nodeCopy
}

private fun cloneGraphBFS(node: Node?): Node? {
    if (node == null) return node

    // Hash map to save the visited node and it's respective clone
    // as key and value respectively. This helps to avoid cycles.
    val visited = HashMap<Node?, Node?>()

    // Put the first node in the queue
    val queue = ArrayDeque<Node?>()
    queue.add(node)
    // Clone the node and put it in the visited dictionary.
    val nodeCopy = Node(node.num)
    nodeCopy.neighbors = ArrayList()
    visited[node] = nodeCopy

    // Start BFS traversal
    while (!queue.isEmpty()) {
        // Pop a node from the front of the queue.
        val curr = queue.removeFirst() ?: continue
        // Iterate through all the neighbors of the current node
        for (neighbor in curr.neighbors) {
            if (neighbor == null) continue
            if (!visited.containsKey(neighbor)) {
                // Clone the neighbor and put in the visited, if not present already
                val neighborCopy = Node(neighbor.num)
                neighborCopy.neighbors = ArrayList()
                visited[neighbor] = neighborCopy
                // Add the newly encountered node to the queue.
                queue.add(neighbor)
            }
            // Add the clone of the neighbor to the neighbors of the clone node "n".
            visited[curr]!!.neighbors.add(visited[neighbor])
        }
    }

    // Return the clone of the node from visited.
    return visited[node]
}

fun main() {
    val node1 = Node(1)
    val node2 = Node(2)
    val node3 = Node(3)
    val node4 = Node(4)
    node1.neighbors = arrayListOf(node2, node4)
    node2.neighbors = arrayListOf(node1, node3)
    node3.neighbors = arrayListOf(node2, node4)
    node4.neighbors = arrayListOf(node1, node3)

    cloneGraphIterativeDFS(node1)
    cloneGraphRecursiveDFS(node1)
}