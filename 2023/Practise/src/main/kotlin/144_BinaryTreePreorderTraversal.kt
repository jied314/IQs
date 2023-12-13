/**
 * Given the root of a binary tree, return the preorder traversal of its nodes' values.
 *
 * Example:
 *  Input: root = [1,null,2,3]
 *  Output: [1,2,3]
 */

// Definition for a binary tree node
class TreeNode(val num: Int) {
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

    val result = mutableListOf<Int>()
    val nodeStack = ArrayDeque<TreeNode>()
    nodeStack.add(root)
    while (nodeStack.isNotEmpty()) {
        val node = nodeStack
    }
    return emptyList()
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

