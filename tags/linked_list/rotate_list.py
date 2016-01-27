# 10/20 - LL, Two Pointers (M)
# Given a list, rotate the list to the right by k places, where k is non-negative.
# For example:
#   Given 1->2->3->4->5->NULL and k = 2, return 4->5->1->2->3->NULL.

import lib

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class RotateList(object):
    # Test on LeetCode - 64ms
    # Idea:
    #   use two pointers with span = k to find the start of the new list. rotate the list.
    #   note when k >= length, k %= length
    def rotate_right(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: 
        """
        if k == 0 or head is None:
            return head

        dummy_head = ListNode(-1)
        dummy_head.next = head
        new_head_pre, node = dummy_head, dummy_head

        # traverse the list to reach the right starting node with distance = k to head
        # note if k >= length
        i = 0
        while i < k:
            node = node.next
            i += 1
            if node.next is None:  # reaching the end, i is list length
                k %= i  # adjust k
                if k == 0:
                    dummy_head.next = None
                    return head
                i = 0
                node = dummy_head

        # have two pointers with span = k
        while node.next is not None:
            node = node.next
            new_head_pre = new_head_pre.next
        # now node is at the tail, while new_head_pre.next is the new head
        node.next = dummy_head.next
        new_head = new_head_pre.next
        new_head_pre.next = None

        dummy_head.next = None
        return new_head

    # Test on LeetCode - 56ms
    # borrow from Yanxing
    def rotate_right_nice(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 0:
            return head

        # compute length
        node = head
        i = 1
        while node.next is not None:
            node = node.next
            i += 1
        length = i
        k %= length
        if k == 0:
            return head
        node.next = head

        # move node to right before
        node = head
        for i in range(0, length-k-1):
            node = node.next
        ret = node.next
        node.next = None
        return ret


def main():
    ll1 = lib.build_ll([1,2,3,4,5])
    ll2 = lib.build_ll([1,2])
    ll3 = lib.build_ll([])
    test = RotateList()
    new_ll = test.rotate_right(ll3, 7)
    print lib.traverse_ll(new_ll)


if __name__ == '__main__':
    main()

