/**
 * Given an array of integers temperatures represents the daily temperatures, return an array answer such that
 * answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
 * If there is no future day for which this is possible, keep answer[i] == 0 instead.
 *
 * Example:
 *     Input: temperatures = [73,74,75,71,69,72,76,73]
 *     Output: [1,1,4,2,1,1,0,0]
 *
 * Solutions:
 * 1. Monotonic Stack - always sorted stack
 *    O(N) Time Complexity & O(N) Space Complexity
 * 2.
 */
private fun dailyTemperatures(temperatures: IntArray): IntArray {
    val stack = ArrayDeque<Int>()
    val result = IntArray(temperatures.size)
    for (i in temperatures.indices) {
        // pop until stack not have elements with lower temperatures
        while (stack.isNotEmpty() && temperatures[i] > temperatures[stack.last()]) {
            val prev = stack.removeLast()
            result[prev] = i - prev
        }
        stack.add(i)
    }
    return result
}

fun main() {
    val temperatures = intArrayOf(73,74,75,71,69,72,76,73)
    println(dailyTemperatures(temperatures).contentToString())

    val a = ArrayDeque<Int>()
    a.removeLast()
}