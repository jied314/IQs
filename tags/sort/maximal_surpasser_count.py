# 1/30 - Sort, not in LC
# For an array, return the maximal number of surpassers.
# For an array element a[i], its surpasser can be a[j] if j > i and a[j] > a[i].
# For example:
#   [10, 3, 7, 1, 23, 14, 6, 9], the surpasser for 10 is 23, 14, so the count is 2.
# while the surpasser for 3 is 7,23,14,6,9, and the count is 5. It has the most surpassers and return 5.
#
# Idea:
#   Divide and Conquer, use the skeleton of merge-sort
#   basically, find the number of in-order pairs
#   for each out-of-order pair, do as usual; for in-order pair, add the counts (tricky)

class Solution(object):
    def __init__(self):
        self.max_count = 0
        self.counts = {}
        self.nums = []
        self.temp = []

    def max_surpasser(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        self.nums = nums
        self.temp = [0] * len(nums)
        for n in nums:
            self.counts[n] = 0
        self.sort(0, len(nums)-1)
        return self.max_count

    def sort(self, left, right):
        if left >= right:
            return
        mid = left + (right - left) / 2
        self.sort(left, mid)
        self.sort(mid+1, right)
        self.merge(left, mid, right)

    def merge(self, left, mid, right):
        if left >= right:
            return
        i, j = left, mid+1
        cur = left
        while i <= mid and j <= right:
            if self.nums[i] > self.nums[j]:  # out-of-order pair, merge
                self.temp[cur] = self.nums[j]
                cur += 1
                j += 1
            else:  # in-order pair, add the count (the count of unmerged right array elements)
                self.counts[self.nums[i]] += right - j + 1
                self.max_count = max(self.max_count, self.counts[self.nums[i]])
                self.temp[cur] = self.nums[i]
                i += 1
                cur += 1
        while i <= mid:
            self.temp[cur] = self.nums[i]
            cur += 1
            i += 1
        while j <= right:
            self.temp[cur] = self.nums[j]
            cur += 1
            j += 1
        # update array
        self.nums[left: right+1] = self.temp[left: right+1]


test = Solution()
print test.max_surpasser([10, 3, 7, 1, 23, 14, 6, 9])