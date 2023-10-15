# 7/29 - Array, Binary Search
# Compare with FindMinInRotatedSortedArray - adjust l or r when nums[m] == nums[r]
#
class FindMinInRotatedSortedArray2:
    # @param {integer[]} nums
    # @return {integer}
    def find_min_bs(self, nums):
        l = 0
        r = len(nums) - 1
        while r > 0 and nums[l] == nums[r]:  # avoid situation like [3,1,3]
            r -= 1
        while nums[l] > nums[r]:
            # adjust l and r to avoid duplicates
            while nums[l] == nums[l+1]:
                l += 1
            while nums[r] == nums[r-1]:
                r -= 1
            # regular bs as used in find_min_in_rotated_sorted_array.py
            m = (l + r) / 2
            if nums[m] > nums[l]:  # min is [m + 1, r]
                l = m + 1
            elif nums[m] < nums[l]:  # min is [l, m]
                r = m
            else:
                return nums[r]
        return nums[l]

    # Test on LC - 44ms, 75% => should always use r
    def find_min_nice_r(self, nums):
        l = 0
        r = len(nums) - 1
        while l < r:
            m = l + (r - l)/2
            if nums[m] > nums[r]:  # min is [m + 1, r]
                l = m + 1
            elif nums[m] < nums[r]:  # min is [l, m]
                r = m
            else:  # nums[m] == nums[r]
                r -= 1
        return nums[l]

    # Test on LC - 52ms, 23%
    # compare to both ends. if duplicates, l += 1
    def find_min_revisit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l < r and nums[l] >= nums[r]:
            m = l + (r - l)/2
            if nums[m] > nums[r]:  # min is [m + 1, r]
                l = m + 1
            elif nums[m] < nums[l]:  # min is [l, m]
                r = m
            else:  # nums[m] == nums[l]
                l += 1
        return nums[l]

def main():
    test = FindMinInRotatedSortedArray2()
    print test.find_min_nice([3,3,0,0,0,1,1,2])
    print test.find_min_nice([3,1,3])
    print test.find_min_nice([1,1])

if __name__ == '__main__':
    main()