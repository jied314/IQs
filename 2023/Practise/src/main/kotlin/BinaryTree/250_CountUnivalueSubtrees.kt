package BinaryTree

/**
 * Given the root of a binary tree, return the number of uni-value subtrees.
 * A uni-value subtree means all nodes of the subtree have the same value.
 */

private var totalCount = 0
fun countUnivalSubtrees(root: TreeNode?): Int {
    if (root == null) return 0
    countUnivalSubtreesRecursively(root, root.num)
    return totalCount
}

fun countUnivalSubtreesRecursively(node: TreeNode?, targetValue: Int): Boolean {
    if (node == null) return true
    if (node.left == null && node.right == null && node.num == targetValue) {
        totalCount++
        return true
    }

    val isLeftUniVal = countUnivalSubtreesRecursively(node.left, targetValue)
    val isRightUniVal = countUnivalSubtreesRecursively(node.right, targetValue)
    if (isLeftUniVal && isRightUniVal && node.num == targetValue) {
        totalCount++
        return true
    }
    return false
}

fun main() {
    val root = TreeNode(5)
    val node1 = TreeNode(1)
    val node52 = TreeNode(5)
    val node53 = TreeNode(5)
    val node54 = TreeNode(5)
    val node55 = TreeNode(5)
    root.left = node1
    root.right = node52
    node1.left = node53
    node1.right = node54
    node52.right = node55

    println(countUnivalSubtrees(root))
}
