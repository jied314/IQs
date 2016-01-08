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
        CombinationSum.result = []
        candidates.qsort()
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

    def combination_sum_revisit(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        CombinationSum.result = []
        candidates.qsort()
        if len(candidates) == 0 or target < candidates[0]:
            return []
        length = len(candidates)
        self.helper([], candidates, 0, length-1, target)
        return CombinationSum.result

    def helper(self, base, candidates, start, end, target):
        if target == 0:
            CombinationSum.result.append(copy.deepcopy(base))
            return
        if start <= end:
            for i in range(start, end+1):
                num = candidates[i]
                if target >= num:
                    max_count = target / num
                    base.extend([num] * max_count)
                    for j in range(max_count, 0, -1):
                        self.helper(base, candidates, i+1, end, target-(num * j))
                        base.pop()
                else:
                    break

    # 12/26 - Revisit
    # DP - T(N) = candidate + T(N-candidate)
    # Note: sift T(N-candidate) using if candidates[j] <= l[0]:
    def combination_sum_dp(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.qsort()
        if len(candidates) == 0 or target < candidates[0]:
            return []
        length = len(candidates)
        dp = [[[]]] * (target+1)
        for i in range(1, target+1):
            cur = []
            for j in range(0, length):
                num = candidates[j]
                if num > i:
                    break
                if i == num:
                    cur.append([i])
                else:
                    for l in dp[i - num]:
                        if num <= l[0]:  # sift -> avoid duplicates
                            cur.append([num] + l)
            dp[i] = cur
        return dp[target]


def main():
    test = CombinationSum()
    print test.combination_sum_recursive([8,7,4,3], 11)
    print test.combination_sum_revisit([8,7,4,3], 11)
    print test.combination_sum_dp([8,7,4,3], 11)

if __name__ == '__main__':
    main()
