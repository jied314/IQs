# 10/19, 20 - Backtracking, Math
# The set [1,2,3,...,n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get the following sequence (ie, for n = 3):
# "123", "132", "213", "231", "312", "321"
# Given n and k, return the kth permutation sequence.
# Note: Given n will be between 1 and 9 inclusive.


import math
class PermutationSequence(object):
    # Test on LeetCode - 48ms
    def get_permutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        return self.permutation_sequence(n, k, [str(i) for i in range(1, n+1)])

    # Idea:
    #   (n, k) = (4, 13)
    #   1. first find the min index that should be changed. 13 > 1 * 2 * 3  -> change_index = 4
    #      prefix = "", rest = [1, 2, 3, 4]
    #   2. find the right first num. (13 - 1) / 6 = 2 -> start_index = 2, prefix = "2".
    #      reduce problem to (n, k) = (3, 1)
    # Note:
    #   for special cases when k % base == 0, use (k - 1) / base
    def permutation_sequence(self, n, k, nums):
        base, change_index = 1, 0
        # find the min index that should be changed
        for i in range(1, n + 1):
            base *= i
            if base >= k:
                change_index = i
                if base > k:
                    base /= i
                break

        # find the unchanged prefix. or prefix = "".join(nums[0:n-change_index]
        prefix = ""
        for i in range(0, n - change_index):
            prefix += nums[i]

        # the rest that needs to be changed
        rest = nums[n - change_index:]
        if base == k:  # just reverse
            rest.reverse()
            suffix = "".join(rest)
        else:  # find the first changed num, reduce the problem
            """start_index = 0
            for i in range(2, change_index+1):
                if base * (i - 1) < k < base * i + 1:
                    start_index = i - 1
                    break"""
            start_index = (k - 1) / base
            prefix += rest.pop(start_index)
            suffix = self.permutation_sequence(change_index - 1, k - start_index * base, rest)
        return prefix + suffix

    # similar idea as above, but much nicer
    # adjust k first, then choose the right num one by one.
    # combine the above finding base and choose the right first one together.
    # divmod is a built-in function. (1, 1) = divmod(3, 2)
    def get_permutation_nice(self, n, k):
        array = range(1, n + 1)
        # k = (k % math.factorial(n)) - 1  # or k = (k - 1) % math.factorial(n)
        k -= 1  # adjust k for the special case as k % a == 0
        permutation = []
        for i in xrange(n - 1, -1, -1):
            idx, k = divmod(k, math.factorial(i))
            permutation.append(array.pop(idx))

        return "".join(map(str, permutation))

def main():
    test = PermutationSequence()
    print test.get_permutation(1, 1)
    print test.get_permutation(2, 2)
    print test.get_permutation(3, 4)
    print test.get_permutation(3, 5)
    print test.get_permutation(4, 6)
    print test.getPermutation_nice(4, 24)


if __name__ == "__main__":
    main()