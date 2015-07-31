# 7/31 - Tree
# Note:
#   Binary Tree V.S. Binary Search Tree
#
class LowestCommonAncestorInBT:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}

    # Test on LeetCode - 172ms
    # Idea: search whether the subtree contains p or q
    def lowest_common_ancestor_normal(self, root, p, q):
        if root is None or root is p or root is q:
            return root
        left = self.lowest_common_ancestor_normal(root.left, p, q)
        right = self.lowest_common_ancestor_normal(root.right, p, q)
        if left is not None:
            if right is not None:
                return root
            else:
                return left
        else:
            return right
