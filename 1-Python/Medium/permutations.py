# 7/6, 7/8 - Backtracking

import copy
class Permutations:
    # @param {integer[]} nums
    # @return {integer[][]}
    # Test on Leetcode - 173ms
    def permute(self, nums):
        if nums:
            if len(nums) == 1:
                return [nums]
            else:
                result = []
                for i in range(0, len(nums)):
                    head = [nums[i]]
                    cpy = copy.deepcopy(nums)
                    cpy.remove(nums[i])
                    for e in self.permute(cpy):
                        e.insert(0, head)
                        result.append(e)
                return result
        else:
            return [[]]

    # Test on LeetCode - 144ms
    # Idea: use swap
    def permute_nice(self, nums):
        result = []
        self.permutation(nums, 0, result)
        return result

    def permutation(self, nums, begin, result):
        if begin == len(nums) - 1:
            result.append(nums)
            return

        for i in range(begin, len(nums)):
            p = copy.deepcopy(nums)
            p[begin], p[i] = p[i], p[begin]
            self.permutation(p, begin+1, result)

    # Test On LeetCode - 96ms
    # No need to deepcopy, just pop & insert
    def permute_fast(self, nums):
        if not nums:
            return [[]]

        result = []
        for i in xrange(len(nums)):
            tmp = nums.pop(i)
            result = result + [[tmp] + child for child in self.permute_fast(nums)]
            nums.insert(i, tmp)

        return result


def main():
    test = Permutations()
    print len(test.permute_fast([1,2,3]))


if __name__ == '__main__':
    main()