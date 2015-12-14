# 7/2 - DC, Array, DP
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
class MaximumSubarray:
    # @param {integer[]} nums
    # @return {integer}
    # Test on LeetCode - 64ms
    def max_subarray_dp(self, nums):
        max_sum = 0
        if nums:
            max_sum, sum = nums[0], nums[0]
            # max_start, max_end, start, end = 0, 0, 0, 0
            for i in range(1, len(nums)):
                if sum + nums[i] <= nums[i]:  # should start anew
                    sum = nums[i]
                    # start, end = i, i
                else:  # should add this one
                    sum += nums[i]
                    # end = i
                if sum > max_sum:
                    max_sum = sum
                    # max_start, max_end = start, end
        return max_sum


def main():
    test = MaximumSubarray()
    print test.max_subarray([-1])
    print test.max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])


if __name__ == '__main__':
    main()

