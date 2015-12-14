# 8/21 - DFS, List
# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ConvertSortedListToBST(object):
    cur = None

    # Test on LeetCode - 268ms
    # Idea:
    #   DFS: use length and keep track of the next List Node
    def sorted_list_to_BST(self, head):
        """
        :type head: ListNode
        :rtype:
        """
        root = None
        if head is not None:
            node = head
            length = 0
            while node is not None:
                length += 1
                node = node.next
            ConvertSortedListToBST.cur = head
            root = self.build(0, length-1)
        return root

    def build(self, start, end):
        if start <= end:
            mid = (start + end) / 2
            lc = self.build(start, mid-1)
            node = ConvertSortedListToBST.cur
            root = TreeNode(node.val)
            ConvertSortedListToBST.cur = node.next
            rc = self.build(mid+1, end)
            root.left = lc
            root.right = rc
            return root
        else:
            return None

