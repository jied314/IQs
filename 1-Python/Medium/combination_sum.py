# 8/16 - Array, BackTracking
# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate
# numbers sums to T.
# The same repeated number may be chosen from C unlimited number of times.
# Note:
#   All numbers (including target) will be positive integers.
#   Elements in a combination (a1, a2, ..., ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
#   The solution set must not contain duplicate combinations.
#   For example, given candidate set 10,1,2,7,6,1,5 and target 8,
# For example, given candidate set 2,3,6,7 and target 7,
# A solution set is: [7], [2, 2, 3]
# Complexity - O(2^n) Time (expand the search space exponentially)

import copy

class CombinationSum:
    result = []  # static variable to store result

    # Test on LeetCode - 140ms
    # use less copy.deepcopy
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combination_sum_recursive(self, candidates, target):
        candidates.reverse()
        for i in range(0, len(candidates)):
            num = candidates[i]
            self.visit([num], num, i, candidates, target)
        return CombinationSum.result

    def visit(self, base, base_sum, index, candidates, target):
        if base_sum == target:
            CombinationSum.result.append(copy.deepcopy(base))  # need deepcopy
        else:
            for i in range(index, len(candidates)):
                num = candidates[i]
                if base_sum + num <= target:
                    # temp = copy.deepcopy(base) # too much deepcopy
                    # temp.append(num)
                    base.append(num)
                    self.visit(base, base_sum+num, i, candidates, target)
                    base.pop()  # avoid frequent deepcopy


def main():
    test = CombinationSum()
    print test.combination_sum_recursive([8,7,4,3], 11)


if __name__ == '__main__':
    main()
