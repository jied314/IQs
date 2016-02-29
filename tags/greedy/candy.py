# 2/15 - Greedy
# There are N children standing in a line. Each child is assigned a rating value.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
#
# Idea:
#   1. Init an array of 1s as a starting point
#   2. Traverse (solves upward ratings) - if ratings[i] > ratings[i-1], candies[i] should be greater than candies[i-1]
#   3. Traverse Reversely (solves downward ratings) - if ratings[j] > ratings[j+1], candies[j] should be greater than candies[j+1]


class Solution(object):
    # Test on LC - 92ms, 63%
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if ratings is None or len(ratings) == 0:
            return 0

        length = len(ratings)
        candies = [1] * length

        for i in range(1, length):
            if ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
                candies[i] = candies[i-1] + 1

        for j in range(length-2, -1, -1):
            if ratings[j] > ratings[j+1] and candies[j] <= candies[j+1]:
                candies[j] = candies[j+1] + 1

        return sum(candies)


test = Solution()
print test.candy([2, 1])

