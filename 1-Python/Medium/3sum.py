# 11/28 - Array, Two Pointers
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.
# Note:
#   Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
#   The solution set must not contain duplicate triplets.
# For example, given array S = {-1 0 1 2 -1 -4},
#   A solution set is:
#   (-1, 0, 1)
#   (-1, -1, 2)
# Revisit 12/27
# Idea:
#   For each number i, do two sum. Note to avoid duplicates.
class Solution(object):
    def three_sum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.qsort()
        length = len(nums)
        ret = []
        for i in range(0, length-2):
            if i > 0 and nums[i] == nums[i-1]:  # avoid duplicates
                continue
            num1 = nums[i]
            target = 0 - num1
            i2, i3 = i+1, length-1
            while i2 < i3:
                s = nums[i2] + nums[i3]
                if s == target:
                    ret.append([num1, nums[i2], nums[i3]])
                    # avoid duplicates
                    while i2 < i3 and nums[i2] == nums[i2 + 1]:
                        i2 += 1
                    while i2 < i3 and nums[i3] == nums[i3 - 1]:
                        i3 -= 1
                    i2 += 1
                    i3 -= 1
                elif s > target:
                    i3 -= 1
                else:
                    i2 += 1
        return ret

    # what if four sum with same requirements?
    def four_sum(self, nums):
        nums.qsort()
        length = len(nums)
        ret = []
        for i in range(0, length-3):
            if i > 0 and nums[i] == nums[i-1]:  # avoid duplicates
                continue
            num1 = nums[i]
            target = 0 - num1
            for j in range(i+1, length-2):
                if j > i+1 and nums[j] == nums[j-1]:  # avoid duplicates
                    continue
                num2 = nums[j]
                target -= num2
                i3, i4 = j+1, length-1
                while i3 < i4:
                    s = nums[i3] + nums[i4]
                    if s == target:
                        ret.append([num1, num2, nums[i3], nums[i4]])
                        # avoid duplicates
                        while i3 < i4 and nums[i3] == nums[i3 + 1]:
                            i3 += 1
                        while i3 < i4 and nums[i4] == nums[i4 - 1]:
                            i4 -= 1
                        i3 += 1
                        i4 -= 1
                    elif s > target:
                        i4 -= 1
                    else:
                        i3 += 1
        return ret

test = Solution()
print test.four_sum([0,0,0,0])
print test.four_sum([0,0,0,0,0])