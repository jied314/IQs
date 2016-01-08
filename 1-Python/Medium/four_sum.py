# 1/3 - Two Pointers
# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.
# Note:
#   Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <= b <= c <= d)
#   The solution set must not contain duplicate quadruplets.
#   For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
#   A solution set is: (-1,  0, 0, 1), (-2, -1, 1, 2), (-2,  0, 0, 2)
# Idea:
#   build from two sum. Time Complexity - O(N^3)
#   skip duplicates

class FourSum(object):

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) < 4:
            return []
        nums.qsort()
        length = len(nums)
        ret = []
        for a in range(0, length-3):
            if a > 0 and nums[a] == nums[a-1]:
                    continue
            n1 = nums[a]
            for b in range(a+1, length-2):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                n2 = nums[b]
                temp_target = target - n1 - n2
                right = self.two_sum(temp_target, nums, b+1, length-1)
                if right is not None:
                    for r in right:
                        ret.append([n1, n2] + r)
        return ret

    def two_sum(self, target, nums, start, end):
        if target < nums[start] * 2 or target > nums[end] * 2:
            return None
        ret = []
        while start < end:
            temp_sum = nums[start] + nums[end]
            if temp_sum < target:
                start = self.skip_leading_duplicate(nums, start, end)
            elif temp_sum > target:
                end = self.skip_trailing_duplicate(nums, end, end)
            else:
                ret.append([nums[start], nums[end]])
                start = self.skip_leading_duplicate(nums, start, end)
                end = self.skip_trailing_duplicate(nums, start, end)
        return ret

    def skip_leading_duplicate(self, nums, start, end):
        while start < end-1 and nums[start] == nums[start+1]:
            start += 1
        return start + 1

    def skip_trailing_duplicate(self, nums, start, end):
        while end > start+1 and nums[end] == nums[end-1]:
            end -= 1
        return end - 1
