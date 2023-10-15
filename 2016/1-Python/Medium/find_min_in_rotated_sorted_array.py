# 7/3 - Array, Binary Search
# Note:
#   1. associate sorted array with binary search
#   2. Value Comparison: nums[l] > nums[r] - property of rotated array, or else return nums[l]
#      should return nums[l], since for immediately detected sorted array should return nums[0]
#   3. Index Comparison: l < r, only works for comparing against nums[r], not nums[r]
#      However, cannot detect sorted array immediately, e.g. [1,2,3]
class FindMinInRotatedSortedArray:
    # @param {integer[]} nums
    # @return {integer}
    # Test on LeetCode - 80ms
    def find_min(self, nums):
        result = nums[0]
        flag = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                result = nums[i]
                if flag == 1:  # find rotating point
                    break
                flag = -1  # descend
            else:
                if flag == -1:  # find rotating point
                    break
                flag = 1  # ascend
        return result

    # Test on LeetCode - 48ms
    # compare to nums[l]
    def find_min_comparison_left1(self, nums):
        l = 0
        r = len(nums) - 1
        while nums[l] > nums[r]:
            m = (l + r) / 2
            if nums[m] >= nums[l]:  # min is [m + 1, r]
                l = m + 1
            else:  # nums[m] < nums[l]:  # min is [l, m]
                r = m
        return nums[l]

    # Test on LeetCode - 52ms
    # compare to nums[l]; also if equal, return immediately
    # exactly the same as find_min_comparison_right2 except comparing to nums[l]
    def find_min_comparison_left2(self, nums):
        l = 0
        r = len(nums) - 1
        while nums[l] > nums[r]:
            m = (l + r) / 2
            if nums[m] > nums[l]:  # min is [m + 1, r]
                l = m + 1
            elif nums[m] < nums[l]:  # min is [l, m]
                r = m
            else:  # cannot omit checking equality
                return nums[r]
        return nums[l]

    # Test on LeetCode - 52ms
    def find_min_comparison_right1(self, nums):
        l = 0
        r = len(nums) - 1
        while nums[l] > nums[r]:
            m = l + (r - l) / 2
            if nums[m] > nums[r]:  # min is [m + 1, r]
                l = m + 1
            else:  # nums[m] <= nums[r], min is [l, m]
                r = m
        return nums[l]

    # Test on LeetCode - 40ms
    def find_min_comparison_right2(self, nums):
        l = 0
        r = len(nums) - 1
        while nums[l] > nums[r]:
            m = l + (r - l) / 2
            if nums[m] > nums[r]:  # min is [m + 1, r]
                l = m + 1
            elif nums[m] < nums[r]:  # min is [l, m]
                r = m
            else:
                return nums[r]
        return nums[l]

    # Test on LeetCode - 56ms
    # comparison only works with nums[r], not nums[l]
    def find_min_index(self, nums):
        l = 0
        r = len(nums) - 1
        while l < r:
            m = l + (r - l) / 2
            if nums[m] > nums[r]:  # min is [m + 1, r]
                l = m + 1
            else:  # nums[m] <= nums[r], min is [l, m]
                r = m
        return nums[l]


def main():
    test = FindMinInRotatedSortedArray()
    print test.find_min_comparison_right1([4,5,6,7,0,1,2])
    print test.find_min_index([1,2])
    print test.find_min_index([2,1])
    print test.find_min([3,2,1,7,6,5,4])

if __name__ == '__main__':
    main()