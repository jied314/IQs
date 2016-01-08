# 1/2 - DP
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
# Note:
#   You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# Idea:
#   similar to version 3.
#   use dp to track max profit for ith transaction
#   dp[i][j] = max(dp[i-1, j], prices[j] + tmpMax)
class Solution(object):
    def max_profit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if k >= length / 2:  # use all profits
            return self.quickSolve(prices)

        # dp[i][j] records the max profit for prices[j] for the ith transaction
        dp = [[0] * length for _ in xrange(k+1)]
        for i in range(1, k+1):
            tmp_max = -prices[0]
            for j in range(1, length):
                dp[i][j] = max(dp[i][j - 1], prices[j] + tmp_max)
                tmp_max = max(tmp_max, dp[i - 1][j - 1] - prices[j])
        return dp[k][length - 1]

    # collect all possible profits
    def quickSolve(self, prices):
        length = len(prices)
        profit = 0
        for i in range(1, length):
            # as long as there is a price gap, we gain a profit.
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


test = Solution()
print test.max_profit(3, [4, 3, 7, 9, 2, 1, 5, 3, 8])