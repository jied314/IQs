# 2/3 - Heap
# You have k lists of sorted integers. Find the smallest range that includes at least one number from each of the k lists.
# For example,
#   List 1: [4, 10, 15, 24, 26]
#   List 2: [0, 9, 12, 20]
#   List 3: [5, 18, 22, 30]
# The smallest range here would be [20, 24] as it contains 24 from list 1, 20 from list 2, and 22 from list 3.
# http://www.fgdsb.com/2015/01/17/smallest-range/
#
# Idea:
#   There are k lists of sorted integers. Make a min heap of size k containing 1 element from each list.
# Keep track of min and max element and calculate the range. In min heap, minimum element is at top.
# Delete the minimum element and another element instead of that from the same list to which minimum element belong.
# Repeat the process till any one of the k list gets empty. Keep track of minimum range.
import heapq


class Solution(object):
    def min_range(self, nums):
        """
        :param nums: List[List[int]]
        :return: [int, int]
        """
        ret = []
        min_range_size = (1 << 31) - 1

        # min heap to store the current val from all lists
        temp_max = nums[0][0]
        heap = Heap()
        for i in range(0, len(nums)):
            val = nums[i][0]
            heap.push(val, i, 0)
            temp_max = max(temp_max, val)

        # init
        min_val, group, index = heap.peek()
        min_range_size = temp_max - min_val + 1
        ret = [min_val, temp_max]

        # traverse k lists, update min and max
        while index < len(nums[group]) - 1:
            min_val, group, index = heap.pop()
            if index + 1 >= len(nums[group]):
                break
            next_val = nums[group][index+1]
            heap.push(next_val, group, index+1)
            temp_max = max(temp_max, next_val)
            new_min = heap.peek()[0]
            if temp_max - new_min + 1 < min_range_size:
                min_range_size = temp_max - new_min + 1
                ret = [new_min, temp_max]
        return ret


class Heap(object):
    def __init__(self):
        self._data = []

    def push(self, val, group, index):
        heapq.heappush(self._data, (val, group, index))

    def pop(self):
        return heapq.heappop(self._data)

    def peek(self):
        return self._data[0]


test = Solution()
print test.min_range([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
print test.min_range([[1,2,4,8,14,20], [6,10,21,25,30], [3,7,9,15,25]])
print test.min_range([[1,2,3], [5,10], [4,12]])



