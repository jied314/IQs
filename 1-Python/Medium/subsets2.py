# 8/19 - Array, BackTracking
# Given a collection of integers that might contain duplicates, nums, return all possible subsets.
# Note:
#   Elements in a subset must be in non-descending order.
#   The solution set must not contain duplicate subsets.
import copy
class Subsets2:
    result = []

    # @param {integer[]} nums
    # @return {integer[][]}

    # Test on LeetCode - 72ms
    # faster, also logic easier
    # Idea: add element to the existing solution sets
    # note in python, s[length-x:] == s[-x:]
    def subsets_with_dup(self, nums):
        Subsets2.result = [[]]
        nums.sort()
        length = len(nums)
        if length == 0:
            return Subsets2.result

        num = nums[0]
        Subsets2.result.append([num])
        prev_num = 1
        for index in range(1, length):
            num = nums[index]
            new_length = len(Subsets2.result)
            if num == nums[index-1]:  # duplicate
                bases = copy.deepcopy(Subsets2.result[-prev_num:])  # copy candidates
            else:  # not duplicate
                prev_num = new_length
                bases = copy.deepcopy(Subsets2.result)
            for base in bases:
                base.append(num)
                Subsets2.result.append(base)

        return Subsets2.result

    # Test on LeetCode - 92ms
    # Idea:
    #   reorganize nums to group duplicates and then traverse
    #   e.g. nums = [1,2,2], new_nums = [[[1]], [[2], [2,2]]]
    def subset_with_dup2(self, nums):
        Subsets2.result = []
        nums.sort()
        length = len(nums)
        new_nums = []
        index = 1
        while index-1 < length:
            num = nums[index-1]
            base = [num]
            new_nums.append(copy.deepcopy([base]))
            # if duplicate exists
            while index < length and nums[index] == num:
                base.append(num)
                new_nums[-1].append(copy.deepcopy(base))
                index += 1
            index += 1
        self.visit2([], 0, new_nums, len(new_nums))
        return Subsets2.result
    
    def visit2(self, base, start, new_nums, length):
        Subsets2.result.append(base)
        for i in range(start, length):
            candidates = new_nums[i]
            for candidate in candidates:
                temp = copy.deepcopy(base)
                temp.extend(candidate)
                self.visit2(temp, i+1, new_nums, length)

def main():
    test = Subsets2()
    print test.subsets_with_dup([1,2,2])


if __name__ == '__main__':
    main()

