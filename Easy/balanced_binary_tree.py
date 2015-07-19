# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 7/15 - Tree, DFS
# Given a binary tree, determine if it is height-balanced.
#
# Similar to Maximum Depth Binary Tree, except that you need to track the balance info
# Basically have to calculate depth and balance info at the same time.
# Note:
#   use a global variable to track balance info (cannot do in Python)
#   instead of returning two values
#
# Test on LeetCode - 104ms
class BalancedBinaryTree:
    # @param {TreeNode} root
    # @return {boolean}
    def is_balanced(self, root):
        return self.check_balance(root)[0]

    def check_balance(self, node):
        if node:
            left_balance = self.check_balance(node.left)
            right_balance = self.check_balance(node.right)
            depth = 1 + max(left_balance[1], right_balance[1])
            if left_balance[0] and right_balance[0]:
                if abs(left_balance[1] - right_balance[1]) <= 1:
                    return [True, depth]
            return [False, depth]
        else:
            return [True, 0]


def main():
    test = BalancedBinaryTree()

    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    one.left = two
    one.right = three
    two.left = four
    two.right = five
    four.left = six
    print test.is_balanced(one)


if __name__ == '__main__':
    main()