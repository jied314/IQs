# 8/15 - Array, BackTracking
# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be
# used and each combination should be a unique set of numbers.
# Ensure that numbers within the set are sorted in ascending order.
#
# BackTracking is supposed to be depth-first search

import copy

class CombinationSum3:
    result = []  # static variable to store result

    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}

    # Test on LeetCode - 60ms
    # Slightly faster than iterative - no need to keep uppers
    def combination_sum3(self, k, n):
        CombinationSum3.result = []
        self.visit(0, k, n, [])
        return CombinationSum3.result

    def visit(self, i, k, n, combination):
        if k == 0 and n == 0:
                CombinationSum3.result.append(copy.deepcopy(combination))
        elif self.is_promising(i, k, n):
            i += 1
            """ frequent use of deepcopy
            lc = copy.deepcopy(combination)
            lc.append(i)
            rc = combination
            self.visit(i, k-1, n-i, lc)
            self.visit(i, k, n, rc)"""
            combination.append(i)
            self.visit(i, k-1, n-i, combination)
            combination.pop()  # avoid frequent use of deepcopy
            self.visit(i, k, n, combination)

    def is_promising(self, i, k, n):
        return i < 9 and n >= k * (i+1)

    # Test on LeetCode - 100ms (Not Good)
    # save parent node for the next round analysis
    def combination_sum3_iterative(self, k, n):
        CombinationSum3.result = []
        root = Node([], n)
        uppers = [root]
        for i in range(1, 10):
            lowers = []
            for node in uppers:
                if self.is_valid(k, i, node):
                    nums = copy.deepcopy(node.nums)
                    nums.append(i)
                    expand = Node(nums, node.left-i)
                    if self.is_success(k, expand):
                        CombinationSum3.result.append(expand.nums)
                    else:
                        lowers.append(expand)
                        lowers.append(node)
            uppers = lowers
        return CombinationSum3.result

    def is_valid(self, k, i, node):
        return node.left >= (k - len(node.nums)) * i

    def is_success(self, k, node):
        return node.left == 0 and len(node.nums) == k

# each node contains the following information:
# nums - the numbers included
# left - difference to make up n
class Node:
    def __init__(self, nums, left):
        self.nums = nums
        self.left = left


def main():
    test = CombinationSum3()
    print test.combination_sum3_iterative(3, 15)


if __name__ == '__main__':
    main()
