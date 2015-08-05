# 8/4 - Tree, Stack
# Compare with Preorder & Inorder (See OneNone)
# Note: Iterative & one stack
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class PostorderTraversal:
    # @param {TreeNode} root
    # @return {integer[]}

    # Test on LeetCode - 52ms
    def postorder_traversal_recursive(self, root):
        order = []
        self.visit(root, order)
        return order

    def visit(self, node, order):
        if node is not None:
            self.visit(node.left, order)
            self.visit(node.right, order)
            order.append(node.val)

    # Test on LeetCode - 52ms
    # Two stacks - one record visited nodes, one record expanded parents
    # Time - O(N), Memory - O(N)
    def postorder_traversal_iterative(self, root):
        order = []
        if root is not None:
            visited = [root]
            parents = []
            while visited:
                top = visited[-1]
                if top.left is None and top.right is None:  # leaf node
                    order.append(top.val)
                    visited.pop()
                else:  # parent node
                    if parents and top == parents[-1]:
                        order.append(top.val)
                        parents.pop()
                    else:
                        parents.append(top)
                        if top.right is not None:
                            visited.append(top.right)
                        visited.append(top)
                        if top.left is not None:
                            visited.append(top.left)
        return order

    # Test on LeetCode - 44ms
    # Manipulate the output
    def postorder_traversal_iterative_one_stack(self, root):
        order = []
        if root is not None:
            visited = [root]
            while visited:
                node = visited.pop()
                order.insert(0, node.val)
                if node.left is not None:
                    visited.append(node.left)
                if node.right is not None:
                    visited.append(node.right)
        return order
