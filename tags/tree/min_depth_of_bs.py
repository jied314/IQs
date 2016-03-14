# Tree, BFS, DFS
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # Test on LC - 80ms, 15%
    # DFS - if one child is None, not reach the leaf node (both to be None)
    def min_depth_dfs(self, root):
        return self.dfs_depth(root)

    def dfs_depth(self, node):
        if node is None:
            return 0
        if node.left is None:
            return self.dfs_depth(node.right) + 1
        if node.right is None:
            return self.dfs_depth(node.left) + 1
        return 1 + min(self.dfs_depth(node.left), self.dfs_depth(node.right))

    # Test on LC - 80ms, 15%
    def min_depth_bfs(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        nodes = {root}
        depth = 1
        while nodes:
            temp = set()
            while nodes:
                node = nodes.pop()
                if self.is_leaf(node):
                    return depth
                if node.left is not None:
                    temp.add(node.left)
                if node.right is not None:
                    temp.add(node.right)
            nodes = temp
            depth += 1
        return depth

    def is_leaf(self, node):
        return node.left is None and node.right is None

