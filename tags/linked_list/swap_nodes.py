# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 7/5 - Linked List
# Given a linked list, swap every two adjacent nodes and return its head.
class SwapPairs:
    # @param {ListNode} head
    # @return {ListNode}

    # Error - forget update previous to latter
    def swap_pairs_error(self, head):
        if head and head.next:
            previous = head
            head = head.next
            while previous is not None and previous.next:
                cur = previous.next
                previous.next = cur.next
                cur.next = previous
                previous = previous.next
        self.traverse(head)
        return head

    def swap_pairs_nice(self, head):
        pre = ListNode(0)
        pre.next = head
        cur = head
        head = pre
        while cur and cur.next:
            pre.next = cur.next
            cur.next = pre.next.next
            pre.next.next = cur
            pre = cur
            cur = cur.next
        return head.next

    def traverse(self, node):
        while node is not None:
            print node.val
            node = node.next

    def swap_pairs_recursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        next = head.next.next
        new_head = head.next
        new_head.next = head
        head.next = self.swap_pairs_recursive(next)
        return new_head


def main():
    test = SwapPairs()
    head = ListNode(2)
    one = ListNode(1)
    three = ListNode(3)
    four = ListNode(4)
    head.next = one
    one.next = three
    three.next = four
    print test.swap_pairs(head)


if __name__ == '__main__':
    main()
