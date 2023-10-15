# Given a complete binary tree, count the number of nodes.
# Utilize the attribute of complete binary tree. Need to be efficient!
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CountCompleteBinaryTree:
    # @param {TreeNode} root
    # @return {integer}
    # 1/2 - Revisit
    # Test on LeetCode - 180ms
    # Idea:
    #   check if full, else T(N) = T(N/2) * 2
    #   Tme Complexity - O(N)
    def count_nodes_revisit(self, root):
        if root is None:
            return 0
        left_height = self.get_left_height(root)
        right_height = self.get_right_height(root)
        if left_height == right_height:  # every level is full
            return (1 << (left_height + 1)) - 1
        else:
            return 1 + self.count_nodes_revisit(root.left) + self.count_nodes_revisit(root.right)

    def get_left_height(self, node):
        left_heigth = 0
        while node.left is not None:
            node = node.left
            left_heigth += 1
        return left_heigth

    def get_right_height(self, node):
        right_heigth = 0
        while node.right is not None:
            node = node.right
            right_heigth += 1
        return right_heigth

    # Test on LeetCode - 324ms
    # Time Complexity - O(lgn * lgn)
    # Idea:
    #   if left_height == right_height, left if full
    #   else, right is full
    def count_nodes_efficient(self, root):
        if root is None:
            return 0
        hl = self.height(root.left)
        hr = self.height(root.right)
        if hl == hr:  # the last node on the right subtree
            return 2 ** hl + self.count_nodes_efficient(root.right)
        else:  # the last node on the left subtree
            return 2 ** hr + self.count_nodes_efficient(root.left)

    def height(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    # Test on LeetCode - 328ms
    def count_nodes_iterative(self, root):
        if root is None:
            return 0
        count = 0
        while root:
            hl = self.height(root.left)
            hr = self.height(root.right)
            if hl == hr:
                count += 2 ** hl
                root = root.right
            else:
                count += 2 ** hr
                root = root.left
        return count


def main():
    test = CountCompleteBinaryTree()
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
    # three.left = six
    print test.count_nodes_iterative(one)


if __name__ == '__main__':
    main()
