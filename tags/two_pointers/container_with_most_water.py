# 7/30 - Array, Two Pointers
# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# Note: You may not slant the container.
#
# Two Pointers Solution - Proof by Contradiction:
#   Suppose the returned result is not the optimal solution. Then there must exist an optimal solution,
# say a container with aol and aor (left and right respectively), such that it has a greater volume than
# the one we got. Since our algorithm stops only if the two pointers meet. So, we must have visited one
# of them but not the other.
#   Let's say we visited aol but not aor. When a pointer stops at aol, it won't move until:
#   1. The other pointer also points to aol.
#       In this case, iteration ends. But the other pointer must have visited aor on its way from right end to aol.
#   Contradiction to our assumption that we didn't visit aor.
#
#   2. The other pointer arrives at a value, say arr, that is greater than aol before it reaches aor.
#       In this case, we does move aol. But notice that the volume of aol and arr is already greater than
#   aol and aor (as it is wider and higher), which means that aol and aor is not the optimal solution -- Contradiction!
#   Both cases arrive at a contradiction.


class ContainerWithMostWater:
    # @param {integer[]} height
    # @return {integer}

    # Test on LeetCode - TLE
    def max_area_tle(self, height):
        result = 0
        if len(height) > 1:
            for i in range(0, len(height)-1):
                for j in range(i+1, len(height)):
                    area = (j - i) * min(height[i], height[j])
                    if result < area:
                        result = area
        return result

    # Test on LeetCode - 88ms
    # O(N)
    def max_area_two_pointers(self, height):
        result = 0
        if height:
            result = 0
            l, r = 0, len(height) - 1
            while l < r:
                result = max(result, (r - l) * min(height[l], height[r]))
                if height[l] < height[r]:
                    l += 1
                else:
                    r -= 1
        return result

def main():
    test = ContainerWithMostWater()
    print test.max_area_two_pointers([3, 1, 5, 2])


if __name__ == '__main__':
    main()