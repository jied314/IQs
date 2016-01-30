# 12/27 - Two Pointers
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.
#   For example, given array S = {-1 2 1 -4}, and target = 1.
#   The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Idea:
#   For each num i, calculate i + TwoSum(1..N)
#   Time Complexity - O(N*N)
import sys

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.qsort()
        length = len(nums)
        if length < 4:
            return sum(nums)
        ret = sys.maxint
        for i in range(0, length-2):
            num1 = nums[i]
            i2 = i + 1
            i3 = length-1
            while i2 < i3:
                s = num1 + nums[i2] + nums[i3]
                if abs(ret-target) > abs(s-target):
                    ret = s
                if s > target:
                    i3 -= 1
                elif s < target:
                    i2 += 1
                else:
                    return target
        return ret

