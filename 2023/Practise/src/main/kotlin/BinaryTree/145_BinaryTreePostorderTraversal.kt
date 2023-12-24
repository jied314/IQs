package BinaryTree

import kotlin.collections.ArrayDeque
import kotlin.collections.List
import kotlin.collections.MutableList
import kotlin.collections.emptyList
import kotlin.collections.isNotEmpty
import kotlin.collections.mutableListOf
import kotlin.collections.removeLast
import kotlin.collections.reversed


/**
 * Given the root of a binary tree, return the postorder traversal of its nodes' values.
 *
 * Solutions:
 * 1. Use DFS Recursion - rely on stack provided by the system
 *   O(N) Time Complexity, O(LogN) Average Space Complexity & O(N) Worst Space Complexity
 *
 * 2. Iterative Inverse Preorder
 *    [Left, Right, Root] == Inverse [Root, Right, Left]
 *    O(N) Time Complexity & O(N) Space Complexity
 *
 * 3. Use while loop & stack to mimic recursion
 *    Note: use extra while loop for DFS to the leftmost & rightmost node
 *    O(N) Time Complexity & O(N) Space Complexity
 */

private fun postorderTraversalRecursively(root: TreeNode?): List<Int> {
    val result = mutableListOf<Int>()
    postorderTraversalRecursively(root, result)
    return result
}

private fun postorderTraversalRecursively(root: TreeNode?, traversal: MutableList<Int>) {
    root?.let {
        postorderTraversalRecursively(root.left, traversal)
        postorderTraversalRecursively(root.right, traversal)
        traversal.add(root.num)
    }
}

private fun postorderTraversalIterativeInversePreorder(root: TreeNode?): List<Int> {
    if (root == null) return emptyList()

    val traversal = mutableListOf<Int>()
    val stack = ArrayDeque<TreeNode>()
    stack.add(root)
    while (stack.isNotEmpty()) {
        val current = stack.removeLast()
        traversal.add(current.num)
        if (current.left != null) stack.add(current.left!!)
        if (current.right != null) stack.add(current.right!!)
    }
    return traversal.reversed()
}

private fun postorderTraversalIterative(root: TreeNode?): List<Int> {
    val traversal = mutableListOf<Int>()
    val stack = ArrayDeque<TreeNode>()
    var current = root
    while (current != null || !stack.isEmpty()) {
        // push nodes: right -> node -> left
        while (current != null) {
            if (current.right != null) {
                stack.add(current.right!!)
            }
            stack.add(current)
            current = current.left
        }

        current = stack.removeLast()

        if (!stack.isEmpty() && current.right == stack.last()) { // if the right subtree is not yet processed
            stack.removeLast()
            stack.add(current)
            current = current.right
        } else { // if we're on the leftmost leaf
            traversal.add(current.num)
            current = null
        }
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

    println(postorderTraversalRecursively(fourNode))
    println(postorderTraversalIterativeInversePreorder(fourNode))
    println(postorderTraversalIterative(fourNode))
}