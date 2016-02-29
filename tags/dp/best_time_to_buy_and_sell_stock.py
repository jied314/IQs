# 6/28 - Array, DP
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (ie, buy one and sell 
# one share of the stock), design an algorithm to find the maximum profit.
# Note:
#   record min, keep the one with the highest profit
#
class BestTimeToBuyAndSellStock:
    # Test on LeetCode - 48ms
    # keep track of min and max_profit
    def max_profit_dp_nice(self, prices):
        if prices is None or len(prices) < 2:
            return 0
        max_profit = 0
        low = prices[0]
        for i in range(1, len(prices)):
            low = min(low, prices[i])
            max_profit = max(max_profit, prices[i] - low)
        return max_profit


def main():
    test = BestTimeToBuyAndSellStock()
    #print test.max_profit_dp([4, 7, 2, 9, 5])
    #print test.max_profit_dp([4, 7, 9, 2, 5])
    print test.max_profit_dp_nice([4, 1, 2])


if __name__ == '__main__':
    main()
