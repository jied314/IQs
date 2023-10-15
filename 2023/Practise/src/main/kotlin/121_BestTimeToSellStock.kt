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
 */
private fun maxProfit(prices: IntArray): Int {
    if (prices.count() < 2) return 0

    var maxProfit = 0
    val endI = prices.count()-2
    for (i in 0..endI) {
        var j = i+1
        while (j < prices.count()) {
            if (prices[j] > prices[i]) {
                maxProfit = max(maxProfit, prices[j] - prices[i])
            }
            j++
        }
    }
    return maxProfit
}

fun main() {
    val prices = intArrayOf(7,1,5,3,6,4)
    println(maxProfit(prices))
}