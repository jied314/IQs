# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        if root is None:
            return []
        else:
            return self.singleLevelOrder([root])

    # recursion
    def singleLevelOrder(self, roots):        
        if roots:   
            nodes = [[]]     
            children = []
            for root in roots:
                if root is not None and root != '#':
                    nodes[0].append(root.val)
                    leftNode = root.left
                    rightNode = root.right
                    if leftNode is not None and leftNode != '#':
                        children.append(leftNode)
                    if rightNode is not None and rightNode != '#':
                        children.append(rightNode)
            nodes.extend(self.singleLevelOrder(children))
        else:
            nodes = []
        return nodes

    # use procedural
    def bfs(self, root):
        if root is None:
            return []
        nodes = []
        current_level = [root]
        children = []
        level = 0
        while True:
            nodes.insert(level, [x.val for x in current_level])
            for node in current_level:
                leftChild = node.left
                rightChild = node.right
                if leftChild is not None:
                    children.append(leftChild)
                if rightChild is not None:
                    children.append(rightChild)
            if children:
                current_level = children
                children = []
                level += 1
            else:
                break
        return nodes

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




