# 10/25 - LL, Math
# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order
# and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

import lib

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class AddTwoNumbers(object):
    # Test on LeetCode - 132ms
    # Idea:
    #   easy logic, but need to handle special cases.
    #   1. addition - carry value
    #   2. l1 is None or l2 is None
    #   if either l1 is None or l2 is None, assign carry value to it. remember to clear carry.
    def add_two_numbers_dj(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l2
        dummy_head = ListNode(-1)
        node = dummy_head
        carry = 0
        while l1 is not None or l2 is not None:
            carry, node_val = divmod(l1.val + l2.val + carry, 10)  # add carry
            node.next = ListNode(node_val)
            node = node.next
            l1, l2 = l1.next, l2.next
            # special cases - if l1 or l2 is None
            if l1 is None and l2 is not None:
                l1 = ListNode(carry)
                carry = 0
            elif l2 is None and l1 is not None:
                l2 = ListNode(carry)
                carry = 0
        if carry > 0:
            node.next = ListNode(carry)
        return dummy_head.next

    # similar ideas. instead of use carry, use sum.
    # add l1.val and l2.val incrementally, and keep carry value in sum.
    # avoid testing whether l1 is None or l2 is None in the beginning.
    def add_two_numbers_nice(self, l1, l2):
        dummy_head = ListNode(-1)
        node = dummy_head
        sum = 0
        while l1 is not None or l2 is not None:
            sum /= 10
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            node.next = ListNode(sum % 10)
            node = node.next
        if sum / 10 == 1:
            node.next = ListNode(1)
        return dummy_head.next



def main():
    test = AddTwoNumbers()
    l1 = lib.build_ll([6, 4, 3])
    l2 = lib.build_ll([4, 5, 6])
    l = test.add_two_numbers(l1, l2)
    print lib.traverse_ll(l)


if __name__ == "__main__":
    main()