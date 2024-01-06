package BinaryTree

/**
 * Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
 *
 * According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
 * as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
 *
 * Solutions:
 *   Compared to 236, utilize the property of BST to speed up search:
 *   If p <= root <= q || q <= root <= p -> root is lca;
 *   else root > p || root > q -> search root.left;
 *   else search root.right.
 *
 * 1. Recursion - O(H) Time Complexity & O(H) Space Complexity
 * 2. Iteration (converted from recursion) - O(H) Time Complexity & O(1) Space Complexity
 */

private fun lowestCommonAncestorRecursive(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode? {
    if (root == null || p == null || q == null) return null

    if (root.num > p.num && root.num > q.num) return lowestCommonAncestorRecursive(root.left, p, q)
    else if (root.num < p.num && root.num < q.num) return lowestCommonAncestorRecursive(root.right, p, q)
    else {
        return root
    }
}

private fun lowestCommonAncestorIterative(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode? {
    if (root == null || p == null || q == null) return null

    var node = root
    while (node != null) {
        if (node.num > p.num && node.num > q.num) node = node.left
        else if (node.num < p.num && node.num < q.num) node = node.right
        else return node
    }
    return null
}