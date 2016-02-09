import lib
class Solution(object):
    found = False

    # similar idea as validate bst
    # recursively checking predecessor < cur < successor
    def recover_tree_tle(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        Solution.found = False
        if root is None:
            return
        self.helper(root)

    def helper(self, node):
        if Solution.found:
            return
        left = node.left
        if left is not None:
            pre = left
            while pre.right is not None:
                pre = pre.right
            if pre.val > node.val:  # swapped
                temp = node.val
                node.val = pre.val
                pre.val = temp
                Solution.found = True
                return
            else:
                self.recover_tree_tle(left)

        if Solution.found:
            return
        right = node.right
        if right is not None:
            suc = right
            while suc.left is not None:
                suc = right.left
            if suc.val < node.val:
                temp = node.val
                node.val = suc.val
                suc.val = temp
                Solution.found = True
                return
            else:
                self.recover_tree_tle(right)

    # Test on LC 152ms, 54%
    # Adapted from https://leetcode.com/discuss/13034/no-fancy-algorithm-just-simple-and-powerful-order-traversal
    # in-order traversal, find the first and second elements that are not in order
    # e.g. 6, 3, 4, 5, 2
    #   compare each node with its next one, find out that 6 is the first element to swap because 6 > 3
    # and 2 is the second element to swap because 2 < 5.
    # Key Observations:
    #   1. the first element is always larger than its next one
    #   2. the second element is always smaller than its previous one.
    def recover_tree_dfs(self, root):
        self.last = None
        self.first = None
        self.second = None
        self.dfs(root)
        if self.first is not None and self.second is not None:
            self.first.val, self.second.val = self.second.val, self.first.val

    # recursively find the out-of-order pair
    def dfs(self, root):
        if root is None:
            return
        self.dfs(root.left)
        # start of finding the pair
        if self.last is not None:  # avoid None in the first comparison
            if root.val < self.last.val:  # out of order
                if self.first is None:  # first  has not been found, assign last to it (refer to 6 in the example above)
                    self.first = self.last
                if self.first is not None:  # first is found
                    self.second = root  # assign root to second (refer to 2 in the example above)
        self.last = root
        # end of finding the pair
        self.dfs(root.right)

test = Solution()
tree = lib.build_tree([2,3,1])
tl = []
test.recover_tree_dfs(tree)
