# 7/30 - Tree, DFS
#
class SameTree:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}

    # Test on LeetCode - 56ms
    # should be better since once detecting False, will stop comparing
    def is_same_tree(self, p, q):
        return self.compare(p, q, True)

    def compare(self, node1, node2, equal):
        if equal:
            if node1 is not None and node2 is not None:
                if node1.val == node2.val:
                    return self.compare(node1.left, node2.left, equal) and self.compare(node1.right, node2.right, equal)
            elif node1 is None and node2 is None:
                return True
        return False

    # Test on LeetCode - 40ms
    def is_same_tree_nice(self, p, q):
        if p is None or q is None:
            return p == q
        else:
            return p.val == q.val and self.is_same_tree_nice(p.left, q.left) and self.is_same_tree_nice(p.right, q.right)