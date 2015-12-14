# 7/30 - Linked List
# Given a sorted linked list, delete all duplicates such that each element appear only once.
# Compare with Removing duplicates for array:
#   1. array - use two pointers, cannot get rid of duplicates easily, need to manipulate indexes
#   2. ll - use one pointer, just do cur.next = cur.next.next to get rid of duplicates.
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

    # Test on LeetCode - 68ms
    def delete_duplicates_nice(self, head):
        if head is None:
            return head
        cur = head
        while cur.next is not None:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def main():
    test = RemoveDuplicatesFromSortedList()
    one = ListNode(1)
    one1 = ListNode(1)
    one.next = one1
    print test.delete_duplicates_nice(one)

if __name__ == '__main__':
    main()