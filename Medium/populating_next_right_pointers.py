# 6/29 - Tree, DFS
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
#
class PopulatingNextRightPointers:
    # @param root, a tree link node
    # @return nothing

    # Test on LeetCode - TLE
    def connect_tle(self, root):
        if root:
            root.next = None
            upper = [root]
            lower = []
            i = 0
            while upper[0].left is not None:
                node = upper.pop(0)
                node.left.next = node.right
                lower.append(node.left)
                lower.append(node.right)
                if node.next is None:  # the last node in current level
                    if lower[0].left is not None:
                        node.right.next = None
                        upper = lower
                        lower = []
                        i = 0
                else:
                    node.right.next = upper[0].left
                    i += 1

    # Test on LeetCode - 88ms
    # utilize the next attribute
    def connect(self, root):
        if root:
            root.next = None
            start = root.left
            node = root
            while start is not None:
                while node.next is not None:
                    node.left.next = node.right
                    node.right.next = node.next.left
                    node = node.next
                node.left.next = node.right
                node.right.next = None
                node = start
                start = start.left



