# 8/10 - DP
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
# Note:
#   You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# Solution:
#   DP - count kth transaction when traversing

import sys
class BestTimeToBuyAndSellStock4:
    # @param {integer[]} prices
    # @return {integer}

    # Test on LeetCode - 136ms
    # Idea: (similar to 3)
    #   1. using quick_count to deal with large k
    #   2. for each price, count max profit if it is kth buy or sell
    # Time Complexity - O(kn), Space Complexity - O(n)
    def max_profit(self, k, prices):
        length = len(prices)
        # k is large enough to count profit directly
        if k >= length/2:
            return self.quick_count(prices)
        # not proper k
        if k <= 0:
            return 0

        buys = [-sys.maxint-1 for i in range(0, k)]
        sells = [0 for i in range(0, k)]
        for price in prices:
            for j in range(k-1, 0, -1):
                sells[j] = max(sells[j], buys[j] + price)
                buys[j] = max(buys[j], sells[j-1] - price)
            sells[0] = max(sells[0], buys[0] + price)
            buys[0] = max(buys[0], -price)
        return sells[-1]

    # if there is a price jump, gain the profit
    def quick_count(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i-1]
        return profit

    # Test on LeetCode - 144ms
    # Idea - traverse k times to count the kth profit
    def max_profit2(self, k, prices):
        length = len(prices)
        # k is large enough to count profit directly
        if k >= length/2:
            return self.quick_count(prices)
        # not proper k
        if k <= 0:
            return 0

        profits = [[0 for i in range(0, len(prices))] for j in range(0, k+1)]
        for kk in range(1, k+1):
            temp = -prices[0]
            for i in range(1, len(prices)):
                profits[kk][i] = max(profits[kk][i-1], prices[i] + temp)
                temp = max(temp, profits[kk-1][i-1] - prices[i])
        return profits[k][-1]


def main():
    test = BestTimeToBuyAndSellStock4()
    print test.max_profit(1, [2,1])


if __name__ == '__main__':
    main()
