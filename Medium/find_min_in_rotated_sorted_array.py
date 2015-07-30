# 7/3 - Array, Binary Search
# Note:
#   1. associate sorted array with binary search
#   2. nums[l] > nums[r] - property of rotated array
class FindMinInRotatedSortedArray:
    # @param {integer[]} nums
    # @return {integer}
    # Test on LeetCode - 80ms
    def find_min(self, nums):
        min = nums[0]
        flag = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                min = nums[i]
                if flag == 1:  # find rotating point
                    break
                flag = -1  # descend
            else:
                if flag == -1:  # find rotating point
                    break
                flag = 1  # ascend
        return min

    # Test on LeetCode - 52ms
    def find_min_bs(self, nums):
        l = 0
        r = len(nums) - 1
        while nums[l] > nums[r]:
            m = (l + r) / 2
            if nums[m] > nums[l]:  # min is [m + 1, r]
                l = m + 1
            elif nums[m] < nums[l]:  # min is [l, m]
                r = m
            else:
                return nums[r]
        return nums[l]


def main():
    test = FindMinInRotatedSortedArray()
    print test.find_min_bs([4,5,6,7,0,1,2])
    print test.find_min_bs([4,1,2])
    print test.find_min([3,2,1,7,6,5,4])

if __name__ == '__main__':
    main()