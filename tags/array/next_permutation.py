# 10/15 - Array
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of
# numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order
# (ie, sorted in ascending order).
# The replacement must be in-place, do not allocate extra memory.
# Here are some examples.
# Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 -> 1,3,2
# 3,2,1 -> 1,2,3
# 1,1,5 -> 1,5,1


class NextPermutation(object):
    # Idea:
    #   1. from tail to head, find nums[i] > nums[i-1]. note: nums[i] ... nums[N-1] is sorted in descending order
    #   2. from N-1 to 1, find the first one that is larger than nums[i-1], swap.
    #      note: nums[i] ... nums[N-1] is still sorted in descending order
    #   3. reverse nums[i] ... nums[N-1]
    # Test on LeetCode - 68ms
    def next_permutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None:
            return nums
        length = len(nums)
        index = -1
        for i in range(length-1, 0, -1):
            if nums[i] > nums[i - 1]:  # place to reverse
                index = i
                break
        if index > 0:  # switch and reorder
            next_index = -1
            target_val = nums[index - 1]
            # find the index of the element that is larger than target_val, starting from tail
            for i in range(length - 1, index - 1, -1):
                if nums[i] > target_val:
                    next_index = i
                    break
            nums[index - 1], nums[next_index] = nums[next_index], nums[index - 1]
            self.reverse(nums, index)
        else:  # descending order, e.g. [3, 2, 1]. reverse
            nums.qsort()
        return nums

    # reverse nums[start:-1] to ascending order
    def reverse(self, nums, start):
        """
        :param nums: array. from start to end is descending order
        :param start: the starting index that needs to be reversed
        """
        end = len(nums) - 1
        while end > start:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


def main():
    test = NextPermutation()
    #start = [1, 2, 3, 4]
    #end = [4, 3, 2, 1]
    start = [1, 1, 2, 2]
    end = [2, 2, 1, 1]
    while start != end:
        print start
        test.next_permutation(start)
    print start


if __name__ == "__main__":
    main()


