# 7/15 - Tree, DFS
# Given a binary tree, find its maximum depth.

class MaximumDepth:
    # @param {TreeNode} root
    # @return {integer}
    def max_depth(self, root):
        if root:
            return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
        else:
            return 0

