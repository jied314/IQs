# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 8/5 - LL
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# Compare with (E)RemoveDuplicatesFromSortedList and RemoveDuplicatesFromSortedArray(1 & 2)
#
class RemoveDuplicatesFromSortedList2:
    # @param {ListNode} head
    # @return {ListNode}
    # Test on LeetCode - 72ms
    # Idea: once duplicate, skip. Record duplicate value to remove completely
    def delete_duplicates(self, head):
        if head is None or head.next is None:
            return head
        dummy_head = ListNode(0)
        dummy_head.next = head
        node = dummy_head
        duplicate = None
        while node.next is not None and node.next.next is not None:
            if node.next.val == node.next.next.val:
                node.next.next = node.next.next.next
                duplicate = node.next.val
            else:
                if duplicate is not None:
                    node.next = node.next.next
                    duplicate = None
                else:
                    node = node.next
        if duplicate is not None:
            node.next = node.next.next
        return dummy_head.next

    # Test on LeetCode - 72ms
    # for each value, exhaust all duplicates, and adjust accordingly
    def delete_duplicates_exhaust(self, head):
        if head is None or head.next is None:
            return head
        dummy_head = ListNode(0)
        dummy_head.next = head
        pre = dummy_head
        cur = head
        while cur is not None:
            while cur.next is not None and cur.val == cur.next.val:  # find the last duplicate
                cur = cur.next
            if pre.next == cur:  # no duplicate
                pre = pre.next
            else:  # has duplicate
                pre.next = cur.next
            cur = cur.next
        return dummy_head.next

    # Test on LeetCode - 80ms
    # similar to above, but reconstruct a new ll
    def delete_duplicates_exhaust_build(self, head):
        if head is None:
            return head
        dummy = ListNode(-1)
        pre = dummy
        node = head
        while node is not None:
            old = node
            while node.next is not None and node.val == node.next.val:  # find the last duplicate
                node = node.next
            if old == node:  # no duplicate
                pre.next = node
                pre = pre.next
            node = node.next
        pre.next = None
        return dummy.next