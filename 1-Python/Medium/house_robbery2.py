# 10/8 - DP
# This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, the security system for these houses remain the same as for those in the previous street.
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.

class HouseRobbery2(object):
    # Test on LeetCode - 44ms
    # Idea:
    #   Since every house is either robbed or not robbed and at least half of the houses are not robbed,
    # the solution is simply the larger of two cases with consecutive houses
    #   rob(0...n) = max(rob(0...n-1), rob(1...n))
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        return max(self.rob_all(nums[0:-1]), self.rob_all(nums[1:]))

    def rob_all(self, nums):
        length = len(nums)
        pre, cur = 0, nums[0]
        for i in range(1, length):
            temp = pre + nums[i]
            pre = cur
            cur = max(temp, cur)
        return cur

    # 12/27 - Revisit
    # Twice DP
    def rob_revisit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        length = len(nums)
        if length == 1:
            return nums[0]

        dp1 = [0] * length
        dp1[1] = nums[0]
        dp2 = [0] * length
        dp2[1] = nums[1]

        for i in range(1, length-1):
            dp1[i+1] = max(dp1[i], dp1[i-1] + nums[i])
            dp2[i+1] = max(dp2[i], dp2[i-1] + nums[i+1])
        return max(dp1[-1], dp2[-1])


def main():
    test = HouseRobbery2()
    print test.rob([1])
    print test.rob([2, 7, 9, 3, 1])
    print test.rob([4, 1, 2, 7, 5, 3, 1])
    print test.rob([2, 2, 4, 3, 2, 5])

if __name__ == '__main__':
    main()
