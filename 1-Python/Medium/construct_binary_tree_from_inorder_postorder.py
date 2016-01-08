# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # Idea:
    #   root is stored at the end of postorder
    #   find the index of root in inorder, then left-side and right-side are the left and right child
    def build_tree_memory_recursive(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder is None:
            return None
        # return self.build_update_array_mle(inorder, postorder)
        length = len(inorder)
        return self.build_update_array_index(inorder, postorder, 0, 0, length)

    # Test on LeetCode - Memory Limit Exceeded
    # Exceed Memory Limit -> pass inorder and postorder in the recursion
    def build_update_array_mle(self, inorder, postorder):
        length = len(inorder)
        if length == 0:
            return None
        root_val = postorder[length - 1]
        root_index_inorder = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.build_update_array_mle(inorder[0:root_index_inorder], postorder[0:root_index_inorder])
        root.right = self.build_update_array_mle(inorder[root_index_inorder+1:length], postorder[root_index_inorder:length-1])
        return root

    # Test on LeetCode - 116ms
    # Pass in array index ranges, instead of arrays
    def build_update_array_index(self, inorder, postorder, in_s, post_s, length):
        if length <= 0:
            return None
        post_e = post_s + length - 1
        root_val = postorder[post_e]
        root_index_inorder = inorder.index(root_val)
        left_length = root_index_inorder - in_s
        right_length = length - 1 - left_length
        root = TreeNode(root_val)
        root.left = self.build_update_array_index(inorder, postorder, in_s, post_s, left_length)
        root.right = self.build_update_array_index(inorder, postorder, root_index_inorder+1, post_e-right_length, right_length)
        return root

    def build_tree_iterative(self, inorder, postorder):
        i, j, length = 0, 0, len(inorder)
        left, right, root, node = None, None, None, None
        node_stack = []
        while j < length:
            if inorder[i] == postorder[j]:  # same value. can be left or root (no RHS)
                val = inorder[i]
                if left is None:  # left
                    left = TreeNode(val)
                    i += 1
                    j += 1
                else:  # root
                    node = TreeNode(val)
                    node.left = left
                    i += 1
                    j += 1
                    left = None
                    node_stack.append(node)
            else:  # must be root with RHS
                if root is None:
                    node = TreeNode(inorder[i])
                    node.left = left
                    root = node
                    left = None
                else:
                    node = TreeNode(inorder[i])
                    root.right = node
                    node_stack.append(root)
                    root = None
                i += 1
                j += 1
        return left



def main():
    test = Solution()
    # r1 = test.build_tree_iterative([1], [1])
    r2 = test.build_tree_iterative([2, 1, 3], [2, 3, 1])
    r3 = test.build_tree_iterative([4, 2, 5, 1, 6, 3, 7], [4, 5, 2, 6, 7, 3, 1])
    print 1

if __name__ == '__main__':
    main()

