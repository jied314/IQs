package DynamicProgramming

/**
 * Sample practise for Dynamic Programming
 * Solutions:
 * 1. Top-down with recursion
 *    O(2^N) Time Complexity & O(1) Space Complexity
 * 2. Top-down with recursion & memorization
 *    O(N) Time Complexity & O(N) Space Complexity
 * 3. Bottom-up with
 */
private fun getFibonacciNumberBottomUp(i: Int): Int {
    if (i <= 1) return 0
    if (i == 2) return 1

    var first = 0
    var second = 1
    for (j in 3..i) {
        val next = first + second
        first = second
        second = next
    }
    return second
}

private fun getFibonacciNumberTopDown(i: Int): Int {
    val visitedNumbers = mutableMapOf<Int, Int>()
    return getFibonacciNumberRecursive(i, visitedNumbers)
}

private fun getFibonacciNumberRecursive(i: Int, visitedNumbers: MutableMap<Int, Int>): Int {
    if (i <= 1) return 0
    if (i == 2) return 1

    if (!visitedNumbers.contains(i)) {
        visitedNumbers[i] = getFibonacciNumberRecursive(i-1, visitedNumbers) +
                getFibonacciNumberRecursive(i-2, visitedNumbers)
    }
    return visitedNumbers[i]!!
}

fun main() {
    println(getFibonacciNumberBottomUp(8))

    println(getFibonacciNumberTopDown(8))
}