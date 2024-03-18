package Tree.BST

import Tree.TreeNode

/**
 * Given the root of a binary tree, determine if it is a valid binary search tree (BST).
 *
 * A valid BST is defined as follows:
 *   The left subtree of a node contains only nodes with keys less than the node's key.
 *   The right subtree of a node contains only nodes with keys greater than the node's key.
 *   Both the left and right subtrees must also be binary search trees.
 *
 * Note: the tricky part is having range check for each subtree
 *
 * Solutions:
 * 1. Recursion with range check
 *    O(N) Time Complexity & O(N) Space Complexity
 *
 * 2. Convert #1 to iteration with 3 stacks to track value, low and high
 *    O(N) Time Complexity & O(N) Space Complexity
 *
 * 3. Recursive in-order traverse the tree - difficult to think of
 *    O(N) Time Complexity & O(N) Space Complexity
 *
 * 4. Iteratively in-order traverse the tree, and compare with the previous node.
 *    O(N) Time Complexity & O(N) Space Complexity
 */

private fun isValidBSTRecursiveWithRange(root: TreeNode?): Boolean {
    return isValidBSTRecursive(root, null, null)
}

private fun isValidBSTRecursive(root: TreeNode?, low: Int?, high: Int?): Boolean {
    // Empty trees are valid BSTs.
    if (root == null) return true

    // The current node's value must be between low and high.
    if ((low != null && root.num <= low) || (high != null && root.num >= high)) {
        return false
    }

    // The left and right subtree must also be valid.
    return isValidBSTRecursive(root.right, root.num, high) && isValidBSTRecursive(root.left, low, root.num)
}

private val nodeStack = ArrayDeque<TreeNode?>()
private val lowStack = ArrayDeque<Int?>()
private val highStack = ArrayDeque<Int?>()

private fun updateStacks(node: TreeNode?, low: Int?, high: Int?) {
    nodeStack.add(node)
    lowStack.add(low)
    highStack.add(high)
}
private fun isValidBSTIterativeWithRange(root: TreeNode?): Boolean {
    if (root == null) return false
    var low: Int? = null
    var high: Int? = null
    updateStacks(root, low, high)

    while (nodeStack.isNotEmpty()) {
        val node = nodeStack.removeLast()
        low = lowStack.removeLast()
        high = highStack.removeLast()

        if (node == null) continue
        if ((low != null && node.num <= low) || (high != null && node.num >= high)) {
            return false
        }

        updateStacks(node.right, node.num, high)
        updateStacks(node.left, low, node.num)
    }
    return true
}

private var prev: Int? = null

fun isValidBSTInOrderRecursive(root: TreeNode?): Boolean {
    prev = null
    return inorder(root)
}

private fun inorder(root: TreeNode?): Boolean {
    if (root == null) return true

    // dfs to leftmost
    if (!inorder(root.left)) return false

    // process the current
    if (prev != null && prev!! >= root.num) return false
    prev = root.num

    // check the right
    return inorder(root.right)
}

private fun isValidBSTInOrderIterative(root: TreeNode?): Boolean {
    var prev: Int? = null
    val stack = ArrayDeque<TreeNode>()
    var node = root
    while (stack.isNotEmpty() || node != null) {
        // dfs to leftmost
        while (node != null) {
            stack.add(node)
            node = node.left
        }

        // process the node
        node = stack.removeLast()
        // The next element in inorder traversal should be larger than the previous one
        if (prev != null && node.num <= prev) {
            return false
        }

        // check the right
        prev = node.num
        node = node.right
    }
    return true
}

fun main() {
    val root = TreeNode(5)
    val node4 = TreeNode(4)
    val node6 = TreeNode(6)
    val node3 = TreeNode(3)
    val node7 = TreeNode(7)
    root.left = node4
    root.right = node6
    node6.left = node3
    node6.right = node7

    println(isValidBSTRecursiveWithRange(root))
    println(isValidBSTIterativeWithRange(root))
    println(isValidBSTInOrderRecursive(root))
    println(isValidBSTInOrderIterative(root))
}