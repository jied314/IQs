# Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that
# any number in range [1, n] inclusive can be formed by the sum of some elements in the array.
# Return the minimum number of patches required.
#
# Example 1:
#   nums = [1, 3], n = 6. Return 1.
#   Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
#   Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
#   Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
#   So we only need 1 patch.
#
# Example 2:
#   nums = [1, 5, 10], n = 20. Return 2.
#   The two patches can be [2, 4].
#
# Example 3:
#   nums = [1, 2, 2], n = 5. Return 0.
#
# Idea:
#   use min_miss to record the minimum missing number.
#   note that all numbers < min_miss must be sorted in order and are covered.
#


class Solution(object):
    # Test on LC - 60ms, 21%
    def min_patches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        min_miss = 1
        count = 0
        i = 0
        while min_miss <= n:
            if i < len(nums) and nums[i] <= min_miss:
                min_miss += nums[i]  # the max covered number so-far
                i += 1
            # add a patch. since < min_miss are covered, certainly after adding min_miss, numbers in range
            # (min_miss, 2*min_miss) are covered too.
            else:
                min_miss += min_miss
                count += 1
        return count

test = Solution()
print test.min_patches([1, 2, 4, 13, 43], 100)
print test.min_patches([1, 5, 10], 20)