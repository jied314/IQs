# 8/9, 10 - Array, DP
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
# Note:
#   You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# Solution:
#   1. two non-overlapping transaction, history & future (only works for two, not k transaction)
#   2.

import sys
class BestTimeToBuyAndSellStock3:
    # @param {integer[]} prices
    # @return {integer}

    # Test on LeetCode - 272ms
    # Since two non-interleave transaction, find the maximum history + future profit for all prices
    def max_profit_history_future(self, prices):
        max_profit = 0
        if len(prices) > 1:
            # scan forward to find history profits
            profit = 0
            valley = prices[0]
            history_max_profits = [0]
            for i in range(1, len(prices)):
                if prices[i] < valley:
                    valley = prices[i]
                else:
                    if prices[i] - valley > profit:
                        profit = prices[i] - valley
                history_max_profits.append(profit)
            # scan backward to find future profits
            profit = 0
            peak = prices[-1]
            future_max_profits = [0]
            for j in range(len(prices)-2, -1, -1):
                if prices[j] > peak:
                    peak = prices[j]
                else:
                    if peak - prices[j] > profit:
                        profit = peak - prices[j]
                future_max_profits.insert(0, profit)
                max_profit = max(max_profit, profit + history_max_profits[j])
        return max_profit

    # Test on LeetCode - 72ms
    # Track the max profit for buy and sell
    def max_profit_sell_buy(self, prices):
        buy1, buy2 = -sys.maxint-1, -sys.maxint-1
        sell1, sell2 = 0, 0
        for price in prices:
            sell2 = max(sell2,  buy2 + price)
            buy2  = max(buy2,  sell1 - price)
            sell1 = max(sell1,  buy1 + price)
            buy1  = max(buy1,  -price)
        return sell2


class Profit:
    def __init__(self, start, end, min, max):
        self.start = start
        self.end = end
        self.min = min
        self.max = max
        self.profits = []

    def set_end(self, end):
        self.end = end

    def set_min(self, min):
        self.min = min

    def set_max(self, max):
        self.max = max

    def add_profit(self, profit):
        self.profits.append(profit)


def main():
    test = BestTimeToBuyAndSellStock3()
    print test.max_profit([3, 7, 5, 10, 2, 4, 8, 3, 9, 6, 10, 5, 6, 9, 7, 10])


if __name__ == '__main__':
    main()