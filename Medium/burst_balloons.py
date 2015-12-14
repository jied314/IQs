# 12/13 - DC, DP
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
# You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
# Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
# Find the maximum coins you can collect by bursting the balloons wisely.
# Note:
#   (1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
#   (2) 0 <= n <= 500, 0 <= nums[i] <= 100
# Example:
#   Given [3, 1, 5, 8]
#   Return 167
#   nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
# Fail on first trial

class BurstBallons(object):
    # Wrong - assume popping the smallest coins (in the middle) will yield maximum
    def max_coins_error(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        length = len(nums)
        ret = 0
        if length == 1:
            return nums[0]
        ret += nums[0] * nums[length-1]
        ret += max(nums[0], nums[length-1])
        if length > 2:
            sorted_nums = sorted(nums[1:length - 1])
            for num in sorted_nums:
                index = nums.index(num)
                ret += num * nums[index - 1] * nums[index + 1]
                nums.pop(index)
        return ret

    # Test on LC - 732ms
    # Time Complexity - O(N^3), Memory Complexity - O(N^3)
    # DP - compute varying ranges and consider different final pops to minimize problem size
    def max_coins_dp(self, nums):
        nums.insert(0, 1)
        nums.append(1)
        full_length = len(nums)
        # dp_range_values[i][j] stores the max of coins can be obtained by popping within the range [i, j]
        dp_range_values = [[0] * full_length for _ in range(0, full_length)]

        # compute from shorter length to full length
        for length in range(1, full_length-1):  # 1 <= length <= len(nums)
            for start in range(1, full_length-length):  # start + length < full_length
                end = start + length - 1
                # compute the max of coins can be obtained by popping within [start, end]
                # final can be at any position
                for final in range(start, end+1):  # start <= final <= end
                    temp = dp_range_values[start][final-1] + dp_range_values[final+1][end]  # popping from outside
                    temp += (nums[start-1] * nums[final] * nums[end+1])  # popping the final
                    dp_range_values[start][end] = max(dp_range_values[start][end], temp)
        return dp_range_values[1][full_length-2]

test = BurstBallons()
print test.max_coins_dp([3, 1, 5, 8])