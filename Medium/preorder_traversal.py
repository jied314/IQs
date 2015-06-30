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

    # Test on LeetCode - 60ms
    # slightly different from inorder_tracersal
    def preorder_traversal_morris(self, root):
        order = []
        node = root
        while node is not None:
            if node.left is None:
                order.append(node.val)
                node = node.right
            else:
                # find the preorder predecessor of node (rightmost node of the left subtree)
                pre = node.left
                while pre.right is not None and pre.right != node:
                    pre = pre.right
                if pre.right is None:  # not point to node
                    order.append(node.val)
                    pre.right = node
                    node = node.left
                else:  # already point to node
                    pre.right = None
                    node = node.right
        return order