/**
 * Sample practise for Dynamic Programming
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

    if (visitedNumbers.contains(i)) {
        visitedNumbers[i]?.let {
            return it
        }
    }
    val result = getFibonacciNumberRecursive(i-1, visitedNumbers) +
            getFibonacciNumberRecursive(i-2, visitedNumbers)
    visitedNumbers[i] = result
    return result
}

fun main() {
    println(getFibonacciNumberBottomUp(8))

    println(getFibonacciNumberTopDown(8))
}