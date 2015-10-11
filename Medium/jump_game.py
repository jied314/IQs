# 10/10 - Array, Greedy (M)
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.
# For example:
#   A = [2,3,1,1,4], return true.
#   A = [3,2,1,0,4], return false.
#
class JumpGame(object):
    # Test on LeetCode - 128ms
    # Idea:
    #   record max index can go so far
    def can_jump_dp(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False
        result = False
        length = len(nums) - 1
        if length == 0:
            return True
        max_so_far = 0
        for i in range(0, length):
            if i > max_so_far:
                break
            max_so_far = max(max_so_far, i + nums[i])
            if max_so_far >= length:
                result = True
                break
        return result

    # Test on LeetCode - 48ms
    # Same idea, but simpler code
    def can_jump_dp_nice(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False
        length = len(nums)
        max_so_far = 0
        for i in range(0, length):
            if i > max_so_far:
                return False
            max_so_far = max(max_so_far, i + nums[i])
        return True

    # Test on LeetCode - 132ms
    # Idea:
    #   backward, move last index.
    def can_jump_nice(self, nums):
        if nums is None or len(nums) == 0:
            return False
        length = len(nums)
        last = length - 1
        for i in range(length-2, -1, -1):
            if i + nums[i] >= last:
                last = i
        return last <= 0

def main():
    test = JumpGame()
    print test.can_jump_nice([])
    print test.can_jump_nice([1])
    print test.can_jump_nice([2, 3, 1, 1, 4])
    print test.can_jump_nice([3, 2, 1, 0, 4])
    print test.can_jump_nice([1, 0, 0, 1, 4])

if __name__ == '__main__':
    main()
