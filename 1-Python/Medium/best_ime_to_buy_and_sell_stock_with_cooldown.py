# 12/22 - DP
# Say you have an array for which the ith element is the price of a given stock on day i.
#   Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Example:
#   prices = [1, 2, 3, 0, 2] -> maxProfit = 3
#   transactions = [buy, sell, cooldown, buy, sell]
#
# Solution:
#   for each price, three options: buy, sell and cooldown.
#       only sell after buy -> sell[i] = max(sell[i-1], price + buy[i-1])
#       only buy after cooldown -> buy[i] = max(buy[i-1], cooldown[i-1] - price)
#       cooldown after sell -> cooldown[i] = sell[i-1]
#
#   Optimization:
#       only depends on the previous state, array is not needed.
#       cooldown[i] = sell[i-1]

class Solution(object):
    def max_profit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == None or len(prices) < 2:
            return 0
        length = len(prices)
        dp_buy = [0] * length
        dp_sell = [0] * length
        dp_cooldown = [0] * length
        dp_buy[0] = -prices[0]
        
        for i in range(1, length):
            price = prices[i]
            dp_buy[i] = max(dp_cooldown[i-1] - price, dp_buy[i-1])
            dp_sell[i] = max(dp_sell[i-1], price + dp_buy[i-1])
            dp_cooldown[i] = dp_sell[i-1]
        return dp_sell[-1]

    def max_profit_nice(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == None or len(prices) < 2:
            return 0
        length = len(prices)
        prev_buy = -prices[0]
        prev_sell = 0
        prev_cooldown = 0
        for i in range(1, length):
            price = prices[i]
            buy = max(prev_cooldown - price, prev_buy)
            sell = max(prev_sell, price + prev_buy)
            prev_cooldown = prev_sell
            prev_sell = sell
            prev_buy = buy
        return sell


test = Solution()
print test.max_profit_nice([1,2,3,0,2])