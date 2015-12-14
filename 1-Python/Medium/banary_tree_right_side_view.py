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