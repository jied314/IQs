# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        self.flip(root)
        return root

    def flip(self, node):
        if node:
            left = node.left
            self.flip(left)
            right = node.right
            self.flip(right)
            node.left = right
            node.right = left
