# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedListIntersection:
    # @param two ListNodes
    # @return the intersected ListNode
    # Test on LeetCode - 809ms, memory O(n)
    def get_intersection_node(self, headA, headB):
        visited = set()
        nodeA = headA
        nodeB = headB
        while nodeA is not None or nodeB is not None:
            if nodeA:
                if nodeA in visited:
                    return nodeA
                else:
                    visited.add(nodeA)
                    nodeA = nodeA.next
            if nodeB:
                if nodeB in visited:
                    return nodeB
                else:
                    visited.add(nodeB)
                    nodeB = nodeB.next
        return None

    # Test on LeetCode - 660ms, memory O(1)
    def get_intersection_node_1(self, headA, headB):
        nodeA = headA
        nodeB = headB
        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA is not None else headB
            nodeB = nodeB.next if nodeB is not None else headA
        return nodeA

    # Test on LC - 360ms, 85%
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # calculate length
        l1, l2 = 0, 0
        n1, n2 = headA, headB
        while n1 is not None:
            l1 += 1
            n1 = n1.next
        while n2 is not None:
            l2 += 1
            n2 = n2.next
        # make sure l1 is longer
        n1, n2 = headA, headB
        if l1 < l2:
            l1, l2 = l2, l1
            n1, n2 = headB, headA
        # reposition n1
        diff = l1 - l2
        for i in range(0, diff):
            n1 = n1.next
        # move in parallel
        while n1 is not None:
            if n1 == n2:
                return n1
            n1 = n1.next
            n2 = n2.next
        return None

one = ListNode(1)
test = LinkedListIntersection()
test.getIntersectionNode(one, None)
