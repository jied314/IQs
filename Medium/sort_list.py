# 8/2 - LL, Sort
# Sort a linked list in O(n log n) time using constant space complexity.
# Idea - modify Merge Sort
#   O(nlgn) Time Complexity with O(1) Memory Complexity, also stable performance.
#   Array Merge Sort uses O(n) memory in merge step, while for LL no need. (manipulate pointers)
#   1. multiple scan, each time solve 2 ** i nodes
#   2. sort while scanning - sort first two, next two, then merge; repeat until reach the end (no multiple scan, but
#      needs O(n) memory.
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Test on LeetCode - 448ms
class SortList:
    # @param {ListNode} head
    # @return {ListNode}
    def sort_list(self, head):
        node = head
        length = 0
        while node:
            length += 1
            node = node.next

        dummy_head = ListNode(0)
        dummy_head.next = head
        unit_size = 1

        # each loop, sort and merge sublists
        while unit_size < length:
            index = 0
            node = dummy_head.next
            tail = dummy_head
            while index < length:
                # find size_a and size_b
                size_a = min(length - index, unit_size)
                size_b = min(length - index - size_a, unit_size)

                # find b and new start, init end of each unit as None
                a = node
                b = None
                if size_b > 0:
                    for i in range(0, size_a-1):
                        node = node.next
                    b = node.next
                    node.next = None
                    node = b
                    for i in range(0, size_b-1):
                        node = node.next
                    temp = node.next
                    node.next = None
                    node = temp  # new start

                # merge and find tail
                new_node = tail
                while a is not None and b is not None:
                    if a.val < b.val:
                        new_node.next = a
                        a = a.next
                    else:
                        new_node.next = b
                        b = b.next
                    new_node = new_node.next
                if a is not None:
                    new_node.next = a
                    while a.next is not None:
                        a = a.next
                    tail = a
                else:
                    new_node.next = b
                    while b.next is not None:
                        b = b.next
                    tail = b
                index += size_a + size_b
                self.traverse(dummy_head.next)
            unit_size <<= 1
        return dummy_head.next

    def traverse(self, head):
        result = []
        while head is not None:
            result.append(head.val)
            head = head.next
        print result


def main():
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    three.next = four
    four.next = one
    l = three
    test = SortList()
    test.sort_list(l)

if __name__ == '__main__':
    main()

        