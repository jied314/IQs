# 1/14 - Array, Union Find, Hash Table
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# For example,
#   Given [100, 4, 200, 1, 3, 2],
#   The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
# Your algorithm should run in O(n) complexity.


class Solution(object):
    # Test on LC - 52ms, 54%
    # Idea:
    #   Use set to enable fast query.
    #   Starting from the smallest of a sequence, find the largest of the sequence.
    #   Update best if applicable.
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        best = 0  # record the length of a sequence
        for n in nums:
            if n - 1 not in nums:  # n is the smallest of a sequence
                m = n + 1
                while m in nums:  # find the largest of the sequence
                    m += 1
                best = max(best, m - n)
        return best

test = Solution()
print test.longestConsecutive([100, 4, 202, 8, 10, 200, 1, 3, 201, 2])