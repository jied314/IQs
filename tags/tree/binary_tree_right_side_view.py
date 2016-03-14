# 8/20 - Tree, BFS, DFS
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 12/25 - Revisit
from collections import deque


class BinaryTreeRightSideView(object):
    # Test on LeetCode - 44ms
    def right_side_view(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        node = root
        self.visit(node, 1, result)
        return result

    def visit(self, node, level, result):
        if node is not None:
            if level > len(result):
                result.append(node.val)
            self.visit(node.right, level+1, result)
            self.visit(node.left, level+1, result)

    # Test on LC - 48ms, 75%
    # keep updating val (since traversal is left-> right)
    def right_side_view_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        self.helper(root, 1, ret)
        return ret

    def helper(self, node, level, ret):
        if node is None:
            return
        if level > len(ret):
            ret.append(node.val)
        else:
            ret[level-1] = node.val
        self.helper(node.left, level+1, ret)
        self.helper(node.right, level+1, ret)

    # Test on LC - 56ms, 27%
    # level-order-traversal(BFS) -> record the last node (rightmost)
    def right_side_view_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        ret = []
        while queue:
            ret.append(queue[-1].val)
            temp = deque()
            while queue:
                node = queue.popleft()
                if node.left is not None:
                    temp.append(node.left)
                if node.right is not None:
                    temp.append(node.right)
            queue = temp
        return ret