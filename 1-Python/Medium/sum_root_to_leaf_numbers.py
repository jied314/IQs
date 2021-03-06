# 7/30 - Tree, DFS
# Note:
#   no necessarily need to change node values (due to recursion)
class SumRootToLeafNumbers:
    # @param {TreeNode} root
    # @return {integer}
    # Test on LeetCode - 44ms
    def sum_numbers(self, root):
        return self.traverse_sum(root, 0, 0)

    def traverse_sum(self, node, parent_val, sum_val):
        if node is not None:
            node.val += parent_val * 10
            if node.left is None and node.right is None:  # leaf node
                return sum_val + node.val
            else:
                return self.traverse_sum(node.left, node.val, sum_val) + self.traverse_sum(node.right, node.val, sum_val)
        else:
            return 0

    # Test on LeetCode - 52ms
    # pass values without changing node.val
    def sum_numbers_no_change(self, root):
        return self.traverse_sum_no_change(root, 0)

    def traverse_sum_no_change(self, node, parent_val):
        if node is not None:
            if node.left is None and node.right is None:  # leaf node
                return 10 * parent_val + node.val
            else:
                return self.traverse_sum_no_change(node.left, 10 * parent_val + node.val) + \
                       self.traverse_sum_no_change(node.right, 10 * parent_val + node.val)
        else:
            return 0

    # 12/25 - Revisit
    # Test on LeetCode - 44ms
    # DFS - only leaf nodes count
    # if leaf nodes, add to total_sum.
    total_sum = 0
    def sum_numbers_revisit(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root, 0)
        return self.total_sum

    def helper(self, node, sum):
        if node is None:
            return
        sum = sum * 10 + node.val
        if node.left is None and node.right is None:
            self.total_sum += sum
        self.helper(node.left, sum)
        self.helper(node.right, sum)