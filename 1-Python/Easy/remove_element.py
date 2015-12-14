# 9/14 - Array, Two Pointers (E)
# Given an array and a value, remove all instances of that value in place and return the new length.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#

class RemoveElement(object):
    def remove_element(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1;
        return j+1
