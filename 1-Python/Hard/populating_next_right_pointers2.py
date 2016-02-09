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

import collections
class PopulatingNextRightPointers2:
    # @param root, a tree link node
    # @return nothing

    # Same solution PopulatingNextRightPointers
    # Use None as level separator
    # Time Complexity - O(N), Space Complexity - O(1)
    def connect_queue(self, root):
        if root is None:
            return

        nodes = collections.deque()
        nodes.append(root)
        nodes.append(None)
        while len(nodes) > 1:
            node = nodes.popleft()
            if node is None:
                nodes.append(None)
            else:
                top = nodes.popleft()
                node.next = top
                nodes.appendleft(top)
                if node.left is not None:
                    nodes.append(node.left)
                if node.right is not None:
                    nodes.append(node.right)

    # Space Complexity - O(N)
    # Test on LC - 96ms, 92%
    def connect_nice(self, root):
        head = None  # head of the next level
        pre = None  # the leading node on the next level
        cur = root
        # based on level-order traversal
        while cur is not None:
            while cur is not None:
                # left child
                if cur.left is not None:
                    if pre is not None:
                        pre.next = cur.left
                    else:
                        head = cur.left
                    pre = cur.left
                # right child
                if cur.right is not None:
                    if pre is not None:
                        pre.next = cur.right
                    else:
                        head = cur.right
                    pre = cur.right

                # move to next node
                cur = cur.next

            # init value for the next level
            cur = head
            head = None
            pre = None
