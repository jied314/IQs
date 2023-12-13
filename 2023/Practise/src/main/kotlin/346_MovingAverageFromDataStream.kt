/**
 * Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
 *
 * Implement the MovingAverage class:
 *     MovingAverage(int size) Initializes the object with the size of the window size.
 *     double next(int val) Returns the moving average of the last size values of the stream.
 *
 * Example:
 * Input
 *     ["MovingAverage", "next", "next", "next", "next"]
 *     [[3], [1], [10], [3], [5]]
 * Output
 *     [null, 1.0, 5.5, 4.66667, 6.0]
 * Explanation
 *     MovingAverage movingAverage = new MovingAverage(3);
 *     movingAverage.next(1); // return 1.0 = 1 / 1
 *     movingAverage.next(10); // return 5.5 = (1 + 10) / 2
 *     movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
 *     movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
 */

class MovingAverage(size: Int) {

    private val data = ArrayDeque<Int> (size)
    private val capacity = size
    private var windowSum: Int = 0

    // O(1) Time Complexity & O(N) Space Complexity
    fun next(num: Int): Double {
        if (data.size == capacity) {
            val firstValue = data.removeFirst()
            windowSum -= firstValue
        }
        data.add(num)
        windowSum += num
        return windowSum.toDouble() / data.size
    }

    // O(N) Time Complexity since recalculate sum each time
    fun nextNotFast(num: Int): Double {
        if (data.size == capacity) data.removeFirst()
        data.add(num)
        return data.average()
    }

}

fun main() {
    val ma = MovingAverage(3)
    println(ma.next(1))
    println(ma.next(10))
    println(ma.next(3))
    println(ma.next(5))
}