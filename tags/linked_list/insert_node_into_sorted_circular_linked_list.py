# 1/27 - not in LC
# Insert Node into Sorted Circular Linked List


class Solution(object):
    def sorted_insert(head, new_node):
        cur = head
        if cur is not None:
            new_node.next = new_node
            head = new_node
        elif cur.val >= new_node.val:
            # If value is smaller than head's value then we need to change next of last node
            while cur.next != head:
                cur = cur.next
            cur.next = new_node
            new_node.next = head
            head = new_node
        else:
            # Locate the node before the point of insertion
            while cur.next != head and cur.next.val < new_node.val:
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node