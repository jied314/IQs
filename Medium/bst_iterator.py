# 8/10 - Tree, Stack
# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
# Calling next() will return the next smallest number in the BST.
# Note:
#   next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Test on LeetCode - 112ms
# use Morris Traversal, traverse in next()
class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.top = root

    # O(1) time, O(1) memory
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.top is not None

    # O(1) memory, on average O(lgn) time - total O(nlgn) time complexity to traverse the whole tree
    # @return an integer, the next smallest number
    def next(self):
        node = self.top
        while node is not None:
            if node.left is None:
                result = node.val
                node = node.right
                break
            else:
                pre = node.left
                while pre.right is not None and pre.right is not node:
                    pre = pre.right
                if pre.right is None:
                    pre.right = node
                    node = node.left
                else:
                    result = node.val
                    pre.right = None
                    node = node.right
                    break
        self.top = node
        return result

# Test on LeetCode - 108ms
# Use stack (treat subtree the same as the whole tree)
class BSTIteratorStack:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.push_left(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0

    # @return an integer, the next smallest number
    def next(self):
        top = self.stack.pop()
        self.push_left(top.right)
        return top.val

    def push_left(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

# read tree's serialized interpretation
def read_tree(array):
    root = TreeNode(array[0])
    parents = [root]
    index = 1
    while index < len(array):
        children = []
        for node in parents:
            if node is not None:
                left = array[index]
                if left is not None:
                    left = TreeNode(left)
                node.left = left
                index += 1
                right = array[index]
                if right is not None:
                    right = TreeNode(right)
                node.right = right
                index += 1
                children.append(node.left)
                children.append(node.right)
        if index < len(array):
            parents = children
    tree = []
    traverse(root, tree)
    print tree
    return root

def traverse(root, result):
    node = root
    if node is not None:
        traverse(node.left, result)
        result.append(node.val)
        traverse(node.right, result)


def main():
    """one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)
    two.left = one
    two.right = three
    four.left = two
    four.right = six
    six.left = five
    six.right = seven
    test = BSTIterator(four)
    v = []
    while test.hasNext():
        v.append(test.next())
    print v"""
    root = read_tree([41,37,44,24,39,42,48,1,35,38,40,None,43,46,49,0,2,30,36,None,None,None,None,None,None,45,47,None,None,
                None,None,None,4,29,32,None,None,None,None,None,None,3,9,26,None,31,34,None,None,7,11,25,27,None,None,
                33,None,6,8,10,16,None,None,None,28,None,None,5,None,None,None,None,None,15,19,None,None,None,None,12,
                None,18,20,None,13,17,None,None,22,None,14,None,None,21,23])
    test = BSTIterator(root)
    v = []
    while test.hasNext():
        v.append(test.next())
    print v

if __name__ == '__main__':
    main()
