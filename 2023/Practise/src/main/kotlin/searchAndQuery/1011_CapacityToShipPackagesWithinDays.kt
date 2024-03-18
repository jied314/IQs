package searchAndQuery

/**
 * A conveyor belt has packages that must be shipped from one port to another within days days.
 *
 * The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages
 * on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity
 * of the ship.
 *
 * Return the least weight capacity of the ship that will result in all the packages on the conveyor belt
 * being shipped within days days.
 *
 * Solution: Binary Search with range [max package weight, total package weight]
 * Time Complexity: O(N*LogN)
 * Space Complexity: O(1)
 */

fun shipWithinDays(weights: IntArray, days: Int): Int {
    var max = 0
    var total = 0
    for (weight in weights) {
        total += weight
        if (weight > max) max = weight
    }
    return bfs(weights, days, max, total)
}

fun bfs(weights: IntArray, days: Int, min: Int, max: Int): Int {
    var left = min
    var right = max
    while (left < right) {
        val mid = left + (right - left)/2
        if (isValid(weights, days, mid)) right = mid
        else left = mid+1
    }
    return left
}

private fun isValid(weights: IntArray, days: Int, capacity: Int): Boolean {
    var daysNeeded = 1
    var currLoad = 0
    for (weight in weights) {
        currLoad += weight
        if (currLoad > capacity) {
            daysNeeded++
            if (daysNeeded > days) return false
            currLoad = weight
        }
    }
    return true
}

fun main() {
    val weights1 = intArrayOf(1,2,3,4,5,6,7,8,9,10)
    println(shipWithinDays(weights1, 5))
}