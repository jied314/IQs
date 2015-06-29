# 6/29 - Tree, Stack
#
# Definition for a binary tree node.
# class TreeNode:
# def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class PreorderTraversal:
    # @param {TreeNode} root
    # @return {integer[]}
    # Test on LeetCode - 44ms
    def preorder_traversal_recursive(self, root):
        order = []
        self.visit(root, order)
        return order

    def visit(self, node, order):
        if node:
            order.append(node.val)
            self.visit(node.left, order)
            self.visit(node.right, order)

    # Test on LeetCode - 48ms
    # Note - exhaust the left child before visiting the right child
    def preorder_traversal_iterative(self, root):
        order = []
        if root:
            visit = [root]
            while visit:
                node = visit.pop(0)
                order.append(node.val)
                if node.right is not None:
                    visit.insert(0, node.right)
                if node.left is not None:
                    visit.insert(0, node.left)
        return order

    # Test on LeetCode - 67ms, using stack
    def preorder_traversal_iterative_stack(self, root):
        order = []
        if root:
            visit = [root]
            while visit:
                node = visit.pop()
                order.append(node.val)
                if node.right is not None:
                    visit.append(node.right)
                if node.left is not None:
                    visit.append(node.left)
        return order
