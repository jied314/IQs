# 10/10 - Array, Greedy, DP (M)
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.
# For example:
#   A = [2,3,1,1,4], return true.
#   A = [3,2,1,0,4], return false.
#
# Follow Up:
#   How can you get the minimum number of jumps.


class JumpGame(object):
    # Test on LeetCode - 48ms
    # Same idea, but simpler code
    def can_jump_dp_nice(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False
        length = len(nums)
        max_so_far = 0
        for i in range(0, length):
            if i > max_so_far:
                return False
            max_so_far = max(max_so_far, i + nums[i])
        return True

    # Test on LeetCode - 132ms
    # Idea:
    #   backward, move start index. Check whether start index == 0.
    def can_jump_greedy(self, nums):
        if nums is None or len(nums) == 0:
            return False
        length = len(nums)
        start = length - 1
        for i in range(length-2, -1, -1):
            if i + nums[i] >= start:
                start = i
        return start == 0

    # TLE - use DP is slower than greedy
    def min_jump_dp_TLE(self, nums):
        if nums is None or len(nums) < 2:
            return 0
        length = len(nums)
        dp = [length] * length
        dp[0] = 0
        for i in range(length-1):
            can_reach = i + nums[i]
            for j in range(i+1, min(can_reach+1, length)):
                dp[j] = min(dp[j], dp[i]+1)
        return dp[-1]

    # use Greedy to solve
    #   1. choose the index that can jump the furthest (cur_max)
    #   2. then update cur_max for indices within (begin, end)
    # Note:
    #   Once reach the last index or further, return the current count.
    def min_jump_greedy(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) < 2:
            return 0
        length = len(nums)
        begin, end, count, cur_max = 0, 0, 0, 0
        while end < length:
            count += 1
            for i in range(begin, end+1):
                cur_max = max(cur_max, i + nums[i])
                if cur_max >= length-1:
                    return count
            begin = end + 1
            end = cur_max
        return count


def main():
    test = JumpGame()
    print test.can_jump_greedy([])
    print test.can_jump_greedy([1])
    print test.can_jump_greedy([2, 3, 1, 1, 4])
    print test.can_jump_greedy([3, 2, 1, 0, 4])
    print test.can_jump_greedy([1, 0, 0, 1, 4])
    print test.min_jump([2, 3, 1, 1, 4])

if __name__ == '__main__':
    main()
