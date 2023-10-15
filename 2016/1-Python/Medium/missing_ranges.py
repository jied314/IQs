# 1/12
# Given a sorted integer array where the range of elements are [0, 99] inclusive, return its missing ranges.
# For example, given [0, 1, 3, 50, 75], return ["2", "4->49", "51->74", "76->99"]
# Source - Yanxing
# Time Complexity - O(N)
# Edge Cases: empty array, or no missing values


class Solution(object):
    # Idea:
    #   find non-contiguous values and form the range
    def find_missing_ranges(self, nums, lower, upper):
        ret = []
        # check if first is 0
        if nums[0] != 0:
            r = "0"
            if nums[0] > 1:
                r += "->" + str(nums[0]-1)
            ret.append(r)

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                r = str(nums[i-1]+1)
                if nums[i] - nums[i-1] > 2:
                    r += "->" + str(nums[i]-1)
                ret.append(r)

        # check if last is 99
        if nums[-1] != 99:
            r = "99"
            if nums[-1] < 98:
                r = str(nums[-1]+1) + "->" + r
            ret.append(r)
        return ret

    # Idea:
    #   similar idea, but use pre and after to find ranges (use special value to avoid checking start and end)
    def find_missing_ranges_nice(self, nums, lower, upper):
        ret = []
        pre = lower - 1
        for i in range(0, len(nums)+1):
            after = upper + 1 if i == len(nums) else nums[i]
            if pre + 2 == after:
                ret.append(str(pre+1))
            elif pre + 2 < after:
                ret.append(str(pre+1) + "->" + str(after-1))
            pre = after
        return ret

test = Solution()
print test.find_missing_ranges([1, 3, 50, 75], 0, 99)
print test.find_missing_ranges_nice([1, 3, 50, 75], 0, 99)