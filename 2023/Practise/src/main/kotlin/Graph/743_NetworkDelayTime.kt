package Graph

import java.util.*

/**
 * You are given a network of n nodes, labeled from 1 to n.
 * You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi),
 * where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel
 * from source to target.
 *
 * We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to
 * receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
 *
 * Solutions:
 * 1. Dijkstra
 *    1.1 Use a PriorityQueue to traverse the nodes in increasing order of the time required to reach them.
 *    1.2 In each iteration, visit the node with the shortest travel time. This will help us in finding the
 *        fastest time path first.
 *    Time Complexity: O(V + E*LogV)
 *      O(V) for traversing the array to find the min time
 *      O(LogV) for interactions with Heap, and for each edge there maybe E interactions.
 *    Space Complexity: O(V + E)
 *      O(E) for storing the adjacency list
 *      O(E) for Heap because all edges can be added into the heap
 *      O(V) for signalReceivedAt
 */

private fun networkDelayTime(times: Array<IntArray>, n: Int, k: Int): Int {
    // Build the adjacency list
    val adjacencyList: MutableMap<Int, MutableList<Pair<Int, Int>>> = mutableMapOf()
    for ((source, dest, travelTime) in times) {
        adjacencyList.putIfAbsent(source, mutableListOf())
        adjacencyList[source]!!.add(Pair(travelTime, dest))
    }

    // prepare for Dijkstra - array size N+1 since node is 1-based.
    val signalReceivedAt = IntArray(n+1) { Int.MAX_VALUE }
    dijkstra(k, signalReceivedAt, adjacencyList)

    signalReceivedAt[0] = Int.MIN_VALUE
    val longestTime = signalReceivedAt.max()

    // INT_MAX signifies at least one node is unreachable
    return if (longestTime == Int.MAX_VALUE) -1 else longestTime
}

private fun dijkstra(source: Int, signalReceivedAt: IntArray, adjacencyList: MutableMap<Int, MutableList<Pair<Int, Int>>>) {
    // used to store the shortest distance so far, from source to each node
    val heap: Queue<Pair<Int, Int>> = PriorityQueue<Pair<Int, Int>>( compareBy { it.first }) // default is min heap
    heap.add(Pair(0, source))
    signalReceivedAt[source] = 0 // Time for starting node is 0

    while (!heap.isEmpty()) {
        // ensure always visit the node closest to source
        val (currTotalTime, currNode) = heap.remove()

        // the first time visiting the node must be the shortest to the node, subsequent ones are longer and should skip
        // if already reached earlier, skip -> ensure not revisit the same node if already the shortest
        if (currTotalTime > signalReceivedAt[currNode]) continue

        // no out-going edges, skip the node
        if (!adjacencyList.containsKey(currNode)) continue
        // Broadcast the signal to adjacent nodes
        for ((neighborTime, neighborNode) in adjacencyList[currNode]!!) {
            // Only store the earliest signal receiving time so far for neighborNode,
            // and if is a shorter time, add to the heap
            if (signalReceivedAt[neighborNode] > currTotalTime + neighborTime) {
                signalReceivedAt[neighborNode] = currTotalTime + neighborTime
                heap.add(Pair(signalReceivedAt[neighborNode], neighborNode))
            }
        }
    }
}

fun main() {
    val times1 = arrayOf(intArrayOf(2,1,1), intArrayOf(2,3,1), intArrayOf(3,4,1))
    println(networkDelayTime(times1, 4, 2))

    val times2 = arrayOf(intArrayOf(1,2,1))
    println(networkDelayTime(times2, 2, 1))

    val times3 = arrayOf(intArrayOf(1,2,1))
    println(networkDelayTime(times3, 2, 2))
}


