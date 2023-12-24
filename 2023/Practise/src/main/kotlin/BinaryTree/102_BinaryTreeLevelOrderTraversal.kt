package BinaryTree

/**
 * Given the root of a binary tree, return the level order traversal of its nodes' values.
 * (i.e., from left to right, level by level).
 *
 * Solutions:
 * 1. BFS with queue
 *   O(N) Time Complexity & O(N) Space Complexity
 *
 * 2. DFS with recursion
 *   O(N) Time Complexity & O(N) Space Complexity
 */

fun levelOrderBFS(root: TreeNode?): List<List<Int>> {
    val traversal = mutableListOf<List<Int>>()
    if (root == null) return traversal

    var queue = ArrayDeque<TreeNode>()
    queue.add(root)
    while (queue.isNotEmpty()) {
        // start a new level
        val levelTraversal = mutableListOf<Int>()

        // number of elements in the current level
        val size = queue.size
        for (i in 0 until size) {
            val node = queue.removeFirst()

            // fulfill the current level
            levelTraversal.add(node.num)

            // add child nodes of the current level in the queue for the next level
            if (node.left != null) queue.add(node.left!!)
            if (node.right != null) queue.add(node.right!!)
        }
        traversal.add(levelTraversal)
    }
    return traversal
}

private fun levelOrderRecursively(root: TreeNode?): List<List<Int>> {
    val traversal = mutableListOf<MutableList<Int>>()
    if (root == null) return traversal
    levelOrderRecursively(root, 1, traversal)
    return traversal
}

private fun levelOrderRecursively(root: TreeNode, level: Int, traversal: MutableList<MutableList<Int>>) {
    while (traversal.size < level) {
        traversal.add(mutableListOf<Int>())
    }
    traversal[level-1].add(root.num)
    if (root.left != null) levelOrderRecursively(root.left!!, level+1, traversal)
    if (root.right != null) levelOrderRecursively(root.right!!, level+1, traversal)
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

    println(levelOrderBFS(fourNode))
    println(levelOrderRecursively(fourNode))
}