# 10/7 - LL, Two Pointers
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than
# or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
# For example,
#   Given 1->4->3->2->5->2 and x = 3, return 1->2->2->4->3->5.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class PartitionList(object):
    # Test on LeetCode - 60ms
    # Idea:
    #   keep track of end of smaller, and start of larger or equal
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy_head = ListNode(0)
        dummy_head.next = head
        end_s = dummy_head
        start_g = None
        node = dummy_head
        while node.next is not None:
            cur = node.next
            if start_g is None:  # not found node greater or equal to x
                if cur.val >= x:
                    start_g = cur
                else:
                    end_s = cur
            else:  # found start_g
                if cur.val < x:  # need to move node before start_g
                    node.next = cur.next
                    end_s.next = cur
                    cur.next = start_g
                    end_s = cur
                    continue
            node = node.next
        return dummy_head.next

    # Test on LeetCode - 52ms
    # Idea:
    #   still two pointers, but simpler code
    #   just concatenate two lists together
    def partition_nice(self, head, x):
        head1 = ListNode(0)  # store nodes smaller than x
        head2 = ListNode(0)  # store nodes greater or equal to x
        p1, p2 = head1, head2
        while head is not None:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p2.next = None
        p1.next = head2.next
        return head1.next
