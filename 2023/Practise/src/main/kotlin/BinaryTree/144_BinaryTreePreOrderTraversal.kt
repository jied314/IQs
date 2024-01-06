package BinaryTree

/**
 * Given the root of a binary tree, return the preorder traversal of its nodes' values.
 *
 * Example:
 *  Input: root = [1,null,2,3]
 *  Output: [1,2,3]
 *
 * Solutions:
 * 1. Use DFS Recursion - rely on stack provided by the system
 *   O(N) Time Complexity, O(LogN) Average Space Complexity & O(N) Worst Space Complexity
 *
 * 2. Use while loop & stack to mimic recursion
 *   O(N) Time Complexity & O(N) Space Complexity
 */

// Definition for a binary tree node
class TreeNode(var num: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

private fun preorderTraversalRecursively(root: TreeNode?): List<Int> {
    return root?.let {
        val result = mutableListOf<Int>()
        preorderTraversalRecursively(root, result)
        result
    } ?: emptyList()
}

private fun preorderTraversalRecursively(root: TreeNode, result: MutableList<Int>) {
    result.add(root.num)
    root.left?.let { preorderTraversalRecursively(it, result) }
    root.right?.let { preorderTraversalRecursively(it, result) }
}

private fun preorderTraversalIteratively(root: TreeNode?): List<Int> {
    if (root == null) return emptyList()

    val traversal = mutableListOf<Int>()
    val stack = ArrayDeque<TreeNode>()
    stack.add(root)
    while (stack.isNotEmpty()) {
        val current = stack.removeLast()
        traversal.add(current.num)
        if (current.right != null) stack.add(current.right!!)
        if (current.left != null) stack.add(current.left!!)
    }
    return traversal
}

fun main() {
    val oneNode = TreeNode(1)
    val twoNode = TreeNode(2)
    val threeNode = TreeNode(3)
    val fourNode = TreeNode(4)
    val fiveNode = TreeNode(5)
    val sixNode = TreeNode(6)
    twoNode.left = oneNode
    twoNode.right = threeNode
    fourNode.left = twoNode
    fourNode.right = sixNode
    sixNode.left = fiveNode

    println(preorderTraversalRecursively(fourNode))
    println(preorderTraversalIteratively(fourNode))
}


