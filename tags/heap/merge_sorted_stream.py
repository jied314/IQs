# 2/3 - Heap
# Given an array of Iterator, (data in the Iterator are sorted), design and implement MergeIterator class which merges
# these sorted iterators.
# Note:
#   MergeIterator only has has_next and get_next.
#   Iterator only has has_next and get_next.
import heapq


class Iterator(object):
    def __init__(self, data):
        self.data = data
        self.cur_index = 0

    # note iterator always point to the next item
    def has_next(self):
        return self.cur_index < len(self.data)

    def next(self):
        cur = self.data[self.cur_index]
        self.cur_index += 1
        return cur


class Heap(object):
    def __init__(self):
        self._data = []

    def push(self, val, item):
        heapq.heappush(self._data, (val, item))

    def pop(self):
        return heapq.heappop(self._data)

    def empty(self):
        return len(self._data) == 0


# only store K values in the heap, pop and push along the way
# Alternative is to store all values into the heap and then pop.
class MergeIterator(object):
    def __init__(self, stream):
        """
        :param stream: List[Iterator]
        :return: void
        """
        self.stream = stream
        self.heap = Heap()
        for i in range(0, len(stream)):
            iterator = stream[i]
            if not iterator.has_next():
                continue
            self.heap.push(iterator.next, i)

    def has_next(self):
        return not self.heap.empty()

    def next(self):
        ret, index = self.heap.pop()
        if self.stream[index].has_next():
            self.heap.push(self.stream[index].next, index)
        return ret



