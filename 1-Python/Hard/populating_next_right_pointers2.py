# 8/20 - Tree, DFS
# Any binary tree?
#
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
#
class PopulatingNextRightPointers2:
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
    # utilize the next attribute - BFS
    def connect(self, root):
        if root:
            node = root
            # find the leftmost children
            start = node.left
            while start is None and node is not None:
                if node.left is None:
                    if node.right is None:
                        node = node.next
                    else:
                        start = node.right
                else:
                    start = node.left
            # assign next
            while start is not None:
                lc = start
                while node.next is not None:
                    if node.left is None or node.right is None:
                    else:
                        node.left.next = node.right.next

                    lc = node.left
                    rc = node.right
                    if lc is None and rc is None:
                        node = node.next
                    else:  # node has children

                        if lc is not None:
                            if rc is not None:
                                lc.next = rc




            while lc is not None:
                while node.next is not None:
                    if node.left is not None:
                        if node.right is not None:
                            node.left.next = node.right
                            node.right.next = node.next.left
                        else:
                            node.left.next = node.next.left
                    node = node.next
                node.left.next = node.right
                node.right.next = None
                node = lc
                lc = lc.left

    # Test on LeetCode - 92ms
    # utilize the next attribute - DFS
    def connect_recursive(self, root):
        self.visit(root)

    def visit(self, node):
        if node is not None and node.left is not None:
            node.left.next = node.right
            if node.next is not None:
                node.right.next = node.next.left
            self.visit(node.left)
            self.visit(node.right)

