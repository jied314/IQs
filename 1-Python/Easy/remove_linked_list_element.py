# 6/16 Linked List - Remove Linked List Elements
# Solutions:
#   1. traverse the list and remove nodes
#   2. recursive
#
# Definition for singly-linked list.
# class ListNode:
# def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    # Test on LeetCode - 212ms
    def remove_elements(self, head, val):
        if head:
            current = head
            prev = None
            while current:
                if current.val == val:
                    if current == head:
                        head = head.next
                    else:
                        prev.next = current.next
                else:
                    prev = current
                current = current.next
        return head

    # Test on LeetCode - maximum recursion depth exceeded
    # Note: Not always good to use recursion - stack space
    def remove_elements_recursive(self, head, val):
        if head is None:
            return None
        head.next = self.remove_elements_recursive(head.next, val)
        return head.next if head.val == val else head
