# 6/25 - Binary Search Tree
# Given an array of integers, find out whether there are two distinct indices i and j 
# in the array such that the difference between nums[i] and nums[j] is at most t and 
# the difference between i and j is at most k.
#
# Revisit - 1/1
# BFS - use TreeSet to maintain the search window


class ContainDuplicate3:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}

    # Test on LeetCode - TLE e.g. [0,2147483647], k=1, t=2147483647
    # range of j is greatly expanded, and potentially overflow (for statically typed languages)
    def contains_nearby_almost_duplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if nums is None or len(nums) < 2:
            return False
        dict = {nums[0]: 0}
        length = len(nums)
        for i in range(1, length):
            n = nums[i]
            for j in range(n-t, n+t+1):
                if j in dict and i - dict[j] <= k:
                    return True
            dict[n] = i
        return False

    # Revisit - 1/1
    # Idea:
    #   Since there is now a constraint on the range of the values of the elements to be considered duplicates,
    # it reminds us of doing a range check which is implemented in tree data structure and would take
    # O(LogN) if a balanced tree structure is used, or doing a bucket check which is constant time.
    def contains_nearby_almost_duplicate_bucket(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        dict = {}
        for i in range(len(nums)):
            bucket = nums[i] / (t+1)  # hash into bucket
            for key in [bucket-1, bucket, bucket+1]:  # can be in any neighbor bucket
                if key in dict and abs(dict[key] - nums[i]) <= t:
                    return True
            # since values in the same bucket are considered duplicates, it is safe to update dictionary.
            dict[bucket] = nums[i]
            if i >= k:  # maintain the search window (delete early values)
                pop_key = nums[i-k] / (t+1)
                dict.pop(pop_key)
        return False


def main():
    test = ContainDuplicate3()
    #print test.contains_nearby_almost_duplicate([2, 1, 3, 4, 3, 2, 3, 1], 1, 2)
    print test.contains_nearby_almost_duplicate([1,3,1], 2, 1)


if __name__ == '__main__':
    main()

