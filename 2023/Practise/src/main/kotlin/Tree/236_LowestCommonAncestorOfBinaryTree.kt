package Tree

import kotlin.collections.ArrayDeque
import kotlin.collections.contains
import kotlin.collections.set


/**
 * Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
 *
 * According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
 * as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
 *
 * Solutions:
 * 1. Recursion with DFS
 *  The first node in which subtree contains both nodes is the LCA.
 *  O(N) Time Complexity & O(N) Space Complexity
 *
 * 2. Iterative with parent pointers
 *  First traverse the tree to build the parent pointers map.
 *  Then build the ancestor hashset for p.
 *  Last find the first duplicate ancestor when iterating q's parents.
 *  O(N) Time Complexity & O(N) Space Complexity
 */

// limitation: does not traverse the whole tree because it returns early once having a value match
//             cannot be used when p or q does not exist in the tree.
private fun lowestCommonAncestorEasyRecursion(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode? {
    if (root == null || root == p || root == q) return root
    val left = lowestCommonAncestorEasyRecursion(root.left, p, q)
    val right = lowestCommonAncestorEasyRecursion(root.right, p, q)
    return if (left != null && right != null) root
    else left ?: right
}

private var lca: TreeNode? = null
private fun lowestCommonAncestorRecursively(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode? {
    dfs(root, p, q)
    return lca
}

// easy to read version with early return check
private fun dfs(root: TreeNode?, p: TreeNode?, q: TreeNode?): Boolean {
    if (root == null) return false
    if (lca != null) return true

    val left = dfs(root.left, p, q)
    val right = dfs(root.right, p, q)
    val mid = root.num == p!!.num || root.num == q!!.num
    if (((mid && left) || (mid && right) || (left && right)) && lca == null) lca = root
    return mid || left || right
}

private fun lowestCommonAncestorIteratively(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode? {
    if (root == null) return null

    // Stack for tree traversal
    val stack = ArrayDeque<TreeNode>()

    // HashMap for parent pointers
    val parent = mutableMapOf<TreeNode?, TreeNode?>()

    parent[root] = null
    stack.add(root)

    // Iterate until we find both the nodes p and q to build the parent hashmap
    while (!parent.containsKey(p) || !parent.containsKey(q)) {
        val node = stack.removeLast()

        // While traversing the tree, keep saving the parent pointers.
        if (node.left != null) {
            parent[node.left] = node
            stack.add(node.left!!)
        }
        if (node.right != null) {
            parent[node.right] = node
            stack.add(node.right!!)
        }
    }

    // Ancestors set for node p
    val ancestors = mutableSetOf<TreeNode>()

    // Process all ancestors for node p using parent pointers.
    var pAncestor = p
    while (pAncestor != null) {
        ancestors.add(pAncestor)
        pAncestor = parent[pAncestor]
    }

    // The first ancestor of q which appears in p's ancestor set is their lowest common ancestor
    var qAncestor = q
    while (!ancestors.contains(qAncestor)) qAncestor = parent[qAncestor]
    return qAncestor
}