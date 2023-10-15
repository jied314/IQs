# 9/24 - Array, Two Pointers (E)
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order
# of the non-zero elements.
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

class MoveZeroes(object):
    # Test on LeetCode - 140ms
    def move_zeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is not None and len(nums) > 1:
            length = len(nums)
            zero_start = -1
            for i in range(0, length):
                if nums[i] != 0:
                    if -1 < zero_start < i:
                        nums[zero_start], nums[i] = nums[i], nums[zero_start]
                        zero_start += 1
                else:
                    if zero_start == -1:
                        zero_start = i


def main():
    l1 = [0, 1, 0, 3, 12]
    l2 = [1, 0, 2, 0, 3]
    test = MoveZeroes()
    test.move_zeroes(l1)
    test.move_zeroes(l2)
    print l1, l2


if __name__ == '__main__':
    main()
