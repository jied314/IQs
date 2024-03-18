package Tree

import kotlin.math.abs
import kotlin.math.max

/**
 * Given a binary tree, determine if it is height-balanced.
 * The height of the two subtrees of every node never differs by more than 1
 *
 * Solutions:
 *   Bottom-up approach - check left & right, then check height balance
 *   O(N) Time Complexity & O(N) Space Complexity
 */

data class TreeInfo(val height: Int, val isBalanced: Boolean)
private fun isBalanced(root: TreeNode?): Boolean {
    return dfs(root).isBalanced
}

private fun dfs(root: TreeNode?): TreeInfo {
    if (root == null) return TreeInfo(0, true)
    val left = dfs(root.left)
    val right = dfs(root.right)
    val isBalanced: Boolean = left.isBalanced && right.isBalanced && abs(left.height - right.height) <= 1
    return TreeInfo(max(left.height, right.height)+1, isBalanced)
}

fun main() {
    val root = TreeNode(1)
    val node2 = TreeNode(2)
    val node3 = TreeNode(3)
    val node4 = TreeNode(4)
    val node5 = TreeNode(5)
    val node6 = TreeNode(6)
    val node7 = TreeNode(7)
    root.left = node2
    root.right = node3
    node2.left = node4
    node2.right = node5
    node4.left = node6
    node4.right = node7

    println(isBalanced(root))
}