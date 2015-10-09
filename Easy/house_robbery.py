# Dynamic Programming - House Robber
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.
# No two adjacent houses can be robbery at the same night.
#
# Note:
#   only need to know the previous two values
#
class HouseRobbery:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        result = []
        for i in range(0, len(nums) + 1):
            if i == 0:
                value = 0
            elif i == 1:
                value = nums[i - 1]
            else:
                value = max(result[i - 1], result[i - 2] + nums[i - 1])
            result.append(value)
        #print result
        return result[len(nums)]

    def rob_memory(self, nums):
        result = []
        for i in range(0, len(nums) + 1):
            if i == 0:
                result.append(0)
            elif i == 1:
                result.append(nums[i - 1])
            else:
                value = max(result[1], result[0] + nums[i - 1])
                result[0] = result[1]
                result[1] = value
        #print result
        return result[len(result) - 1]


def main():
    test = HouseRobbery()
    print test.rob_memory([4, 2, 3, 2])

if __name__ == '__main__':
    main()
