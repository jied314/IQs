# 8/17 - Array, BackTracking
# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where
# the candidate numbers sums to T.
# Each number in C may only be used once in the combination.
# Note:
#   All numbers (including target) will be positive integers.
#   Elements in a combination (a1, a2, ..., ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
#   The solution set must not contain duplicate combinations.
#   For example, given candidate set 10,1,2,7,6,1,5 and target 8,
#   A solution set is: [1, 7], [1, 2, 5], [2, 6], [1, 1, 6]
#

import copy

class CombinationSum2:
    result = []  # static variable to store result

    # Test on LeetCode - 116ms
    # use less copy.deepcopy
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combination_sum_recursive(self, candidates, target):
        CombinationSum2.result = []
        candidates.reverse()
        length = len(candidates)
        self.visit([], target, 0, candidates, length)
        return CombinationSum2.result

    def visit(self, base, left, index, candidates, length):
        if left == 0:
            CombinationSum2.result.append(copy.deepcopy(base))  # need deepcopy
        else:
            if self.is_promising(left, index, candidates, length):
                j = 1
                num = candidates[index]
                while index < length-1 and candidates[index] == candidates[index+1]:
                    index += 1
                    j += 1
                index += 1
                if j > 1:  # contains duplicates
                    j = min(j, left/num)
                    for i in range(j, 0, -1):
                        base.append(num)
                        left -= num
                    for i in range(0, j):
                        self.visit(base, left, index, candidates, length)
                        base.pop()
                        left += num
                    self.visit(base, left, index, candidates, length)
                else:  # no duplicates
                    base.append(num)
                    self.visit(base, left-num, index, candidates, length)
                    base.pop()
                    self.visit(base, left, index, candidates, length)

    def is_promising(self, left, index, candidates, length):
        return index < length and left >= candidates[index]

def main():
    test = CombinationSum2()
    # print test.combination_sum_recursive([10,1,2,7,6,1,5], 8)
    print test.combination_sum_recursive([1], 2)


if __name__ == '__main__':
    main()
