# Tag: Tree, Depth-First Search
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum_recursive(self, root, sum):
        """first check conditions, than traverse the subTree"""
        if root is None:
            return False
        #if root.val > sum: return False # value canbe negative
        if root.left is None and root.right is None:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    def hasPathSum_procedural(self, root, sum):
        result = False
        while root is not None:
            if root.left is None and root.right is None:
                return root.val == sum


