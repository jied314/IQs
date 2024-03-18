package StackAndQueue

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
 * 2. Array with optimized space
 *    Iterate backwards through the array, and move forwards to find the number of days until a warmer day.
 *    O(N) Time Complexity & O(1) Space Complexity
 */
private fun dailyTemperaturesStack(temperatures: IntArray): IntArray {
    val stack = ArrayDeque<Int>()
    val result = IntArray(temperatures.size)
    for (i in temperatures.indices) {
        // pop until stack not have elements with lower temperatures
        while (stack.isNotEmpty() && temperatures[i] > temperatures[stack.last()]) {
            val lastIndex = stack.removeLast()
            result[lastIndex] = i - lastIndex
        }
        // Because the problem is asking for the number of days, instead of storing the temperatures themselves,
        // store the indices of the days, and use temperatures[i] to find the temperature of the ith day.
        stack.add(i)
    }
    return result
}

private fun dailyTemperaturesArray(temperatures: IntArray): IntArray {
    var hottest = 0
    val answer = IntArray(temperatures.size)
    for (currDay in temperatures.size-1 downTo 0) {
        val currTemp = temperatures[currDay]
        // skip if hottest temp -> answer[currDay] = 0
        if (currTemp >= hottest) {
            hottest = currTemp
            continue
        }
        var days = 1
        while (temperatures[currDay + days] <= currTemp) {
            // Use information from answer to search for the next warmer day
            days += answer[currDay + days]
        }
        answer[currDay] = days
    }
    return answer
}

fun main() {
    val temperatures = intArrayOf(73,74,75,71,69,72,76,73)
    println(dailyTemperaturesStack(temperatures).contentToString())
    println(dailyTemperaturesArray(temperatures).contentToString())
}