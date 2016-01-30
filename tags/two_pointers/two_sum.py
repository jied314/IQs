# 12/3 - Array, Hash Table
# Given an array of integers, find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target,
# where index1 must be less than index2. Please note that your returned answers (both index1 and index2)
# are not zero-based.
# You may assume that each input would have exactly one solution.
#   Input: numbers={2, 7, 11, 15}, target=9
#   Output: index1=1, index2=2
#
class TwoSum(object):
    # Test on LeetCode - 44ms
    # Idea:
    #   sort the array, then find the two numbers (two pointers).
    #   find the original index and remember to sort then in ascending order.
    # Time Complexity - O(N*N)
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        array = sorted(nums)
        length = len(array)
        i, j = 0, length - 1
        while i < j:
            sum = array[i] + array[j]
            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else:
                break
        index1 = nums.index(array[i])
        if array[i] == array[j]:  # duplicates
            for index in range(index1+1, length):
                if nums[index] == array[j]:
                    index2 = index
                    break
        else:
            index2 = nums.index(array[j])
        ret = [index1+1, index2+1]
        ret.sort()
        return ret

    # Time Complexity - O(N), Memory Complexity - O(N)
    # Test on LeetCode - 52ms
    # Idea:
    #   use hash map to store numbers and search for numbers
    #   sequence matters to have short code
    def two_sum_hash(self, nums, target):
        length = len(nums)
        num_dict = {}
        ret = [1, 1]
        for i in range(0, length):
            num = nums[i]
            rest = target - num
            if rest in num_dict:
                ret[0] = num_dict.get(rest)
                ret[1] = i + 1
                break
            num_dict[num] = i + 1
        return ret

test = TwoSum()
print test.two_sum([2, 7, 11, 15], 18)
print test.two_sum([0, 4, 3, 0], 0)
print test.two_sum_hash([-1,-2,-3,-4,-5], -8)