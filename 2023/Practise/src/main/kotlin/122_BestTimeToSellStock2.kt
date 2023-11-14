/**
 * You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
 *
 * On each day, you may decide to buy and/or sell the stock.
 * You can only hold at most one share of the stock at any time.
 * However, you can buy it then immediately sell it on the same day.
 *
 * Find and return the maximum profit you can achieve.
 *
 * Input: prices = [7,1,5,3,6,4]
 * Output: 7
 * Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
 *              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
 *              Total profit is 4 + 3 = 7.
 *
 * Solutions:
 * 1. Brute Force with Recursion
 *    Calculate all possible set of combinations and find the max profit using Recursion.
 *    O(N^N) Time Complexity due to the recursion. O(1) Space Complexity
 *
 * 2. Peak Valley Approach
 *    Maximize the profit by considering every peak immediately following a valley.
 *    Cannot skip any peak since missing one transaction leading to a lesser overall profit.
 *    O(N) Time Complexity & O(1) Space Complexity
 *
 * 3. One Pass
 *    Based on Peak Valley approach. But instead of tracking peak and valley, just summing up all profits if
 *  there is a price increase.
 *    O(N) Time Complexity & O(1) Space Complexity
 */
private fun maxProfitRecursive(prices: IntArray): Int {
    return calculate(prices, 0)
}

private fun calculate(prices: IntArray, startIndex: Int): Int {
    if (startIndex >= prices.size) return 0 // Recursion End Condition

    var max = 0
    for (i in startIndex..<prices.size) {
        var maxProfit = 0
        for (j in i + 1..<prices.size) {
            if (prices[j] > prices[i]) {
                val profit = calculate(prices, j + 1) + (prices[j] - prices[i])
                if (profit > maxProfit) maxProfit = profit
            }
        }
        if (maxProfit > max) max = maxProfit
    }
    return max
}

private fun maxProfitPeakValley(prices: IntArray): Int {
    var i = 0
    var valley = prices[0]
    var peak = prices[0]
    var maxProfit = 0
    while (i < (prices.size - 1)) {
        // find valley
        while (i < (prices.size - 1) && prices[i] >= prices[i + 1]) i++
        valley = prices[i]
        // find peak
        while (i < (prices.size - 1) && prices[i] <= prices[i + 1]) i++
        peak = prices[i]

        maxProfit += peak - valley
    }
    return maxProfit
}

private fun maxProfitOnePass(prices: IntArray): Int {
    var maxProfit = 0
    for (i in prices.indices) {
        if ((i+1) < prices.size && prices[i+1] > prices[i]) {
            maxProfit += prices[i+1] - prices[i]
        }
    }
    return maxProfit
}

fun main() {
    val prices = intArrayOf(7,1,5,3,6,4)
    println(maxProfitOnePass(prices))
}