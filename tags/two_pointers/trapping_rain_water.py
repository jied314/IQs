# 1/14 - Array, Stack, Two Pointers
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
# it is able to trap after raining.
# Idea:
#   instead of calculating area by height*width, think it in a cumulative way -> sum water amount of each bin(width=1)
#   Search from left to right and maintain a max height of left and right separately
#   Fix the higher one and flow water from the lower part.
#   For example, if current height of left is lower, we fill water in the left bin.
#   Until left meets right, we filled the whole container.


class Solution(object):
    # Test on LC - 72ms, 21%
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        res = 0
        left_max, right_max = 0, 0
        while left <= right:
            if height[left] <= height[right]:  # right is higher -> flow water from left
                if height[left] >= left_max:  # not seen a valley yet
                    left_max = height[left]
                else:
                    res += left_max - height[left]
                left += 1
            else:  # left is higher -> flow water from right
                if height[right] >= right_max:  # not seen a valley yet
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1
        return res

test = Solution()
print test.trap([0,1,0,2,1,0,1,3,2,1,2,1])