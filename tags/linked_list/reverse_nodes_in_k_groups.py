# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import lib


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 1:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        node = dummy
        while node.next is not None:
            i = 0
            while node is not None and i < k:
                node = node.next
                i += 1
            if node is None:
                break
            else:  # i == k
                next = node.next
                rh, rt = self.reverse(pre.next, next)
                pre.next = rh
                rt.next = next
                pre = rt
                node = pre
        return dummy.next

    def reverse(self, head, tail):
        new_head, new_tail = None, head
        node = head
        while node != tail:
            next = node.next
            node.next = new_head
            new_head = node
            node = next
        return [new_head, new_tail]

    # 1/26 - borrowed from Yanxing
    # Test on LC - 80ms, 32%
    def reverse_k_groups_nice(self, head, k):
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        count = 0
        while head is not None:
            count += 1
            if count % k == 0:
                last = pre.next
                next = head.next
                pre.next = self.reverse_between(pre.next, head.next)
                pre = last
                head = next
                last.next = head
            else:
                head = head.next
        return dummy.next

    # recursively reverse
    def reverse_between(self, head, end):
        if head is None or head.next == end:
            return head
        next = head.next
        new_head = self.reverse_between(next, end)
        next.next = head
        head.next = None
        return new_head

test = Solution()
ll = lib.build_ll([1,2,3,4,5])
print lib.traverse_ll(test.reverseKGroup(ll, 3))