package Heap

import java.util.*


/**
 * There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).
 *
 * You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that
 * the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are
 * fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.
 *
 * Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.
 *
 * Solutions:
 * 1.
 */
fun carPoolingHeap(trips: Array<IntArray>, capacity: Int): Boolean {
    trips.sortBy { it[1] }
    val heap = PriorityQueue<Pair<Int, Int>>( compareBy { it.first } )
    var currCapacity = 0
    for (trip in trips) {
        while (heap.isNotEmpty() && trip[1] >= heap.peek().first) {
            val top = heap.remove()
            currCapacity -= top.second
        }
        currCapacity += trip[0]
        if (currCapacity > capacity) return false
        heap.add(Pair(trip[2], trip[0]))
    }
    return true
}

fun carPooling(trips: Array<IntArray>, capacity: Int): Boolean {
    val timestamp: MutableMap<Int, Int> = TreeMap()
    for (trip in trips) {
        val startPassenger = timestamp.getOrDefault(trip[1], 0) + trip[0]
        timestamp[trip[1]] = startPassenger
        val endPassenger = timestamp.getOrDefault(trip[2], 0) - trip[0]
        timestamp[trip[2]] = endPassenger
    }
    var usedCapacity = 0
    for (passengerChange in timestamp.values) {
        usedCapacity += passengerChange
        if (usedCapacity > capacity) {
            return false
        }
    }
    return true
}

fun main() {
    val trips = arrayOf(intArrayOf(2,1,5), intArrayOf(3,3,7))
    println(carPoolingHeap(trips, 4))
    println(carPooling(trips, 4))
}