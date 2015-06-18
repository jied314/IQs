# Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
# (ie, from left to right, level by level from leaf to root).
# can use list slice or reverse list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        if root is None:
            return []
        else:
            return self.singleLevelOrder([root])

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
            nodes[0:0] = self.singleLevelOrder(children)
        else:
            nodes = []
        return nodes

