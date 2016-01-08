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
# 12/30 - Revisit
# choose whatever format you like -> can output all children
#
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Test on Leetcode - 192ms
class Codec:

    # BFS - flag whether reaching leaf
    def serialize_bfs(self, root):
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
                    if is_bottom and root.left is not None or root.right is not None:
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

    # DFS - need to clean if last row is all None
    def serialize_dfs(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        ret = [[str(root.val)]]
        self.visit(root, 1, ret)
        last_row = ret[-1]
        while last_row and last_row[-1] == 'None':
            last_row.pop()
        string = ""
        for row in ret:
            string += ','.join(row)
            string += ','
        return string[:-1]

    def visit(self, node, level, ret):
        if node is None:
            return
        if level == len(ret):
            ret.append([])
        if node.left is None:
            left_val = 'None'
        else:
            left_val = str(node.left.val)
        ret[level].append(left_val)
        if node.right is None:
            right_val = 'None'
        else:
            right_val = str(node.right.val)
        ret[level].append(right_val)
        self.visit(node.left, level+1, ret)
        self.visit(node.right, level+1, ret)

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

import Queue

class CodecRevisit:
    SEPARATOR = ','
    NN = 'X'

    # DFS preorder - print all nodes, and all its children if node is not None
    # e.g. 1 -> [1, X, X]
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        sl = []
        self.build_string(root, sl)
        return ''.join(sl)

    def build_string(self, node, sl):
        if node is None:
            sl.append(CodecRevisit.NN)
            sl.append(CodecRevisit.SEPARATOR)
        else:
            sl.append(str(node.val))
            sl.append(CodecRevisit.SEPARATOR)
            self.build_string(node.left, sl)
            self.build_string(node.right, sl)

    # Use Data Structure - Queue
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        queue = Queue.Queue()
        vals = data.split(CodecRevisit.SEPARATOR)
        for val in vals:
            queue.put(val)
        return self.build_tree(queue)

    def build_tree(self, queue):
        val = queue.get()
        if val == CodecRevisit.NN:
            return None
        node = TreeNode(int(val))
        node.left = self.build_tree(queue)
        node.right = self.build_tree(queue)
        return node



one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
one.left = two
one.right = three
three.left = four

one1 = TreeNode(1)

# Your Codec object will be instantiated and called as such:
codec = CodecRevisit()
serilization = codec.serialize(one)
print codec.serialize(codec.deserialize(serilization))