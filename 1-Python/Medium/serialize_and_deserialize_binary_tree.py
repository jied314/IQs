# 12/2 - Tree, Design
#
# Serialization is the process of converting a data structure or object into a sequence of bits so that
# it can be stored in a file or memory buffer, or transmitted across a network connection link to be
# reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree.
# There is no restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and this string can be
# deserialized to the original tree structure.
#
# For example, you may serialize the following tree
#
#   1
#  / \
# 2   3
#    / \
#   4   5
#
# as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree.
# You do not necessarily need to follow this format, so please be creative and come up with
# different approaches yourself.
#
# Note: Do not use class member/global/static variables to store states.
# Your serialize and deserialize algorithms should be stateless.
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Test on Leetcode - 192ms
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        ret = ""
        roots = [root]
        while len(roots) > 0:
            temp = []
            level_ret = ""
            is_bottom = True
            for root in roots:
                if root is not None:
                    level_ret += str(root.val) + ","
                    if root.left is not None or root.right is not None:
                        is_bottom = False
                    temp.append(root.left)
                    temp.append(root.right)
                else:
                    level_ret += "None,"
            if is_bottom:
                roots = []
            else:
                roots = temp
            ret += level_ret
        return ret[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        values = data.split(",")
        length = len(values)
        root = TreeNode(values[0])
        roots = [root]
        i = 1
        while len(roots) > 0 and i < length:
            temp = []
            for node in roots:
                if i < length and values[i] != "None":
                    left_child = TreeNode(values[i])
                    node.left = left_child
                    temp.append(left_child)
                i += 1
                if i < length and values[i] != "None":
                    right_child = TreeNode(values[i])
                    node.right = right_child
                    temp.append(right_child)
                i += 1
            roots = temp
        return root


one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
one.left = two
one.right = three
three.left = four
three.right = five

# Your Codec object will be instantiated and called as such:
codec = Codec()
serilization = codec.serialize(one)
print codec.serialize(codec.deserialize(serilization))