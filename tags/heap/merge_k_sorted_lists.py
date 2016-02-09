# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
import heapq


class Solution(object):
    # TLE - O(NK)
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists is None:
            return None
        dummy = ListNode(-1)
        pre = dummy
        while True:
            next = self.get_next(lists)
            if next is None:
                break
            pre.next = next
            pre = next
        return dummy.next

    def get_next(self, lists):
        min_node_group, min_val = -1, (1 << 31) - 1
        for i in range(0, len(lists)):
            head = lists[i]
            if head is not None and head.val < min_val:
                min_node_group, min_val = i, head.val
        if min_node_group == -1:
            return None
        min_node = lists[min_node_group]
        lists[min_node_group] = lists[min_node_group].next
        return min_node

    # Idea: use heap
    # Test on LC - 144ms, 55%
    def merge_k_lists_heap(self, lists):
        dummy = ListNode(-1)
        cur = dummy
        heap = MyHeap()
        for list in lists:
            if list is not None:
                heap.push(list)
        while not heap.empty():
            small = heap.pop()
            cur.next = small
            cur = cur.next
            small = small.next
            if small is not None:
                heap.push(small)
        cur.next = None
        return dummy.next


# heap wrapper - by default, heap use the first element of the tuple to compare
class MyHeap(object):
    def __init__(self):
        self._data = []

    def push(self, item):
        heapq.heappush(self._data, (item.val, item))

    def pop(self):
        return heapq.heappop(self._data)[1]

    def empty(self):
        return len(self._data) == 0