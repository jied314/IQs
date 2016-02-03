# 8/22 -
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order,
#  not the kth distinct element.
# For example,
#   Given [3,2,1,5,6,4] and k = 2, return 5.
#
# 12/26 - Revisit
#   Use quick sort. remember the division of smallers and largers, and swap with pivot. -> reduce shifting.
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

    # partition the array in reversed order
    def partition(self, nums, p, r):
        pivot = nums[r]
        i = p - 1
        for j in range(p, r):
            if nums[j] >= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[r] = nums[r], nums[i+1]
        return i+1

    # adapt from Yanxing
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        return self.select(nums, 0, len(nums)-1, k)

    # same idea - use quicksort
    def select(self, nums, left, right, k):
        if left == right:
            return nums[left]
        pivot = self.partition1(nums, left, right)
        count = pivot - left + 1
        if k == count:
            return nums[pivot]
        elif k < count:
            return self.select(nums, left, pivot-1, k)
        else:
            return self.select(nums, pivot+1, right, k-count)

    # 3 way partition (larger, equal, smaller)
    def partition1(self, nums, left, right):
        pivot = nums[right]
        j = left
        while j <= right:
            if nums[j] < pivot:
                nums[j], nums[right] = nums[right], nums[j]
                right -= 1
            elif nums[j] == pivot:
                j += 1
            else:
                nums[j], nums[left] = nums[left], nums[j]
                left += 1
                j += 1
        return left


def main():
    test = KthLargestElementInArray()
    print test.findKthLargest([3, 1, 2, 4], 2)
    print test.find_kth_largest_quick_sort([3,2,1,5,6,4], 2)
    print test.find_kth_largest_quick_sort([2,1], 1)


if __name__ == "__main__":
    main()

