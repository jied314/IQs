# 1/13 -
# Given a binary tree, return the postorder traversal of its nodes' values.
# For example:
#   Given binary tree {1,#,2,3},
#       1
#        \
#         2
#        /
#       3
#   return [3,2,1].
# Note: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import lib
import collections

class Solution(object):
    # Idea:
    #   use stack to track roots whose RHS hasn't been explored
    #   use pre to record last pop node, to help determine whether the root node has been fully explored
    def postorder_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret, roots = [], []
        node = root
        while node is not None or roots:
            if node is not None:
                roots.append(node)
                node = node.left
            else:
                top = roots[-1]
                if top.right is None:  # leaf node
                    pre = roots.pop()
                    ret.append(pre.val)
                    while roots and pre == roots[-1].right:
                        pre = roots.pop()
                        ret.append(pre.val)
                else:  # expand the RHS
                    node = top.right
        return ret

    # Notice postorder is a reverse of inorder.
    # post - Left -> Right -> Root
    # pre' - Root -> Right -> Left
    # So do preoder traversal, but visit right then left.
    def postorder_traversal_reverse(self, root):
        if root is None:
            return []
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            ret.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)  # make sure visit right first
        ret.reverse()
        return ret

test = Solution()
ta = [1,2,3,4,5,6,7]
tree = lib.build_tree(ta)
print test.postorder_traversal(tree)
print test.postorder_traversal_reverse(tree)