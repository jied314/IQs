# 2/2 - Sort
# Given an integer array, return the number of all inverse pairs.
# For example:
#   {7, 5, 6, 4}
#   There are five inverse pairs in total: (7,6), (7,5), (7,4), (6,4), (5,4)
#   The result should be 5.
# Idea:
#   MergeSort - similar to max_surpasser_count


class Solution(object):
    def __init__(self):
        self.count = 0
        self.nums = []
        self.temp = []

    def inverse_pairs(self, arr):
        """
        :param arr: List[int]
        :return: int
        """
        self.nums = arr
        self.temp = [0] * len(arr)
        self.sort(0, len(arr)-1)
        return self.count

    def sort(self, left, right):
        if left >= right:
            return
        mid = left + (right - left) / 2
        self.sort(left, mid)
        self.sort(mid+1, right)
        self.merge(left, mid, right)

    def merge(self, left, mid, right):
        i, j, k = left, mid+1, left
        while i <= mid and j <= right:
            self.temp[k] = min(self.nums[i], self.nums[j])
            k += 1
            if self.nums[i] < self.nums[j]:
                i += 1
            else:
                j += 1
                self.count += mid-i+1
        while i <= mid:
            self.temp[k] = self.nums[i]
            i += 1
            k += 1
        while j <= right:
            self.temp[k] = self.nums[j]
            j += 1
            k += 1
        self.nums[left:right+1] = self.temp[left:right+1]


test = Solution()
print test.inverse_pairs([7, 5, 6, 4])


