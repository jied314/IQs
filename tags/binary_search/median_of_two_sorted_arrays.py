# 2/17 - Array, BS
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# Note - not finished


class Solution(object):
    def find_median_sorted_arrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        if total & 1:  # odd
            return self.find_kth(nums1, nums2, total/2 + 1)
        else:
            return 0.5 * (self.find_kth(nums1, nums2, total/2) + self.find_kth(nums1, nums2, total/2 + 1))

    def find_kth(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            return self.find_kth(nums2, nums1, k)
        if len(nums1) == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])

        p1, p2 = min(k/2, len(nums1)), min(len(nums2, k/2))
        if nums1[p1-1] > nums2[p2-1]:
            return self.find_kth(nums1, nums2, )
        else:
            return self.find_kth()
        return 0




