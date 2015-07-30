# 7/30 - Linked List
#
class RemoveDuplicatesFromSortedList:
    # @param {ListNode} head
    # @return {ListNode}
    # Test on LeetCode - 88ms
    def delete_duplicates(self, head):
        node = head
        start = node
        while node is not None and node.next is not None:
            if node.val != node.next.val:
                if start != node:
                    start.next = node.next
                start = node.next
            node = node.next
        if start != node:
            start.next = node.next
        return head

    def delete_duplicates_nice(self, head):
        if head is None:
            return head
        cur = head
        while cur.next is not None:
            if cur.val == cur.next.val:
                cur.next == cur.next.next
            else:
                cur = cur.next
        return head