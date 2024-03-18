package Tree

/**
 * Given the root of a binary tree, return its maximum depth.
 *
 * A binary tree's maximum depth is the number of nodes along the longest path from the root node down to
 * the farthest leaf node.
 *
 * Solutions:
 *      A good example to show top-down & bottom-up approach to recursively solve tree problems
 *
 * 1. Top-down Recursion
 *   Use distance from root to its children
 *
 * 2. Bottom-up Recursion
 *   Use distance from left node to the root
 *   Both recursive solutions had O(N) Time Complexity, O(N) worst Space Complexity & O(LogN) average Space Complexity
 *
 * 3. Tail recursion + BFS -> not reduce space since still use BFS
 *   Note: Tail recursion (the recursive call is the last action in the function) could reduce space usage,
 *         because the compiler can optimize the memory allocation of the call stack by reusing the same space
 *         for every recursive call, rather than creating the space for each one.
 *         A function cannot be tail recursion if there are multiple occurrences of recursive calls in the function,
 *         even if the last action is the recursive call. Because the system has to maintain the function call stack
 *         for the sub-function calls that occur within the same function.
 *
 * 4. Iterative approach with Stack
 */

private var maxDepth = 0
private fun maxDepthTopDown(root: TreeNode?): Int {
    maxDepthTopDown(root, 1)
    return maxDepth
}

private fun maxDepthTopDown(root: TreeNode?, depth: Int) {
    if (root == null) return
    if (root.left == null && root.right == null) {
        maxDepth = maxOf(maxDepth, depth)
    }
    maxDepthTopDown(root.left, depth+1)
    maxDepthTopDown(root.right, depth+1)
}

private fun maxDepthBottomUp(root: TreeNode?): Int {
    if (root == null) return 0
    val leftDepth = maxDepthBottomUp(root.left)
    val rightDepth = maxDepthBottomUp(root.right)
    return maxOf(leftDepth, rightDepth) + 1
}

fun main() {
    val oneNode = TreeNode(1)
    val twoNode = TreeNode(2)
    val threeNode = TreeNode(3)
    val fourNode = TreeNode(4)
    val fiveNode = TreeNode(5)
    val sixNode = TreeNode(6)
    val sevenNode = TreeNode(7)
    twoNode.left = oneNode
    twoNode.right = threeNode
    fourNode.left = twoNode
    fourNode.right = sixNode
    sixNode.left = fiveNode
    fiveNode.right = sevenNode

    println(maxDepthTopDown(fourNode))
    println(maxDepthBottomUp(fourNode))
}