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

class UniqueBinarySearchTree:
    # @param {integer} n
    # @return {TreeNode[]}

    # Test on LeetCode - 696ms
    def generate_trees_dj(self, n):
        tree_structures = []
        tree_structures.append([[]])
        tree_structures.append([TreeNode(1)])
        tree_structures.append(self.two_node_trees(1, 2))
        for i in range(3, n + 1):
            trees = []
            for j in range(1, i + 1):
                root = TreeNode(j)
                left = j - 1
                right = i - j
                left_children = None
                right_children = None
                if left > 0:
                    left_children = self.search_tree_structure(tree_structures, left, 1)
                if right > 0:
                    right_children = self.search_tree_structure(tree_structures, right, j + 1)

                if left_children:
                    for left_child in left_children:
                        if right_children:
                            for right_child in right_children:
                                new_root = deepcopy(root)
                                new_root.left = deepcopy(left_child)
                                new_root.right = deepcopy(right_child)
                                trees.append(new_root)
                        else:
                            new_root = deepcopy(root)
                            new_root.left = deepcopy(left_child)
                            trees.append(new_root)
                else:
                    for right_child in right_children:
                        new_root = deepcopy(root)
                        new_root.right = deepcopy(right_child)
                        trees.append(new_root)
            tree_structures.append(trees)
        return tree_structures[n]

    # note: num1 < nums2
    def two_node_trees(self, num1, num2):
        trees = []
        one = TreeNode(num1)
        two = TreeNode(num2)
        one.right = two
        trees.append(one)
        one = TreeNode(num1)
        two = TreeNode(num2)
        two.left = one
        trees.append(two)
        return trees

    # note: start is the desired range beginning
    def search_tree_structure(self, tree_structures, num_nodes, start):
        trees = deepcopy(tree_structures[num_nodes])
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


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def main():
    test = UniqueBinarySearchTree()
    print test.generate_trees(5)


if __name__ == '__main__':
    main()
