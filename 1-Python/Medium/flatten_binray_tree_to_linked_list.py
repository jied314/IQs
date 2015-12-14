# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FlattenBinaryTreeToLinkedList:
    # Test on LeetCode - 76ms
    def flatten_iterative(self, root):
        if root is None:
            return
        # using Morris Traversal of BT
        node = root
        while node is not None:
            if node.left is not None:
                pre = node.left
                while pre.right is not None:
                    pre = pre.right
                pre.right = node.right
                node.right = node.left
                node.left = None
            node = node.right

    # static variable to store last-visited node
    last = None

    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    # Test on LeetCode - 76ms
    def flatten_in_place(self, root):
        self.traverse(root)

    def traverse(self, node):
        if node is not None:
            left = node.left
            right = node.right
            if FlattenBinaryTreeToLinkedList.last is not None:
                FlattenBinaryTreeToLinkedList.last.left = None
                FlattenBinaryTreeToLinkedList.last.right = node
            FlattenBinaryTreeToLinkedList.last = node
            self.traverse(left)
            self.traverse(right)

    # Test on LeetCode - 52ms
    # Use extra space to store the list
    def flatten_list(self, root):
        result = []
        self.traverse_list(root, result)
        for i in range(0, len(result)-1):
            result[i].left = None
            result[i].right = result[i+1]

    def traverse_list(self, node, lst):
        if node is not None:
            lst.append(node)
            self.traverse_list(node.left, lst)
            self.traverse(node.right, lst)