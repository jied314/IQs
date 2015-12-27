# 8/4 - Array, Two Pointers
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# Two Pointers:
#   one traverses the whole list, one points to the desired index (result) - two versions (either points to the start of
# the current comparing value, or the new start of the next comparing value
class RemoveDuplicatesFromSortedArray:
    # @param {integer[]} nums
    # @return {integer}
    # Test on LeetCode - 92ms
    def remove_duplicates_swap(self, nums):
        if nums is None or len(nums) < 2:
            return len(nums)
        i, j = 0, 1
        while j < len(nums):
            if nums[i] < nums[j]:
                # swap if necessary
                if nums[i+1] <= nums[i]:  # swap
                    nums[i+1], nums[j] = nums[j], nums[i+1]
                i += 1
            j += 1
        return i+1

    # 12/25 - Revisit
    # Test on LeetCode - 88ms
    # Two pointers: i -> last visited unique value, j -> traverse the list
    def remove_duplicates_revisit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        length = len(nums)
        i = 0
        for j in range(1, length):
            if nums[i] != nums[j]:
                nums[i+1], nums[j] = nums[j], nums[i+1]
                i += 1
        return i+1

    # # Test on LeetCode - 104ms
    def remove_duplicates_change_value1(self, nums):
        if nums is None or len(nums) < 2:
            return len(nums)
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1

    # # Test on LeetCode - 104ms
    def remove_duplicates_change_value2(self, nums):
        if nums is None or len(nums) < 2:
            return len(nums)
        i = 1
        for j in range(1, len(nums)):
            if nums[i-1] != nums[j]:
                nums[i] = nums[j]
                i += 1
        return i

def main():
    test = RemoveDuplicatesFromSortedArray()
    print test.remove_duplicates_change_value2([1,2])
    print test.remove_duplicates_change_value2([1,1,1,2,2])

if __name__ == '__main__':
    main()