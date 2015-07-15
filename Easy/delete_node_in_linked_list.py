# 7/15 - Easy, Linked List
# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
# Note:
#   node = node.next  # Wrong, node just points differently, doesn't actually change the linked list
#   also, cannot delete the tail
class DeleteNodeInLinkedList:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def delete_node(self, node):
        node.val = node.next.val
        node.next = node.next.next
