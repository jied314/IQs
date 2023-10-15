# 7/31 - Tree
# Note:
#   Utilize BST property root.left.val < root.val < root.right.val
#
class LowestCommonAncestorInBST:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}

    # Test on LeetCode - 168ms
    def lowest_common_ancestor(self, root, p, q):
        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root

    # Test on LeetCode - 148ms
    def lowest_common_ancestor_short(self, root, p, q):
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]
        return root