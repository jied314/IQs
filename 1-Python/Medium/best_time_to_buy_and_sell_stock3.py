# 1/2 - DP
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
# Note:
#   You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# Idea:
#   DP - four variables, buy1, sell1, buy2, sell2, calculate in sequence
class Solution(object):
    def max_profit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) < 2:
            return 0
        min_val = -(1 << 31)
        buy1, sell1, buy2, sell2 = min_val, 0, min_val, 0
        for price in prices:
            sell2 = max(sell2, buy2 + price)
            buy2 = max(buy2, sell1 - price)
            sell1 = max(sell1, buy1 + price)
            buy1 = max(buy1, -price)
        return sell2
