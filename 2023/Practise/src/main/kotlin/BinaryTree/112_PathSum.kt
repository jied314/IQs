package BinaryTree

/**
 * Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path
 * such that adding up all the values along the path equals targetSum.
 *
 * A leaf is a node with no children.
 *
 * Solutions:
 * 1. Recursion with Top-Down
 *
 * 2. Iteration
 */

private fun hasPathSumRecursively(root: TreeNode?, targetSum: Int): Boolean {
    if (root == null) return false
    if (root.left == null && root.right == null) return root.num == targetSum
    return hasPathSumRecursively(root.left, targetSum-root.num) ||
            hasPathSumRecursively(root.right, targetSum-root.num)
}

private fun hasPathSumIteratively(root: TreeNode?, targetSum: Int): Boolean {
    if (root == null) return false
    val nodeStack = ArrayDeque<TreeNode>()
    val sumStack = ArrayDeque<Int>()
    nodeStack.add(root)
    sumStack.add(root.num)
    while (nodeStack.isNotEmpty()) {
        val node = nodeStack.removeLast()
        val sum = sumStack.removeLast()
        if (node.left == null && node.right == null && sum == targetSum) {
            return true
        }
        if (node.right != null) {
            val newSum = sum + node.right!!.num
            nodeStack.add(node.right!!)
            sumStack.add(newSum)
        }
        if (node.left != null) {
            val newSum = sum + node.left!!.num
            nodeStack.add(node.left!!)
            sumStack.add(newSum)
        }
    }
    return false
}

fun main() {
    val node5 = TreeNode(5)
    val node4 = TreeNode(4)
    val node8 = TreeNode(8)
    val node11 = TreeNode(11)
    val node13 = TreeNode(13)
    val node42 = TreeNode(4)
    val node7 = TreeNode(7)
    val node2 = TreeNode(2)
    val node1 = TreeNode(1)
    node5.left = node4
    node5.right = node8
    node4.left = node11
    node8.left = node13
    node8.right = node42
    node11.left = node7
    node11.right = node2
    node8.left = node13
    node8.right = node42
    node42.right = node1

    println(hasPathSumIteratively(node5, 22))
}