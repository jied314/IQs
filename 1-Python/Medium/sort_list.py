# 8/2 - LL, Sort
# Sort a linked list in O(n log n) time using constant space complexity.
# Idea - modify Merge Sort
#   O(nlgn) Time Complexity with O(1) Memory Complexity, also stable performance.
#   Array Merge Sort uses O(n) memory in merge step, while for LL no need. (manipulate pointers)
#   1. multiple scan, each time solve 2 ** i nodes
#   2. sort while scanning - sort first two, next two, then merge; repeat until reach the end (no multiple scan, but
#      needs O(n) memory.
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Test on LeetCode - 448ms
class SortList:
    # @param {ListNode} head
    # @return {ListNode}
    def sort_list(self, head):
        node = head
        length = 0
        while node:
            length += 1
            node = node.next

        dummy_head = ListNode(0)
        dummy_head.next = head
        unit_size = 1

        # each loop, sort and merge sublists
        while unit_size < length:
            index = 0
            node = dummy_head.next
            tail = dummy_head
            while index < length:  # use index to help track progress
                # find size_a and size_b
                size_a = min(length - index, unit_size)
                size_b = min(length - index - size_a, unit_size)

                # find b and new start, init end of each unit as None
                a = node
                b = None
                if size_b > 0:
                    for i in range(0, size_a-1):
                        node = node.next
                    b = node.next
                    node.next = None
                    node = b
                    for i in range(0, size_b-1):
                        node = node.next
                    temp = node.next
                    node.next = None
                    node = temp  # new start

                # merge and find tail
                new_node = tail
                while a is not None and b is not None:
                    if a.val < b.val:
                        new_node.next = a
                        a = a.next
                    else:
                        new_node.next = b
                        b = b.next
                    new_node = new_node.next
                if a is not None:
                    new_node.next = a
                    while a.next is not None:
                        a = a.next
                    tail = a
                else:
                    new_node.next = b
                    while b.next is not None:
                        b = b.next
                    tail = b
                index += size_a + size_b
                self.traverse(dummy_head.next)
            unit_size <<= 1
        return dummy_head.next

    def traverse(self, head):
        result = []
        while head is not None:
            result.append(head.val)
            head = head.next
        print result


# 1/2 - Revisit
# Quick Sort - but worst case can be O(N*N), Space Complexity - O(lgN) due to recursion
# Reason for TLE - not handle duplicates well
# see Yanxing's version
class SolutionQuickSort(object):
    # my trial - TLE
    def sort_list_tle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        return self.sort(head)[0]

    # construct two new lists using existing nodes
    def sort(self, node):
        if node.next is None:
            return [node, node]
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        hh, ht, th, tt = dummy1, dummy1, dummy2, dummy2
        pivot = node
        node = node.next
        pivot.next = None
        while node is not None:
            next = node.next
            node.next = None
            if node.val < pivot.val:
                ht.next = node
                ht = node
            else:
                tt.next = node
                tt = node
            node = next

        if hh.next is None:
            small_head, small_tail = pivot, pivot
        else:
            small_head, small_tail = self.sort(hh.next)
            small_tail.next = pivot
        if th.next is None:
            large_head, large_tail = pivot, pivot
        else:
            large_head, large_tail = self.sort(th.next)
            pivot.next = large_head
        return [small_head, large_tail]

    # 1/2 - borrow from Yanxing
    # Test on LeetCode - 216ms, 95%
    # handle duplicates in quicksort
    def sort_list_nice(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.qsort(head, None)

    # use i and ii
    def qsort(self, start, end):
        if start is None or start == end:
            return start
        pi = None  # record the right position for pivot
        pivot_val = start.val  # use the first node as pivot
        ni, nii = 0, 0  # ni - count of smallers, nii - count of equals
        # i - start of greater of equals, ii - start of greater
        node, i, ii = start.next, start.next, start.next
        while node != end:
            if node.val < pivot_val:  # swap and adjust i,
                if i != node:
                    i.val, node.val = node.val, i.val
                pi = i
                i = i.next
                ni += 1
                if ni > nii:
                    ii = i
                    nii = ni
            elif node.val == pivot_val:
                if ii != node:
                    ii.val, node.val = node.val, ii.val
                ii = ii.next
                nii += 1
            node = node.next

        if pi is not None:
            pi.val, start.val = start.val, pi.val
            self.qsort(start, pi)
        self.qsort(ii, end)
        return start



def main():
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)
    six = ListNode(6)
    three.next = five
    five.next = one
    one.next = six
    six.next = four
    four.next = two
    l = three
    test = SortList()
    test.sort_list(l)


if __name__ == '__main__':
    main()

        