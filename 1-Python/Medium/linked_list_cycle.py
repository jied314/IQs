# 6/29 - Linked List, Two Pointers
# Complexity: Time - O(n), Space - O(1)

# Definition for singly-linked list.
# class ListNode:
# def __init__(self, x):
# self.val = x
#         self.next = None

class LinkedListCycle:
    # @param head, a ListNode
    # @return a boolean

    # Test on LeetCode - TLE
    def has_cycle_tle(self, head):
        visited = []
        node = head
        while node is not None:
            if node in visited:
                return True
            visited.append(node)
            node = node.next
        return False

    # Test on LeetCode - 136ms
    def has_cycle_two_pointers(self, head):
        if head:
            fast = head
            slow = head
            while fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return True
        return False