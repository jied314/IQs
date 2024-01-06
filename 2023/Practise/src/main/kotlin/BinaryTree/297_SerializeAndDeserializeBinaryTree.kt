package BinaryTree

/**
 * Serialization is the process of converting a data structure or object into a sequence of bits so that
 * it can be stored in a file or memory buffer, or transmitted across a network connection link to be
 * reconstructed later in the same or another computer environment.
 *
 * Design an algorithm to serialize and deserialize a binary tree.
 * There is no restriction on how your serialization/deserialization algorithm should work.
 * You just need to ensure that a binary tree can be serialized to a string and this string
 * can be deserialized to the original tree structure.
 *
 * Clarification: The input/output format is the same as how LeetCode serializes a binary tree.
 * You do not necessarily need to follow this format, so please be creative and come up with
 * different approaches yourself.
 *
 * Solutions:
 * 1. BFS (Level-order traversal) with Queue - Correct but memory limit exceeded
 *    O(N) Time Complexity & O(N) Space Complexity
 *
 * 2. DFS (In-order traversal) with clever recursion - amazing!
 *    In-order traversal naturally provides links to build a tree top-down. (Root -> Left -> Right)
 *    Record children of leaf nodes as null for easy marking.
 *    O(N) Time Complexity & O(H) Space Complexity, O(N) Space Complexity for deserialization
 */

private const val NULL = "null"
private const val SEPARATOR = ", "

// Encodes a tree to a string.
private fun serializeBFS(root: TreeNode?): String {
    if (root == null) return ""

    val result = mutableListOf<String>()
    val queue = ArrayDeque<TreeNode?>()
    queue.add(root)
    while (queue.isNotEmpty()) {
        var hasNextLevel = false
        val size = queue.size
        for (i in 0 until size) {
            val node = queue.removeFirst()
            hasNextLevel = hasNextLevel || (node != null && (node.left != null || node.right != null))
            if (node != null) {
                result.add(node.num.toString())
                queue.add(node.left)
                queue.add(node.right)
            } else { // add in placeholder
                result.add(NULL)
                queue.add(null)
                queue.add(null)
            }
        }
        if (!hasNextLevel) queue.removeAll { true }
    }
    return result.joinToString()
}

// Decodes your encoded data to tree.
private fun deserializeBFS(data: String): TreeNode? {
    if (data.isEmpty()) return null

    val dataList = data.split(SEPARATOR)
    val nodeList: List<TreeNode?> = dataList.map { if (it == NULL) null else TreeNode(it.toInt()) }
    if (nodeList.size > 1) {
        for (i in 0 until nodeList.size/2) {
            val node = nodeList[i]
            if (node != null) {
                val leftNode = nodeList[2*i + 1]
                val rightNode = nodeList[2*i + 2]
                node.left = leftNode
                node.right = rightNode
            }
        }
    }
    return nodeList[0]
}

private fun serializeDFS(root: TreeNode?): String {
    if (root == null) return ""
    return serializeRecursively(root)
}

private fun serializeRecursively(root: TreeNode?): String {
    if (root == null) return NULL
    return root.num.toString() + SEPARATOR + serializeRecursively(root.left) + SEPARATOR + serializeRecursively(root.right)
}

private fun deserializeDFS(data: String): TreeNode? {
    if (data.isEmpty()) return null
    val nodeList = data.split(SEPARATOR).map { if (it == NULL) null else TreeNode(it.toInt()) }.toMutableList()
    return deserializeRecursively(nodeList)
}

private fun deserializeRecursively(nodeList: MutableList<TreeNode?>): TreeNode? {
    if (nodeList.isEmpty()) return null
    val root = nodeList.removeFirst()
    if (root != null) {
        root.left = deserializeRecursively(nodeList)
        root.right = deserializeRecursively(nodeList)
    }
    return root
}

fun main() {
    val root = TreeNode(0)
    val node1 = TreeNode(1)
    val node2 = TreeNode(2)
    val node4 = TreeNode(4)
    val node5 = TreeNode(5)
    root.left = node1
//    root.right = node2
//    node2.left = node4
//    node2.right = node5
    val serializationBFS = serializeBFS(root)
    println(serializationBFS)
    val serializationDFS = serializeDFS(root)
    println(serializationDFS)

    println(serializeBFS(deserializeBFS(serializationBFS)))
    println(serializeDFS(deserializeDFS(serializationDFS)))
}