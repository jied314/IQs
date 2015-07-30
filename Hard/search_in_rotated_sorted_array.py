# 7/30 - Array, BS
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Note:
#   1. multiple conditions using similar methods as find_min_in_rotated_sorted_array
#   2. two steps methods - easier to understand
#      note how to do bs with rotated sorted array
#
class SearchInRotatedSortedArray:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}

    # Test on LeetCode - 44ms
    # do bs based on different situations
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) / 2
            if target == nums[m]:
                return m
            if target == nums[l]:
                return l
            if target == nums[r]:
                return r
            if nums[m] >= nums[l]:  # pivot [m+1, r]
                if nums[m] >= target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:  # nums[m] < nums[l] pivot [l, m]
                if nums[r] > target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

    # first find the min, then do regular binary search
    def search_two_steps(self, nums, target):
        l = 0
        r = len(nums) - 1
        # find the index of the smallest value using binary search.
        # Loop will terminate since mid < hi, and lo or hi will shrink by at least 1.
        # Proof by contradiction that mid < hi: if mid==hi, then lo==hi and loop would have been terminated.
        while l < r:
            m = l + (r - l) / 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        # lo==hi is the index of the smallest value and also the number of places rotated.
        pivot = l
        l = 0
        n = len(nums)
        r = n - 1
        # the usual binary search and accounting for rotation.
        while l <= r:
            m = l + (r - l) / 2
            realmid = (m + pivot) % n;
            if nums[realmid] == target:
                return realmid
            if nums[realmid] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

def main():
    test = SearchInRotatedSortedArray()
    print test.search_two_steps([4,1,2,3], 2)
    print test.search([4,5,6,1,2], 5)
    print test.search([4,5,6,1,2], 3)

if __name__ == '__main__':
    main()