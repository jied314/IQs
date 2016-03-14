# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    # BFS traversal - top to bottom
    def level_order(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ret = []
        queue = deque()
        queue.append(root)

        while queue:
            temp = deque()
            level = []
            while queue:
                node = queue.popleft()
                level.append(node.val)
                if node.left is not None:
                    temp.append(node.left)
                if node.right is not None:
                    temp.append(node.right)
            queue = temp
            ret.append(level)
        return ret

    # use DFS to traverse, but not actually level order
    def dfs(self, root):
        result = []
        if root is not None:
            self.traverse(root, 0, result)
        return result

    # use DFS
    def traverse(self, node, level, visited):
        if node is not None:
            if len(visited) == level:
                visited.insert(level, [])
            visited[level].append(node.val)
            if node.left is not None:
                self.traverse(node.left, level + 1, visited)
            if node.right is not None:
                self.traverse(node.right, level + 1, visited)




