package Graph

import java.util.*

/**
 * There are n cities connected by some number of flights. You are given an array flights where
 * flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
 *
 * You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops.
 * If there is no such route, return -1.
 *
 * Solutions:
 *
 */
data class Route(val dst: Int, var minCost: Int, var steps: Int)
private fun findCheapestPrice(n: Int, flights: Array<IntArray>, src: Int, dst: Int, k: Int): Int {
    // build adjacency list
    val adj = mutableMapOf<Int, MutableList<Pair<Int, Int>>>()
    for ((from, to, cost) in flights) {
        adj.putIfAbsent(from, mutableListOf())
        adj[from]!!.add(Pair(to, cost))
    }

    // prepare dijkstra
    val minSteps = IntArray(n) { Int.MAX_VALUE }
    val heap = PriorityQueue<Route>(compareBy { it.minCost })
    minSteps[src] = 0
    heap.add(Route(src, 0, 0))

    while (heap.isNotEmpty()) {
        val (currNode, currCost, currSteps) = heap.remove()

        // already visited this node with cheaper price and fewer steps
        if (currSteps > minSteps[currNode]) continue
        // cannot reach within k+1 steps (k+1 step == k stops)
        if (currSteps > k+1) continue

        // record min steps for currNode, note this must be the cheapest price for currSteps since this is a heap
        minSteps[currNode] = currSteps

        // the first time we reach dst, can return since greedily choosing the node with the lowest total price
        if (currNode == dst) return currCost

        // no out-going edges, skip the node
        if (!adj.containsKey(currNode)) continue
        for ((neighborCity, cost) in adj[currNode]!!) {
            heap.add(Route(neighborCity, currCost+cost, currSteps+1))
        }
    }
    return -1
}

fun main() {
    val flights1 = arrayOf(intArrayOf(0,1,100), intArrayOf(1,2,100), intArrayOf(2,0,100), intArrayOf(1,3,600), intArrayOf(2,3,200))
    println(findCheapestPrice(4, flights1, 0, 3, 1))

    val flights2 = arrayOf(intArrayOf(0,1,100), intArrayOf(1,2,100), intArrayOf(0,2,500))
    println(findCheapestPrice(3, flights2, 0, 2, 1))

    val flights3 = arrayOf(intArrayOf(0,1,100), intArrayOf(1,2,100), intArrayOf(0,2,500))
    println(findCheapestPrice(3, flights3, 0, 2, 0))

    val flights4 = arrayOf(intArrayOf(0,1,2), intArrayOf(1,2,1), intArrayOf(2,0,10))
    println(findCheapestPrice(3, flights4, 1, 2, 1))
}