# 1/12 - Array
# Given an unsorted integer array, find the first missing positive integer.
# For example, [1,2,0] => 3, [3,4,-1,1] => 2, [1000] => 1.
# Your algorithm should run in O(n) time and uses constant space.
# Idea:
#   move all positive numbers (< length) to its right position
#   e.g. 1 -> index 0, 2 -> index1 and so on.
#   the first unmatched element is the first missing one
#   e.g. [3,4,-1,1] -> [1,-1,3,4] => 2


class Solution(object):
    # Test on LC - 52ms 25%; Borrow from Yanxing
    def first_missing_positive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        i = 0
        while i < length:
            if 0 < nums[i] < length:
                if nums[nums[i]-1] != nums[i]:
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                    i -= 1
            i += 1
        for i in range(0, length):
            if nums[i] != i+1:
                return i+1
        return length+1

test = Solution()
print test.first_missing_positive([-1,4,2,1,9,10])