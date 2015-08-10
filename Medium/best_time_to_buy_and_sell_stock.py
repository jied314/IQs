# 6/28 - Array, DP
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (ie, buy one and sell 
# one share of the stock), design an algorithm to find the maximum profit.
# Note:
#   record min, keep the one with the highest profit
#
class BestTimeToBuyAndSellStock:
    # @param {integer[]} prices
    # @return {integer}

    # Test on LeetCode - TLE
    def max_profit(self, prices):
        if not prices or len(prices) == 1:
            return 0
        ordered = sorted(prices)
        min_index = prices.index(ordered[0])
        max_index = prices.index(ordered[-1])
        if min_index < max_index:
            return ordered[-1] - ordered[0]
        else:
            if len(prices) == 2:
                return 0
            result1 = 0
            result2 = 0
            for i in range(len(ordered) - 2, -1, -1):
                if min_index < prices.index(ordered[i]):
                    result1 = ordered[i] - ordered[0]
                    break
            # print result1
            for i in range(1, len(ordered)):
                if max_index > prices.index(ordered[i]):
                    result2 = ordered[-1] - ordered[i]
                    break
            # print result2
            return max(result1, result2)

    # Test on LeetCode - 60ms, Time Complexity - O(N)
    # Idea: record min_so_far and max_so_far (including indexes), compare along the way
    #       not very good due to max in not necessary
    def max_profit_dp(self, prices):
        result = 0
        if prices and len(prices) > 1:
            min, max = [], []
            if prices[0] < prices[1]:
                result = prices[1] - prices[0]
                min.append(prices[0])
                min.append(0)
                max.append(prices[1])
                max.append(1)
            else:
                max.append(prices[0])
                max.append(0)
                min.append(prices[1])
                min.append(1)
            #print min, max
            for i in range(2, len(prices)):
                if prices[i] > max[0]:
                    max[0] = prices[i]
                    max[1] = i
                    if i > min[1]:
                        result = max[0] - min[0]
                elif prices[i] < min[0]:
                    min[0] = prices[i]
                    min[1] = i
                    if i < max[1]:
                        result = max[0] - min[0]
                else:
                    temp = prices[i] - min[0]
                    if temp > result:
                        result = temp
        return result

    # Test on LeetCode - 48ms
    # keep track of min and result
    def max_profit_dp_nice(self, prices):
        result = 0
        if len(prices) > 1:
            min = prices[0]
            for i in range(1, len(prices)):
                if prices[i] < min:
                    min = prices[i]
                else:
                    if prices[i] - min > result:
                        result = prices[i] - min
        return result


def main():
    test = BestTimeToBuyAndSellStock()
    #print test.max_profit_dp([4, 7, 2, 9, 5])
    #print test.max_profit_dp([4, 7, 9, 2, 5])
    print test.max_profit_dp_nice([4, 1, 2])


if __name__ == '__main__':
    main()
