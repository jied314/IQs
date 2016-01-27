# 1/27 - not in LC
# Interleave two linked-list.
# For example: Given 1->2->3->4 & 5->6, return 1->5->2->6->3->4.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def interleave_iterative(self, p, q):
        dummy = ListNode(-1)
        pre = dummy
        while p is not None and q is not None:
            pn, qn = p.next, q.next
            pre.next = p
            p.next = q
            pre = q
            p, q = pn, qn
        if p is None:
            pre.next = q
        else:
            pre.next = p
        return dummy.next

    def interleave_recursive(self, p, q):
        if p is None:
            return q
        if q is None:
            return p
        q.next = self.interleave_recursive(p.next, q.next)
        p.next = q
        return p
