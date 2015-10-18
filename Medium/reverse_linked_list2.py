import lib

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 10/14 - LL
# Reverse a linked list from position m to n. Do it in-place and in one-pass.
# For example: Given 1->2->3->4->5->NULL, m = 2 and n = 4, return 1->4->3->2->5->NULL.
# Note:
#   Given m, n satisfy the following condition: 1 <= m <= n <= length of list.
#
class ReverseLinkedList2(object):
    # Test on LeetCode - 48ms
    # Idea:
    #   use another ll to hold the reversed part
    #   special case: m = n
    def reverse_between(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy_head = ListNode(0)
        dummy_head.next = head
        if n == m:
            return dummy_head.next
        i = 1
        pre = dummy_head
        while i < m:  # skip node before m
            pre = pre.next
            i += 1
        temp_head = None
        tail = pre.next
        while i < n:
            cur = pre.next
            pre.next = cur.next
            cur.next = temp_head
            temp_head = cur
            i += 1
        next = pre.next.next
        pre.next.next = temp_head
        tail.next = next
        return dummy_head.next


def main():
    test = ReverseLinkedList2()
    ll = lib.read_ll([3, 5])
    test.reverse_between(ll, 1, 2)


if __name__ == '__main__':
    main()
