# 7/2 - Tree, DFS
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# Note:
#   1. Recursive & Iterative
#   2. complete binary tree
class ConvertSortedArrayToBST:
    # @param {integer[]} nums
    # @return {TreeNode}
    # Test on LeetCode - 112ms
    # find the median - not a complete tree
    def sorted_array_to_bst_recursive(self, nums):
        root = None
        if nums:
            if len(nums) == 1:
                root = TreeNode(nums[0])
            else:
                mid = len(nums) / 2
                root = TreeNode(nums[mid])
                root.left = self.sorted_array_to_bst(nums[0:mid])
                root.right = self.sorted_array_to_bst(nums[mid+1: len(nums)])
        return root

    # Test on LeetCode - 108ms
    def sorted_array_to_bst_iterative(self, nums):
        root = None
        if nums:
            left_indexes = [0]
            right_indexes = [len(nums) - 1]
            root = TreeNode(0)
            nodes = [root]
            while nodes:
                node = nodes.pop()
                left = left_indexes.pop()
                right = right_indexes.pop()
                mid = left + (right - left)/2
                node.val = nums[mid]
                if left <= mid - 1:
                    node.left = TreeNode(0)
                    left_indexes.append(left)
                    right_indexes.append(mid-1)
                    nodes.append(node.left)
                if right >= mid + 1:
                    node.right = TreeNode(0)
                    right_indexes.append(right)
                    left_indexes.append(mid+1)
                    nodes.append(node.right)
        return root


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

