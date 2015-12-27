# 6/28 - Array, Greedy
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions 
# as you like (ie, buy one and sell one share of the stock multiple times). However, 
# you may not engage in multiple transactions at the same time (ie, you must sell the stock 
# before you buy again).
# Idea:
#   See as long as price goes up (can sell multiple times (first solution) or until price drops (second solution)
class BestTimeToBuyAndSellStock2:
    # @param {integer[]} prices
    # @return {integer}

    # Test on LeetCode - 56ms
    # Idea: sell as long as price goes up
    def max_profit(self, prices):
        profit = 0
        if prices and len(prices) > 1:
            buy = prices[0]
            for num in prices:
                if num > buy:
                    profit += num - buy
                buy = num
        return profit

    # Test on LeetCode - 52ms
    # Idea: not buy and sell at one price, wait until price drops
    def max_profit_greedy(self, prices):
        profit = 0
        if prices and len(prices) > 1:
            buy = prices[0]
            sell = prices[0]
            prices.append(0)
            for i in range(1, len(prices)):
                if prices[i] < prices[i - 1]:  # price drops
                    profit += sell - buy
                    buy = prices[i]
                sell = prices[i]
        return profit