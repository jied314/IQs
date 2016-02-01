# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
#   Example:
# (1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
# (2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].
# Note: You may assume all input has valid answer.
# Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?

class WiggleSort2(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # should use quick-select to partition the array so that the mid element is the median value
        # A[0...mid] <= A[mid] <= A[mid...length]
        nums.sort()
        length = len(nums)
        mid = nums[length - length/2]
        A = lambda x: nums[((1+2*x)) % (length|1)]
        i, j, k = 0, 0, length-1
        while j <= k:
            if A(j) > mid:

                i += 1
                j += 1
            elif A(j) < mid:

            else:
                j += 1

    # Test on LC - 116ms, 42%
    # Idea:
    #   1. break the sorted array into two parts.
    #   2. merge the two from the tails.
    # e.g. [1, 3, 2, 2, 3, 1] -> [1, 1, 2, 2, 3, 3]
    #      -> [1, 1, 2] & [2, 3, 3] -> [2, 3, 1, 3, 1, 2]
    # Note: find mid in an array
    def wiggle_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) < 2:
            return
        sorted_nums = sorted(nums)
        length = len(nums)
        if length % 2 == 0:
            mid = (length / 2) - 1
        else:
            mid = length / 2
        i = 0
        i1, i2 = mid, length-1
        while i1 > -1 and i2 > mid:
            nums[i] = sorted_nums[i1]
            i1 -= 1
            i += 1
            nums[i] = sorted_nums[i2]
            i2 -= 1
            i += 1
        if i < length:
            nums[i] = sorted_nums[i1]
        return nums


test = WiggleSort2()
print test.wiggleSort([1,3,2,2,2,1,1,3,1,1,2])
