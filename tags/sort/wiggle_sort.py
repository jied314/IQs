# Given an unsorted array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
# Time Complexity - O(N)
# Idea:
#
class WiggleSort(object):
    def wiggle_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 0:
            return

        flag = True  # <
        current = nums[0]
        for i in range(0, length-1):
            if (flag and current > nums[i+1]) or (not flag and current < nums[i+1]):
                nums[i] = nums[i+1]
            else:
                nums[i] = current
                current = nums[i+1]
            flag = not flag
        nums[length-1] = current
        return nums

test = WiggleSort()
nums = [1,3,2,2,3,2]
print test.wiggle_sort(nums)

