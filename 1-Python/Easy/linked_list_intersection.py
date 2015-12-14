# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
