package Heap

import java.util.*


/**
 * Given an array of meeting time intervals where intervals[i] = [starti, endi],
 * return the minimum number of conference rooms required.
 *
 * Solutions:
 * 1. Min Heap
 *    Allocate a new room based on the end time -> don't care which room gets freed up
 *    Min heap -> Sort intervals based on end time
 *    Time Complexity: O(N*LogN)
 *    Space Complexity: O(N)
 * 2. Chronological order
 *    When we encounter an ending event, that means that some meeting that started earlier has ended now.
 *    We are not really concerned with which meeting has ended. All we need is that some meeting ended thus making a room available.
 *    Time Complexity: O(N*LogN)
 *    Space Complexity: O(N)
 */

fun minMeetingRoomsHeap(intervals: Array<IntArray>): Int {
    intervals.sortBy { it[0] }
    val heap = PriorityQueue<Int>()
    heap.add(intervals[0][1])
    for (i in 1..<intervals.size) {
        val interval = intervals[i]
        if (interval[0] >= heap.peek()) {
            heap.remove()
        }
        heap.add(interval[1])
    }
    return heap.size
}

fun minMeetingRoomsChronologicalOrdering(intervals: Array<IntArray>): Int {

    // Check for the base case. If there are no intervals, return 0
    if (intervals.isEmpty()) return 0

    val start = IntArray(intervals.size)
    val end = IntArray(intervals.size)
    for (i in intervals.indices) {
        start[i] = intervals[i][0]
        end[i] = intervals[i][1]
    }

    // Sort the start and end chronologically
    start.sort()
    end.sort()

    // The two pointers in the algorithm: e_ptr and s_ptr.
    var sp = 0
    var ep = 0

    // Variables to keep track of maximum number of rooms used.
    var usedRooms = 0

    // Iterate over intervals.
    while (sp < intervals.size) {

        // If there is a meeting that has ended by the time the meeting at `start_pointer` starts
        if (start[sp] >= end[ep]) {
            usedRooms -= 1
            ep += 1
        }

        // We do this irrespective of whether a room frees up or not.
        // If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
        // remain the same in that case. If no room was free, then this would increase used_rooms
        usedRooms += 1
        sp += 1
    }
    return usedRooms
}

fun main() {
    val intervals = arrayOf(intArrayOf(0,30), intArrayOf(5,10), intArrayOf(15,20))
    println(minMeetingRoomsHeap(intervals))
    println(minMeetingRoomsChronologicalOrdering(intervals))
}