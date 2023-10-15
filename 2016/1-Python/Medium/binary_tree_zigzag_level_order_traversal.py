# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import lib

class Solution(object):
    # Test on LeetCode - 44ms
    # Idea: BFS
    def zigzag_level_order_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ret = []
        reverse_flag = True
        parents = [root]
        while len(parents) > 0:
            ret.append([parent.val for parent in parents])
            children = []
            for i in range(len(parents)-1, -1, -1):
                parent = parents[i]
                left = parent.left
                right = parent.right
                if reverse_flag:  # need to traverse right to left
                    if right is not None:
                        children.append(right)
                    if left is not None:
                        children.append(left)
                else:  # need to traverse left to right
                    if left is not None:
                        children.append(left)
                    if right is not None:
                        children.append(right)
            reverse_flag = not reverse_flag
            parents = children
        return ret

    # Test on LeetCode - 48ms
    # Idea: DFS
    def zigzag_level_order_recursive(self, root):
        if root is None:
            return []
        ret = [[]]
        self.zigzag_visit(root, 0, ret)
        return ret

    def zigzag_visit(self, node, level, ret):
        if node is None:
            return
        while len(ret) <= level:
            ret.append([])
        if level & 1:  # add to the end
            ret[level].insert(0, node.val)
        else:  # add to the front
            ret[level].append(node.val)
        self.zigzag_visit(node.left, level + 1, ret)
        self.zigzag_visit(node.right, level + 1, ret)


def main():
    test = Solution()
    tree = lib.build_tree([1,2,3,4,None,None,5])
    print test.zigzag_level_order_iterative(tree)
    print test.zigzag_level_order_recursive(tree)


if __name__ == "__main__":
    main()