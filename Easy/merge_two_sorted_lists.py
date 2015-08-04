# 8/1 - LL
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
# Solution:
#   1. Iterative V.S. Recursive (not good due to long stack calls)
#   2. Either choose one list and modify in place or create a new list
#   3. Use dummy head (frequently used for LL)

import sys
class MergeTwoSortedLists:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}

    # Test on LeetCode - 76ms
    def merge_two_lists_in_place(self, l1, l2):
        # init head, one, another
        if l1 is None or l1 is not None and l2 is not None and l1.val >= l2.val:
            head = l2
            another = l1
        else:
            head = l1
            another = l2
        one = head

        # form merged list
        while one is not None and another is not None:
            if one.next is None:
                one.next = another
                break
            elif another.val <= one.next.val:
                node = another
                another = another.next
                node.next = one.next
                one.next = node
            one = one.next
        return head

    # Test on LeetCode - 76ms
    def merge_two_lists_anew(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            head = ListNode(l1.val)
            l1 = l1.next
        else:
            head = ListNode(l2.val)
            l2 = l2.next

        node = head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        node.next = l1 if l1 is not None else l2
        return head

    # Test on LeetCode - 60ms
    # use dummy head and create a new list
    def merge_two_lists_dummy_head(self, l1, l2):
        dummy_head = ListNode(-sys.maxint-1)
        node = dummy_head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        node.next = l1 if l1 is not None else l2
        return dummy_head.next

    # can cause stack overflow
    def merge_two_lists_recursive(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            l1.next = self.merge_two_lists_recursive(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_lists_recursive(l2.next, l1)
            return l2


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def main():
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(4)
    l2 = ListNode(0)
    test = MergeTwoSortedLists()
    test.merge_two_lists(l1, l2)

if __name__ == '__main__':
    main()