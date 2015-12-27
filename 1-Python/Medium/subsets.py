# 8/18 - Array, BackTracking, Bit Manipulation
# Given a set of distinct integers, nums, return all possible subsets.
# Note:
#   Elements in a subset must be in non-descending order.
#   The solution set must not contain duplicate subsets.
#
# Solution:
#   1. BackTracking - expand the search space
#   2. Bit Manipulation - use bit to indicate whether including an array member
import copy

class Subsets:
    result = []
    # @param {integer[]} nums
    # @return {integer[][]}

    # Test on LeetCode - 72ms
    # Time Complexity - O()
    def subsets_backtracking(self, nums):
        Subsets.result = []
        nums.sort()
        length = len(nums)
        self.visit([], 0, nums, length)
        return Subsets.result

    def visit(self, base, index, nums, length):
        if index <= length:
            Subsets.result.append(copy.deepcopy(base))
            for i in range(index, length):
                base.append(nums[i])
                self.visit(base, i+1, nums, length)
                base.pop()

    # Test on LeetCode - 80ms
    # Idea:
    #  start with -> visit 1 -> visit 2   -> visit 3
    #       []    ->   [1]   -> [2] [1,2] -> [3] [1,3] [2,3] [1,2,3]
    # can also be viewed as dynamic programming
    def subsets_iterative(self, nums):
        Subsets.result = [[]]
        nums.sort()
        for n in nums:
            result = Subsets.result
            length = len(result)
            for i in range(0, length):
                candidate = copy.deepcopy(result[i])
                candidate.append(n)
                Subsets.result.append(candidate)
        return Subsets.result

    # Test on LeetCode - 68ms
    # Because 2**N subsets, can be chosen based on bit patterns.
    def subsets_bit1(self, nums):
        Subsets.result = []
        nums.sort()
        length = len(nums)
        total = 1 << length
        for n in range(0, total):
            candidate = []
            for i in range(0, length):
                if n & (1 << i):
                    candidate.append(nums[i])
            Subsets.result.append(candidate)
        return Subsets.result

    # Test on LeetCode - 60ms (faster than 1)
    # insert only if the nth bit is set, less bit shifting
    def subsets_bit2(self, nums):
        nums.sort()
        length = len(nums)
        total = 1 << length
        Subsets.result = [[] for n in range(0, total)]
        for i in range(0, length):
            for n in range(0, total):
                if n & (1 << i):
                    Subsets.result[n].append(nums[i])
        return Subsets.result


def main():
    test = Subsets()
    print test.subsets_bit1([1,2])
    print test.subsets_backtracking([1,2,3])
    print test.subsets_iterative([1,2,3])


if __name__ == '__main__':
    main()