# 1/17 - Heap
# Given an array nums, there is a sliding window of size k which is moving from the very left of
# the array to the very right. You can only see the k numbers in the window.
# Each time the sliding window moves right by one position.
# For example,
#   Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
#   Window position                Max
#   ---------------               -----
#   [1  3  -1] -3  5  3  6  7       3
#   1 [3  -1  -3] 5  3  6  7       3
#   1  3 [-1  -3  5] 3  6  7       5
#   1  3  -1 [-3  5  3] 6  7       5
#   1  3  -1  -3 [5  3  6] 7       6
#   1  3  -1  -3  5 [3  6  7]      7
# Therefore, return the max sliding window as [3,3,5,5,6,7].
# Note:
#   You may assume k is always valid, ie: 1 <= k <= input array's size for non-empty array.


import heapq
from collections import deque

class Solution(object):
    # TLE - O(N*lgN)
    # Use heap to maintain max
    def max_sliding_window_heap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0 or k == 0:
            return []
        if len(nums) <= k:
            return [max(nums)]
        if k == 1:
            return nums

        ret = []
        heap = nums[:k]
        heapq._heapify_max(heap)  # O(N)
        ret.append(heap[0])
        for i in range(k, len(nums)):
            remove_index = heap.index(nums[i - k])
            heap[remove_index] = heap[-1]  # remove
            heap[-1] = nums[i]  # move window right by one
            heapq.heapify(heap)  # re-heapify, or use _siftup_max
            ret.append(heap[0])
        return ret

    # Test on LC - 220ms, 63%
    # Idea - Monotonic Queue
    #  scan the array from 0 to n-1, keep "promising" elements in the deque
    #   1. if an element in the deque and it is out of i-(k-1), we discard them.
    # we just need to poll from the head, as we are using a deque and elements are ordered as the sequence in the array
    #   2. now only those elements within [i-(k-1),i] are in the deque. We then discard elements smaller than a[i] from
    # the tail. This is because if a[x] <a[i] and x<i, then a[x] has no chance to be the "max" in [i-(k-1),i],
    # or any other subsequent window: a[i] would always be a better candidate.
    #   3. As a result elements in the deque are ordered in both sequence in array and their value.
    # At each step the head of the deque is the max element in [i-(k-1),i]
    def max_sliding_window_deque(self, nums, k):
        if not nums:
            return []
        res = []
        dq = deque()  # store index
        for i in xrange(len(nums)):
            if dq and dq[0] < i-k+1:  # out of the window (front) - case 1
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:  # remove impossible candidate (small end) - case 2
                dq.pop()
            dq.append(i)
            if i >= k-1:  # valid i [k-1...length-1]] - case 3
                res.append(nums[dq[0]])
        return res

test = Solution()
print test.max_sliding_window_deque([1,3,-1,-3,5,3,6,7], 3)

