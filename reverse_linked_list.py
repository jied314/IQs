# Linked List - Reverse Linked List
# Reverse a singly linked list.
# Note:
#   Iterative & Recursive
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
class ReverseLinkedList:
    # @param {ListNode} head
    # @return {ListNode}

    # test on LeetCode - 52ms
    def reverseList_iterative(self, head):
    	node = head
    	if node:
	    	prev = None
	    	while node.next:
	    		next = node.next
	    		node.next = prev
	    		prev = node
	    		node = next
	    	node.next = prev
    	return node

    # test on LeetCode - 100ms
    def reverseList_recursive1(self, head):
    	node = head
    	if node:
	    	node = self.revert(node, None)
    	return node

    def revert(self, current, prev):
    	if current.next:
    		next = current.next
    		current.next = prev
    		prev = current
    		current = next
    		return self.revert(current, prev)
    	else:
    		current.next = prev
    		return current

        