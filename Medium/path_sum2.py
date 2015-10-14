# 10/13 - Tree, DFS (M)
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# Note: performance

import lib

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class PathSum2(object):
    paths = []
    path = []

    # recursively visit tree nodes
    # Note:
    #   use less expensive list copy by pushing and pop
    def path_sum2_recursive(self, root, sum):
        """
            :type root: TreeNode
            :type sum: int
            :rtype: List[List[int]]
            """
        PathSum2.paths = []
        PathSum2.path = []
        # self.visit_tle(root, sum, [])
        self.visit(root, sum)
        return PathSum2.paths

    # Test on LeetCode - TLE
    # making lists is expensive
    # also passing visited (a list) to each recursive call
    def visit_tle(self, node, sum, visited):
        if node is None:
            return
        left_sum = sum - node.val
        visited += [node]  # make a new list - expensive if tree is big
        if node.left is None and node.right is None:  # leaf node
            if left_sum == 0 and len(visited) > 0:  # equal to sum
                PathSum2.paths.append(visited)
        else:  # none left node
            self.visit_tle(node.left, left_sum, visited)
            self.visit_tle(node.right, left_sum, visited)
        visited.pop()

    # Test on LeetCode - 68ms
    # Idea:
    #   reduce making new lists
    #   only use one visited as a class variable
    # @param node: visiting node
    # @param sum: left path sum
    def visit(self, node, sum):
        if node is None:
            return
        left_sum = sum - node.val
        PathSum2.path.append(node.val)
        if node.left is None and node.right is None:  # leaf node
            if left_sum == 0 and len(PathSum2.path) > 0:  # equal to sum
                PathSum2.paths.append(list(PathSum2.path))
        else:  # none left node. no need to check left_sum == 0
            self.visit(node.left, left_sum)
            self.visit(node.right, left_sum)
        PathSum2.path.pop()  # important - reduce numbers of making new lists


def main():
    test = PathSum2()
    tree1 = lib.read_tree([-2, None, -3])
    tree2 = lib.read_tree([1, 2, 3])
    tree3 = lib.read_tree([1,-2,-3,1,3,-2,None,-1])
    print test.path_sum2_recursive(tree1, -5)
    print test.path_sum2_recursive(tree2, 4)
    print test.path_sum2_recursive(tree3, -1)


if __name__ == '__main__':
    main()
