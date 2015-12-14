# 10/1 - Array, Math, Bit Manipulation (M)
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
# find the one that is missing from the array.
# For example, Given nums = [0, 1, 3] return 2.
# Note: Your algorithm should run in linear runtime complexity.
#       Could you implement it using only constant extra space complexity?

class MissingNumber(object):
    # Test on LeetCode - 60ms
    def missing_number(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        standard_sum, true_sum = 0, 0
        for i in range(0, length):
            standard_sum += i
            true_sum += nums[i]
        dif = true_sum - standard_sum
        return length - dif

    def missing_number_avoid_overflow(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        true_sum = 0
        for i in range(0, length):
            true_sum += nums[i]
        return ((length * (length + 1)) - 2 * true_sum) / 2

    # Idea: cancel out the same number
    # Test on LeetCode - 64ms
    def missing_number_bit_manipulation(self, nums):
        length = len(nums)
        result = length
        for i in range(0, length):
            result ^= nums[i]
            result ^= i
        return result


def main():
    test = MissingNumber()
    print test.missing_number([0, 1, 3])
    print test.missing_number([0])
    print test.missing_number_avoid_overflow([0, 1, 3])
    print test.missing_number_avoid_overflow([0])


if __name__ == '__main__':
    main()
