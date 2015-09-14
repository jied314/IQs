# 9/14 - Bit Manipulation (M)
# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements
# appear exactly twice. Find the two elements that appear only once.
# For example:
#     Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
# Note:
#     The order of the result is not important. So in the above example, [5, 3] is also correct.
#     Your algorithm should run in linear runtime complexity.
#     Could you implement it using only constant space complexity?
# Idea - two passes:
#   1. use XOR to find the two numbers XOR result
#   2. since the two numbers are distinct, there must be one bit set to 1 in the XOR result.
#      find one set bit and use it to differentiate from the two numbers

class Solution(object):
    # Test on LeetCode - 44ms
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = 0
        for num in nums:
            result ^= num

        diff = result & -result
        result = [0, 0]
        for num in nums:
            if diff & num == 0:
                result[0] ^= num
            else:
                result[1] ^= num
        return result

