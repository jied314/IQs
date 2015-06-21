# Linked List, Two Pointers - Remove Nth Node From List End
# Note - try solving it in on pass:
#   1. use recursive
#   2. use two pointers
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class RemoveNthNodeFromListEnd:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    # Test on LeetCode - 52ms
    def remove_nth_from_end(self, head, n):
        if n == self.place_to_end(head, None, n):
            head = head.next
        return head
        
    def place_to_end(self, node, previous, n):
        if node.next is None:
            place = 1
        else:
            place = 1 + self.place_to_end(node.next, node, n)
        if place == n:
            if previous is not None:  # node is not head
                previous.next = node.next
        return place

    # Test on LeetCode - 52ms
    def remove_nth_from_end_two_pointers(self, head, n):
        previous = head
        end = head
        i = 1
        while i < n:  # make sure n distance
            end = end.next
            i += 1
        if end.next is None:
            head = head.next
        else:
            end = end.next
            while end.next is not None:  # shift together
                previous = previous.next
                end = end.next
            previous.next = previous.next.next
        return head



def main():
    test = RemoveNthNodeFromListEnd()
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)
    one.next = two
    two.next = three
    three.next = four
    four.next = five
    print test.remove_nth_from_end(one, 5).val
    print test.remove_nth_from_end_two_pointers(one, 5).val

if __name__ == '__main__':
    main()