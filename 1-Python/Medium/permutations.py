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

    # Test On LeetCode - 76ms
    # Idea:
    #   start from T(n-1), insert into 0...length position
    #   [] -> [1] -> [2, 1] -> [3, 2, 1], [2, 3, 1], [2, 1, 3]
    #                [1, 2] -> [3, 1, 2], [1, 3, 2], [1, 2, 3]
    # Note:
    #   use python list +. e.g. [1] + [2] = [1, 2]
    def permute_try(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        length = len(nums)
        for i in range(0, length):
            num = nums[i]
            ret_length = len(ret)
            element_length = len(ret[0])
            for j in range(0, ret_length):
                e = ret.pop(0)
                for k in range(0, element_length+1):
                    ret.append(e[0:k] + [num] + e[k:])
        return ret

def main():
    test = Permutations()
    print len(test.permute_nice([1,2,3]))


if __name__ == '__main__':
    main()