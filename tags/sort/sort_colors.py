# 7/5 - Array, Two Pointers, Sort
# Similar to Dutch National Flag Problem - https://en.wikipedia.org/wiki/Dutch_national_flag_problem
class SortColors:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.

    # Test on LeetCode - 60ms
    # straight forward solution: a two-pass algorithm using counting sort.
    # First, iterate the array counting number of 0's, 1's, and 2's,
    # then overwrite array with total number of 0's, then 1's and followed by 2's.
    def sort_colors_count(self, nums):
        num_0s, num_1s, num_2s = 0, 0, 0
        for num in nums:
            if num == 0:
                num_0s += 1
            elif num == 1:
                num_1s += 1
            else:
                num_2s += 1
        for i in range(0, num_0s):
            nums[i] = 0
        for i in range(0, num_1s):
            nums[num_0s + i] = 1
        for i in range(0, num_2s):
            nums[num_0s + num_1s + i] = 2

    # Test on LeetCode - 56ms
    # The idea is to sweep all 0s to the left and all 2s to the right, then all 1s are left in the middle.
    def sort_colors_nice(self, nums):
        end_0, start_2 = 0, len(nums)
        i = 0
        while i < start_2:
            if nums[i] == 0:
                nums[i], nums[end_0] = nums[end_0], nums[i]
                end_0 += 1
            if nums[i] == 2:
                start_2 -= 1
                nums[i], nums[start_2] = nums[start_2], nums[i]
                i -= 1
            i += 1

    # Revisit - 1/6
    # Test on LC - 44ms
    # similar ideas
    def sort_colors_revisit(self, nums):
        length = len(nums)
        start = 0
        end = length - 1
        i = 0
        while i <= end:
            if nums[i] == 0:
                nums[start], nums[i] = nums[i], nums[start]
                start += 1
                i += 1
            elif nums[i] == 2:
                nums[end], nums[i] = nums[i], nums[end]
                end -= 1
            else:
                i += 1


def main():
    test = SortColors()
    print test.sort_colors([1, 0, 0, 1, 2, 1, 1, 2, 0, 2])


if __name__ == "__main__":
    main()