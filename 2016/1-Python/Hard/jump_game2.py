# 12/28 - Greedy
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# For example:
#   Given array A = [2,3,1,1,4]
#   The minimum number of jumps to reach the last index is 2.
#   (Jump 1 step from index 0 to 1, then 3 steps to the last index.)


class Solution(object):
    # Idea:
    #   jump from one region to another region, always jump to the one which will leads to the furthest.
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return 0
        begin, end, count, max_jump = 0, 0, 0, 0
        while end < length:
            count += 1
            for i in range(begin, end+1):
                if i + nums[i] >= length-1:
                    return count
                max_jump = max(max_jump, i + nums[i])
            begin = end+1
            end = max_jump
        return count

test = Solution()
print test.jump([2, 3, 1])
