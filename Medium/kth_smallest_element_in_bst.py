# 8/5 - Tree, BS
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
# Note: You may assume k is always valid, 1 <= k <= BST total elements.
#
# Follow up:
#   What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
#   How would you optimize the kthSmallest routine?
# Hint:
#   Try to utilize the property of a BST.
#   What if you could modify the BST node's structure?
#   The optimal runtime complexity is O(height of BST).
# Solution:
#   add count field for TreeNode (left_count and right_count, so that insertion/delection only needs to update nodes
# along the path)
#   search: compare k with lc, lc+1, lc+1+rc to find search path
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.lc = 0
        self.rc = 0

    def set_lc(self, lc):
        self.lc = lc

    def set_rc(self, rc):
        self.rc = rc


class KthSmallestElementInBST:
    index = 0

    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kth_smallest_in_order(self, root, k):
        index = 0
        to_visit = []
        node = root
        while to_visit or node is not None:
            if node is not None:
                to_visit.append(node)
                node = node.left
            else:
                node = to_visit.pop()
                index += 1
                if index == k:
                    return node.val
                node = node.right

    # use index to record node number
    def kth_smallest_nice(self, root, k):
        self.index = 0
        return self.visit(root, k)

    def visit(self, node, k):
        if node is None:
            return -1
        x = self.visit(node.left, k)
        if self.index == k:
            return x
        self.index += 1
        if self.index == k:
            return node.val
        return self.visit(node.right, k)

    # count number of left/right child
    # slower - due to multiple counts
    def kth_smallest(self, root, k):
        num_l = self.count(root.left)
        if num_l > k:
            return self.kth_smallest(root.left, k)
        elif num_l + 1 < k:
            return self.kth_smallest(root.right, k-1-num_l)
        else:
            return root.val

    # count number of nodes in the tree starting with node (as root)
    def count(self, node):
        if node is None:
            return 0
        return 1 + self.count(node.left) + self.count(node.right)

    # new insertion function for BST
    def insert(self, root, node):
        if root is None:
            root = node
        else:
            cur = root
            while cur.left is not None and cur.right is not None:
                if cur.val < node.val:
                    cur.rc += 1
                    cur = cur.next
                else:
                    cur.lc += 1
                    cur = cur.right
            if cur.val < node.val:
                cur.rc += 1
                cur.right = node
            else:
                cur.lc += 1
                cur.left = node
        return root

def main():
    test = KthSmallestElementInBST()
    one = TreeNode(1)
    two = TreeNode(2)
    two.left = one
    print test.kth_smallest_nice(two, 1)


if __name__ == '__main__':
    main()
