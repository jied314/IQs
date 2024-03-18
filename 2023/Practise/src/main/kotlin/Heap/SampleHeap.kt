package Heap

import java.util.*

fun main() {
    val randomList = listOf(3, 1, 2)
    val randomCustomList = listOf(Pair(3, -3), Pair(1, -1), Pair(2, -2))

    // In Java/Kotlin, a Heap is represented by a Priority Queue
    // Construct an empty Min Heap
    val minHeap = PriorityQueue<Int>()
    minHeap.addAll(randomList)
    println(minHeap.peek())

    // Construct an empty Max Heap
    val maxHeap = PriorityQueue<Int>(Collections.reverseOrder())
    maxHeap.addAll(randomList)
    println(maxHeap.peek())

    // Construct a Heap with initial elements.
    // This process is named "Heapify".
    // The Heap is a Min Heap
    val heapWithValues = PriorityQueue<Int>(randomList)
    println(heapWithValues.peek())

    // Construct a Heap with custom data type
    val customMinHeap: Queue<Pair<Int, Int>> = PriorityQueue<Pair<Int, Int>>( compareBy { it.first })
    val customMaxHeap: Queue<Pair<Int, Int>> = PriorityQueue<Pair<Int, Int>> { a, b -> b.first - a.first }

    customMinHeap.addAll(randomCustomList)
    println(customMinHeap.peek())
    customMaxHeap.addAll(randomCustomList)
    println(customMaxHeap.peek())
}