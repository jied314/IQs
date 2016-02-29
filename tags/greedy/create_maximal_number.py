# Given two arrays of length m and n with digits 0-9 representing two numbers.
# Create the maximum number of length k <= m + n from digits of the two.
# The relative order of the digits from the same array must be preserved.
# Return an array of the k digits. You should try to optimize your time and space complexity.
#
# Example 1:
#   nums1 = [3, 4, 6, 5]
#   nums2 = [9, 1, 2, 5, 8, 3]
#   k = 5
#   return [9, 8, 6, 5, 3]
# Example 2:
#   nums1 = [6, 7]
#   nums2 = [6, 0, 4]
#   k = 5
#   return [6, 7, 6, 0, 4]
# Example 3:
#   nums1 = [3, 9]
#   nums2 = [8, 9]
#   k = 3
#   return [9, 8, 9]
#
# Refer to: http://algobox.org/create-maximum-number/

class Solution(object):
    # Easy Version 1:
    # Given one array of length n, create the maximum number of length k.
    # The solution to this problem is Greedy with the help of stack.
    def max_array(self, nums, k):
        """
        :param nums: List[int]
        :param k: int
        :return: List[int]
        """
        n = len(nums)
        ans = [0] * k  # result
        j = 0
        for i in range(0, n):
            # have enough left and the next one is greater
            while n - i + j > k and j > 0 and ans[j - 1] < nums[i]:
                j -= 1
            if j < k:  # push to stack
                ans[j] = nums[i]
                j += 1
        return ans

    # Easy Version 2:
    # Given two array of length m and n, create maximum number of length k = m + n.
    # We have k decisions to make, each time will just need to decide ans[i] is from which of the two.
    # O(nm) due to equal situation - look ahead
    def merge(self, nums1, nums2, k):
        """
        :param nums1: List[int]
        :param nums2: List[int]
        :param k: int
        :return: List[int]
        """
        ans = [0] * k
        i, j = 0, 0
        for r in range(0, k):
            if self.greater(nums1, i, nums2, j):
                ans[r] = nums1[i]
                i += 1
            else:
                ans[r] = nums2[j]
                j += 1
        return ans

    def greater(self, nums1, i, nums2, j):
        """
        :param nums1: List[int]
        :param i: int
        :param nums2: List[int]
        :param j: int
        :return: Boolean
        """
        while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
            i += 1
            j += 1
        return j == len(nums2) or (i < len(nums1) and nums1[i] > nums2[j])

    # Final Version:
    # Divide k into two parts: i & k-i
    # Merge the max_number of length i from nums1 and the max_number of length k-i from nums2.
    # Update result accordingly.
    # O((m+n)^3)
    def max_number(self, nums1, nums2, k):
        """
        :param nums1: List[int]
        :param nums2: List[int]
        :param k: int
        :return: List[int
        """
        n, m = len(nums1), len(nums2)
        ans = [0] * k
        i = max(0, k - m)
        while i <= k and i <= n:
            candidate = self.merge(self.max_array(nums1, i), self.max_array(nums2, k - i), k)
            if self.greater(candidate, 0, ans, 0):
                ans = candidate
            i += 1
        return ans


test = Solution()
print test.max_array([9, 1, 2, 5, 8, 3], 5)
print test.merge([6, 7], [6, 0, 4], 5)
print test.max_number([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)