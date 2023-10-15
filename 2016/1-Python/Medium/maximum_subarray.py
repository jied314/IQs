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

    def max_subarray_dc(self, nums):
        if len(nums) == 0:
            return 0
        return self.dc(nums, 0, len(nums)-1)

    def dc(self, nums, low, high):
        if low > high:
            return 0
        if low == high:
            return nums[low]
        mid = low + (high - low) / 2
        # if not contains mid
        left_max = self.dc(nums, low, mid)  # not mid - 1, run example of [-2, -1]
        right_max = self.dc(nums, mid+1, high)
        temp_max = max(left_max, right_max)

        # if contains nums[mid], left max suffix + right max prefix
        left_max, right_max = nums[mid], nums[mid+1]
        temp = 0
        for i in range(mid, low-1, -1):
            temp += nums[i]
            left_max = max(temp, left_max)
        temp = 0
        for i in range(mid+1, high+1):
            temp += nums[i]
            right_max = max(temp, right_max)
        return max(temp_max, left_max+right_max)

def main():
    test = MaximumSubarray()
    print test.max_subarray_dp([-1])
    print test.max_subarray_dc([-2,-1])
    print test.max_subarray_dp([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print test.max_subarray_dc([-2, 1, -3, 4, -1, 2, 1, -5, 4])


if __name__ == '__main__':
    main()

