/**
 * Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
 * The returned integer should be non-negative as well.
 *
 * You must not use any built-in exponent function or operator.
 *
 * Example:
 *
 * Input: x = 8
 * Output: 2
 * Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 *
 * Solutions:
 * 1. Use Binary Search - O(LogN) Time Complexity & O(1) Space Complexity
 *    Note: Handle integer overflow
 * 2. Bit shift based on Sqrt(X) = 2 * Sqrt(X/4)
 * 3. Use existing function Sqrt(X) = Math.e^(0.5 * LogX)
 */
private fun squareRootBS(x: Int) : Int {
    if (x < 2) return x

    var left = 2
    var right = x / 2
    while (left <= right) {
        val mid = (left + right) / 2
        // need to convert to Long to avoid integer overflow
        val square = mid.toLong() * mid
        if (square > x) right = mid - 1
        else if (square < x) left = mid + 1
        else return mid
    }
    return right
}

private fun squareRootBitShift(x: Int): Int {
    if (x < 2) return x

    val left = squareRootBitShift(x shr 2) shl 1
    val right = left + 1
    return if (right.toLong() * right > x) left else right
}

fun main() {
    println(squareRootBS(2147395599))
}