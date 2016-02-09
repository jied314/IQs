# 2/4 - Heap, Design
# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value.
# So the median is the mean of the two middle value.
# Examples:
#   [2,3,4] , the median is 3
#   [2,3], the median is (2 + 3) / 2 = 2.5
# Design a data structure that supports the following two operations:
#   void addNum(int num) - Add a integer number from the data stream to the data structure.
#   double findMedian() - Return the median of all elements so far.
#
# For example:
#   add(1)
#   add(2)
#   findMedian() -> 1.5
#   add(3)
#   findMedian() -> 2
#
# Idea:
#   use a max heap on left side to represent elements that are less than effective median,
# and a min heap on right side to represent elements that are greater than effective median.
import heapq


class OnlineMedian(object):
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def get_median(self):
        """
        :return: double
        """
        if len(self.max_heap) == 0:
            return 0
        if len(self.max_heap) != len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0

    def add_number(self, num):
        if len(self.max_heap) == 0 or num < -self.max_heap[0]:  # insert to max_heap
            heapq.heappush(self.max_heap, -num)
            if len(self.max_heap) - len(self.min_heap) > 1:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        else:  # insert to min_heap
            heapq.heappush(self.min_heap, num)
            if len(self.min_heap) > len(self.max_heap):
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))


test = OnlineMedian()
test.add_number(1)
print test.get_median()
test.add_number(2)
print test.get_median()
test.add_number(3)
print test.get_median()
test.add_number(4)
print test.get_median()