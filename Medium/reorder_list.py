# 10/22 - LL (M)
# Given a singly linked list L: L0->L1->...->Ln-1->Ln, reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->...
# You must do this in-place without altering the nodes' values.
# For example,
#   Given {1,2,3,4}, reorder it to {1,4,2,3}.

import lib

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Test on Leetcode - 138ms
# Idea:
#   1. find the start of the second half
#   2. rotate the second half
#   3. merge the first and second halves
class Solution(object):
    def reorder_list(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return head
        mid = self.find_mid(head)
        if mid == head or mid.next == head:
            return head
        first_half = head
        second_half = self.reverse_list(mid.next)
        mid.next = None
        while second_half is not None:
            first_next = first_half.next
            second_next = second_half.next
            first_half.next = second_half
            second_half.next = first_next
            first_half = first_next
            second_half = second_next
        return head

    def find_mid(self, head):
        mid, node = head, head
        while node.next is not None and node.next.next is not None:
            mid = mid.next
            node = node.next.next
        return mid

    def reverse_list(self, head):
        pre, cur, next = None, head, None
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


def main():
    test = Solution()
    ll1 = lib.build_ll([1, 2, 3, 4, 5, 6])
    new_ll1 = test.reorder_list(ll1)
    print lib.traverse_ll(new_ll1)


if __name__ == '__main__':
    main()
