# 6/29 - Tree, HashTable, Stack
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class InorderTraversal:
    # @param {TreeNode} root
    # @return {integer[]}

    # Test on LeetCode - 56ms
    def inorder_traversal_recursive(self, root):
        order = []
        if root is not None:
            self.visit(root, order)
        return order

    def visit(self, node, order):
        if node.left is not None:
            self.visit(node.left, order)
        order.append(node.val)
        if node.right is not None:
            self.visit(node.right, order)

    # Test on LeetCode - 52ms
    # Two stacks - one record visited nodes, one record expanded parents
    # Time - O(N), Memory - O(N)
    def inorder_traversal_iterative(self, root):
        order = []
        if root is not None:
            visited = [root]
            parents = []
            while visited:
                top = visited.pop()
                if top.left is None and top.right is None:  # leaf node
                    order.append(top.val)
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

    # Test on LeetCode - 61ms
    # go left as much as possible, if end, move to right
    # Time - O(N), Memory - O(N)
    def inorder_traversal_one_stack(self, root):
        to_visit = []
        order = []
        node = root
        while to_visit or node is not None:
            if node is not None:
                to_visit.append(node)
                node = node.left
            else:
                node = to_visit.pop()
                order.append(node.val)
                node = node.right
        return order

    # Test on LeetCode - 56ms
    # Morris Traversal:
    #   1. Initialize current as root
    #   2. While current is not NULL
    #          If current does not have left child
    #              a) Print current’s data
    #              b) Go to the right, i.e., current = current->right
    #          Else
    #              a) Make current as right child of the rightmost node in current's left subtree
    #              b) Go to this left child, i.e., current = current->left
    # Memory O(1), Time O(NlgN)
    # Drawback - modify tree structure
    def inorder_traversal_morris(self, root):
        order = []
        node = root
        while node is not None:
            if node.left is None:
                order.append(node.val)
                node = node.right
            else:
                # find the inorder predecessor of node (rightmost node of the left subtree)
                pre = node.left
                while pre.right is not None and pre.right != node:
                    pre = pre.right
                if pre.right is None:  # not point to node
                    pre.right = node
                    node = node.left
                else:  # already point to node
                    pre.right = None
                    order.append(node.val)
                    node = node.right
        return order




