# 8/22 -
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order,
#  not the kth distinct element.
# For example,
#   Given [3,2,1,5,6,4] and k = 2, return 5.
#
class KthLargestElementInArray(object):
    # Test on LeetCode - 52ms
    # Idea: use quick sort
    def find_kth_largest_quick_sort(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.find_kth_largest_quick_sort_helper(nums, 0, len(nums)-1, k)

    def find_kth_largest_quick_sort_helper(self, nums, start, end, k):
        if start <= end:
            q = self.partition(nums, start, end)
            if k - 1 == q:  # find
                return nums[q]
            elif k - 1 > q:  # search right
                return self.find_kth_largest_quick_sort_helper(nums, q+1, end, k)
            else:  # search left
                return self.find_kth_largest_quick_sort_helper(nums, start, q-1, k)

    def partition(self, nums, p, r):
        pivot = nums[r]
        i = p - 1
        for j in range(p, r):
            if nums[j] >= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[r] = nums[r], nums[i+1]
        return i+1


def main():
    test = KthLargestElementInArray()
    print test.find_kth_largest_quick_sort([3,2,1,5,6,4], 2)
    print test.find_kth_largest_quick_sort([2,1], 1)


if __name__ == "__main__":
    main()

