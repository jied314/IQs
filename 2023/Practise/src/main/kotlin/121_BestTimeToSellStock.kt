import kotlin.math.max

/**
 * You are given an array prices where prices[i] is the price of a given stock on the ith day.
 *
 * You want to maximize your profit by choosing a single day to buy one stock and
 * choosing a different day in the future to sell that stock.
 *
 * Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
 *
 * Input: prices = [7,1,5,3,6,4]
 * Output: 5
 *
 * Solutions:
 * 1. Brute Force
 *    O(N*N) Time Complexity & O(1) Space Complexity
 * 2. One Pass - find the lowest valley (min) and calculate the largest increase after the valley (max profit)
 *    O(N) Time Complexity & O(1) Space Complexity
 */
private fun maxProfitBruteForce(prices: IntArray): Int {
    if (prices.size < 2) return 0

    var maxProfit = 0
    var i = 0
    while (i < (prices.size - 1)) {
        var j = i+1
        while (j < prices.size) {
            if (prices[j] > prices[i]) {
                maxProfit = max(maxProfit, prices[j] - prices[i])
            }
            j++
        }
        i++
    }
    return maxProfit
}

private fun maxProfitOnePass(prices: IntArray): Int {
    var minPrice = Int.MAX_VALUE
    var maxProfit = 0
    for (i in prices.indices) {
        if (prices[i] < minPrice) { // find the lowest valley
            minPrice = prices[i]
        } else if (prices[i] - minPrice > maxProfit)  { // find the largest peak after the valley
            maxProfit = prices[i] - minPrice
        }
    }
    return maxProfit
}

fun main() {
    val prices = intArrayOf(7,1,5,3,6,4)
    println(maxProfitOnePass(prices))
}