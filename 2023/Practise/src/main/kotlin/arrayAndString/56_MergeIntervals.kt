package arrayAndString

/**
 * Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
 * and return an array of the non-overlapping intervals that cover all the intervals in the input.
 *
 * Solutions - Sort
 *    Time Complexity O(N*LogN) - O(NLogN) for sort and O(N) for linear traversal
 *    Space Complexity O(LogN) or O(N) for sorting. Storing result should not be included.
 *
 * Check if two intervals (a0,b0), (a1,b1) have overlap -> min(b0,b1) - max(a0,a1) >= 0 -> if intervals are sorted, a1>= a0
 * Merged intervals -> (min(a0,a1), max(b0,b1))
 */

private fun merge(intervals: Array<IntArray>): Array<IntArray> {
    intervals.sortBy { it[0] }
    val result = mutableListOf<IntArray>()
    for (interval in intervals) {
        // no overlap
        if (result.isEmpty() || result.last[1] < interval[0])
            result.add(interval)
        else {
            // there is an overlap, merge the interval
            result.last[1] = Math.max(result.last[1], interval[1])
        }
    }
    return result.toTypedArray()
}

fun main() {
    val intervals1 = arrayOf(intArrayOf(1,3),intArrayOf(2,6), intArrayOf(8,10), intArrayOf(15,18))
    for (interval in merge(intervals1)) {
        println(interval.contentToString())
    }
}