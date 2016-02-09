# 1/14 - Array, Union Find
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# For example,
#   Given [100, 4, 200, 1, 3, 2],
#   The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
# Your algorithm should run in O(n) complexity.


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        best = 0
        for n in nums:
            if n - 1 not in nums:
                m = n + 1
                while m in nums:
                    m += 1
                best = max(best, m - n)
        return best

test = Solution()
print test.longestConsecutive([100, 4, 202, 8, 10, 200, 1, 3, 201, 2])