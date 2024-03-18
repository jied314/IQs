package Heap

import java.util.PriorityQueue

fun mostBooked(n: Int, meetings: Array<IntArray>): Int {
    meetings.sortBy { it[0] }
    val heap = PriorityQueue<Pair<Int, Int>>()
    heap.add(Pair(meetings[0][1], 0))

    var result = 0
    var maxMeeting = 1
    val meetingCount = IntArray(n)
    meetingCount[0] = 1
    for (i in 1..meetings.size) {
        val interval = meetings[i]
        val top = heap.peek()
        if (interval[0] < top.first) { // need a new room
            var room = top.second
            if (heap.size < n) { // assign a new room
//                room = meetingCount
            } else { // delay meeting for a new room

            }
//            heap.add(room)
        }

    }
    return result
}