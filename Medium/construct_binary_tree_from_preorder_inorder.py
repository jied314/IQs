# 10/10 - Tree, Array, DFS (M)
# Given preorder and inorder traversal of a tree, construct the binary tree.
# Note: You may assume that duplicates do not exist in the tree.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # Idea:
    #   root is stored at the beginning of preorder
    #   find the index of root in inorder, then left-side and right-side are the left and right child
    # Note:
    #   Exceed Memory Limit -> pass  preorder and inorder in the recursion
    #   use array index instead of passing arrays around
    def build_tree_recursive(self, preorder, inorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder is None:
            return None
        # return self.build_update_array(preorder, inorder)
        length = len(inorder)
        return self.build_update_array_index(preorder, inorder, 0, 0, length)

    # Test on LeetCode - Memory Limit Exceeded
    # Exceed Memory Limit -> pass inorder and postorder in the recursion
    def build_update_array_mle(self, preorder, inorder):
        length = len(inorder)
        if length == 0:
            return None
        root_val = preorder[0]
        root_index_inorder = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.build_update_array_mle(preorder[1:root_index_inorder+1], inorder[0:root_index_inorder])
        root.right = self.build_update_array_mle(preorder[root_index_inorder+1:length], inorder[root_index_inorder+1:length])
        return root

    # Test on LeetCode - 148ms
    # Pass array index instead of arrays
    def build_update_array_index(self, preorder, inorder, pre_s, in_s, length):
        if length <= 0:
            return None
        root_val = preorder[pre_s]
        root_index_inorder = inorder.index(root_val)
        root = TreeNode(root_val)
        left_length = root_index_inorder - in_s
        right_length = length - left_length - 1
        root.left = self.build_update_array_index(preorder, inorder, pre_s+1, in_s, left_length)
        root.right = self.build_update_array_index(preorder, inorder, pre_s+left_length+1, root_index_inorder+1, right_length)
        return root


def main():
    test = Solution()
    r1 = test.build_tree_recursive([1], [1])
    r2 = test.build_tree_recursive([1, 2, 3], [2, 1, 3])
    r3 = test.build_tree_recursive([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7])
    print 1

if __name__ == '__main__':
    main()

