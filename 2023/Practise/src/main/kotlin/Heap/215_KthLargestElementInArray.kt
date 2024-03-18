package Heap

import java.util.*


/**
 * Given an integer array nums and an integer k, return the kth largest element in the array.
 * Note that it is the kth largest element in the sorted order, not the kth distinct element.
 *
 * Can you solve it without sorting?
 *
 * Solutions:
 * 1. Use approach 2, as discussed in LC explore.
 *    Time complexity: O(NlogK) & Space complexity: O(K)
 */

private fun findKthLargest2(nums: IntArray, k: Int): Int {
    // add K elements one by one to construct a min Heap with size K
    // use heapify to reduce time complexity to O(K)
    val heap = PriorityQueue<Int>(nums.slice(0..<k))

    // compare the remaining elements with the top of the heap.
    // if larger than the top, remove it and add the new element if necessary; else move onto the next.
    for (i in k..<nums.size) {
        if (nums[i] > heap.peek()) {
            heap.remove()
            heap.add(nums[i])
        }
    }
    // the top element is the Kth element.
    return heap.peek()
}

fun main() {
    println(findKthLargest2(intArrayOf(3, 2, 1, 5, 6, 4), 2))
}