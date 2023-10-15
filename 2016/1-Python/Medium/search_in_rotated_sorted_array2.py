# 8/5 - Array, BS
# Follow up for "Search in Rotated Sorted Array": What if duplicates are allowed?
class SearchInRotatedSortedArray2:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}

    # Test on LeetCode - 52ms
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) / 2
            if target == nums[m] or target == nums[l] or target == nums[r]:
                return True
            if nums[m] > nums[r]:  # pivot [m+1, r]
                if nums[m] > target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < nums[r]:  # pivot [l, m]
                if nums[r] > target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                r -= 1  # deal with duplicates
        return False
