# 10/27 - Tree, DFS
# Given a binary tree, determine if it is a valid binary search tree (BST).
# Assume a BST is defined as follows:
#   The left subtree of a node contains only nodes with keys less than the node's key.
#   The right subtree of a node contains only nodes with keys greater than the node's key.
#   Both the left and right subtrees must also be binary search trees.


# Definition for a binary tree node.
# class TreeNode(object):
# def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class ValidateBinarySearchTree(object):
    # Test on LeetCode - 72ms
    # Idea:
    #   left_child < root < right_child && predecessor < root < successor
    # Time Complexity - O(N*lgN)
    def is_valid_BST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is not None:
            root_val = root.val
            if root.left is not None:
                if root.left.val >= root_val or self.get_left_neighbor(root).val >= root_val or \
                        not self.is_valid_BST(root.left):
                    return False
            if root.right is not None:
                if root.right.val <= root_val or self.get_right_neighbor(root).val <= root_val or \
                        not self.is_valid_BST(root.right):
                        return False
        return True

    # return the rightmost predecessor (predecessor always exists)
    def get_left_neighbor(self, node):
        ret = node.left
        while ret.right is not None:
            ret = ret.right
        return ret

    # return the leftmost successor (successor always exists)
    def get_right_neighbor(self, node):
        ret = node.right
        while ret.left is not None:
            ret = ret.left
        return ret

    # Time Complexity - O(N)
    # adaptation from in-order traversal
    # use last_val to record the predecessor's val (only checking one side is enough)
    def __init__(self):
        self.last_val = -1 * (1 << 31) - 1

    def is_valid_bst_in_order(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root)

    def dfs(self, root):
        if root is None:
            return True
        if not self.dfs(root.left):
            return False
        if self.last_val >= root.val:
            return False
        self.last_val = root.val
        return self.dfs(root.right)


