from copy import deepcopy


# 6/30 - Tree, DP
# Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
# Interesting Solutions:
#   1. O(1) DP:
#       The basic idea is that we can construct the result of n node tree just from the result of n-1 node tree.
#       Here's how we do it: only 2 conditions:
#           1) The nth node is the new root, so newroot->left = oldroot;
#           2) the nth node is not root, we traverse the old tree, every time the node in the old tree
#              has a right child, we can perform: old node->right = nth node, nth node ->left = right child;
#              and when we reach the end of the tree, don't forget we can also add the nth node here.
#       One thing to notice is that every time we push a TreeNode in our result, I push the clone version of the root,
#       and I recover what I do to the old node immediately. This is because you may use the old tree for several times.
#   2. DP:
#       Can be helpful since reuse the previous results.
#       However, problems are: deepcopy trees and adjust node val (which implicitly involves traverse the entire trees)
#   3. Recursive without DP (actually faster 96ms V.S. 600ms)
class UniqueBinarySearchTree:
    # @param {integer} n
    # @return {TreeNode[]}

    # Test on LeetCode - 580ms
    def generate_trees_dj(self, n):
        tree_structures = []
        tree_structures.append([None])
        for i in range(1, n + 1):
            trees = []
            for j in range(1, i + 1):
                left = j - 1
                right = i - j
                left_children = self.search_tree_structure(tree_structures, left, 1)
                right_children = self.search_tree_structure(tree_structures, right, j + 1)
                for left_child in left_children:
                    for right_child in right_children:
                        root = TreeNode(j)
                        root.left = deepcopy(left_child)
                        root.right = deepcopy(right_child)
                        trees.append(root)
            tree_structures.append(trees)
        return tree_structures[n]

    # note: start is the desired range beginning
    def search_tree_structure(self, tree_structures, num_nodes, start):
        trees = deepcopy(tree_structures[num_nodes])
        if start > 1:
            for tree in trees:
                self.visit(tree, start)
        return trees

    # visit each node and update values
    def visit(self, node, start):
        if node is not None:
            node.val = (start + node.val - 1)
            self.visit(node.left, start)
            self.visit(node.right, start)

    # Online Solution - 300ms
    def build(self, nodes):
        n = len(nodes)
        if n == 0:
            yield None
            return
        for i in range(n):
            root = nodes[i]
            for left in self.build(nodes[:i]):
                for right in self.build(nodes[i+1:]):
                    root.left, root.right = left, right
                    yield root

    # @return a list of tree node
    # utilize Python deepcopy and generator
    def generate_trees_pythonic(self, n):
        nodes = map(TreeNode, range(1, n + 1))
        return map(deepcopy, self.build(nodes))
    
    # Test on LeetCode - 96ms
    # problem - too deep recursion depth
    def generate_trees_recursive(self, n):
        return self.generate_trees(1, n)

    def generate_trees(self, start, end):
        trees = []
        if start == end:
            trees.append(TreeNode(start))
        elif start > end:
            trees.append(None)
        else:
            for i in range(start, end+1):
                left_children = self.generate_trees(start, i-1)
                right_children = self.generate_trees(i+1, end)
                for m in range(0, len(left_children)):
                    for n in range(0, len(right_children)):
                        root = TreeNode(i)
                        root.left = left_children[m]
                        root.right = right_children[n]
                        trees.append(root)
        return trees


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def main():
    test = UniqueBinarySearchTree()
    print test.generate_trees_dj(3)


if __name__ == '__main__':
    main()
