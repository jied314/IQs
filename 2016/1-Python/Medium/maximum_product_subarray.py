# 7/20 - Array, DP
# Fail to produce correct answer
# Note:
#   1. product value can reverse due to negative numbers
#   2. 0
#
# Solution:
#   minhere & maxhere (local max and local min), then get global max
class MaximumProductSubarray:
    # @param {integer[]} nums
    # @return {integer}

    # Test on LeetCode - 72ms
    def max_product(self, nums):
        if len(nums) == 0:
            return 0

        max_pre, min_pre, max_product = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            max_cur = max(max(max_pre * nums[i], min_pre * nums[i]), nums[i])
            min_cur = min(min(max_pre * nums[i], min_pre * nums[i]), nums[i])
            max_product = max(max_cur, max_product)
            max_pre = max_cur
            min_pre = min_cur
        return max_product

    def max_product_array(self, nums):
        if len(nums) == 0:
            return 0
        max_pre, max_pre_start, max_pre_end = nums[0], 0, 0
        min_pre, min_pre_start, min_pre_end = nums[0], 0, 0
        max_product, max_start, max_end = nums[0], 0, 0
        for i in range(1, len(nums)):
            if nums[i] > 0:
                if nums[i] > max_pre * nums[i]:  # max_pre is negative, max_cur start anew
                    max_pre_start, max_pre_end = i, i
                    min_pre_end = i
                    max_cur = nums[i]
                else:  # max_pre is positive, include
                    max_pre_end = i
                    max_cur = max_pre * nums[i]
                if nums[i] > min_pre * nums[i]:  # min_pre is negative, include
                    min_pre_end = i
                    min_cur = min_pre * nums[i]
                else:  # start anew
                    min_pre_start, min_pre_end = i, i
                    min_cur = nums[i]
            else:  # negative
                if nums[i] > min_pre * nums[i]:  # min_pre is positive, start anew
                    max_pre_start, max_pre_end = i, i
                    max_cur = nums[i]
                else:  # min_pre is negative, include
                    max_pre_start = min_pre_start
                    max_pre_end = i
                    max_cur = min_pre * nums[i]
                if nums[i] > min_pre * nums[i]:  # min_pre is negative, start anew
                    min_pre_end = i
                    min_cur = min_pre * nums[i]
                else:  # include
                    min_pre_start, min_pre_end = i, i
                    min_cur = nums[i]
            if max_cur > max_product:
                max_start = max_pre_start
                max_end = max_pre_end
            max_pre = max_cur
            min_pre = min_cur
        return nums[max_start:max_end+1]

def main():
    test = MaximumProductSubarray()
    print test.max_product_array([2, 3, -2, 4])
    print test.max_product_array([0, 2])
    print test.max_product_array([-2, 3, -4, 1])
    print test.max_product_array([3, -1, 4])
    print test.max_product([2,-5,-2,-4,3])


if __name__ == '__main__':
    main()

