package BinaryTree

/**
 * Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
 *
 * Solutions:
 * 1. Recursion with Top-down
 *
 * 2. Iterative with BFS
 */

fun isSymmetricRecursively(root: TreeNode?): Boolean {
    if (root == null) return true
    return isSymmetricRecursively(root.left, root.right)
}

fun isSymmetricRecursively(left: TreeNode?, right: TreeNode?): Boolean {
    if (left == null && right == null) return true
    if (left == null || right == null || (left.num != right.num)) return false
    return isSymmetricRecursively(left.left, right.right) && isSymmetricRecursively(left.right, right.left)
}

fun isSymmetricIterativey(root: TreeNode?): Boolean {
    if (root == null) return true

    val queue = ArrayDeque<TreeNode?>()
    queue.add(root.left)
    queue.add(root.right)
    while (queue.isNotEmpty()) {
        val left = queue.removeFirst()
        val right = queue.removeFirst()
        if (left == null && right == null) continue
        if (left == null || right == null || left.num != right.num) return false
        queue.add(left.left)
        queue.add(right.right)
        queue.add(left.right)
        queue.add(right.left)
    }
    return true
}

fun main() {
    val oneNode = TreeNode(1)
    val twoNode = TreeNode(2)
    val threeNode = TreeNode(3)
    val fourNode = TreeNode(4)
    val twoNode2 = TreeNode(2)
    val threeNode2 = TreeNode(3)
    val fourNode2 = TreeNode(4)

    oneNode.left = twoNode
    twoNode.left = threeNode
    twoNode.right = fourNode

    oneNode.right = twoNode2
    twoNode2.left = fourNode2
    twoNode2.right = threeNode2

    println(isSymmetricRecursively(oneNode))
    println(isSymmetricIterativey(oneNode))
}