package Tree

/**
 * Given the root of a binary tree, return the inorder traversal of its nodes' values.
 *
 * Solutions:
 * 1. Use DFS Recursion - rely on stack provided by the system
 *   O(N) Time Complexity, O(LogN) Average Space Complexity & O(N) Worst Space Complexity
 *
 * 2. Use while loop & stack to mimic recursion
 *   Note: use extra while loop for DFS to the leftmost node
 *   O(N) Time Complexity & O(N) Space Complexity
 */
private fun inorderTraversalRecursively(root: TreeNode?): List<Int> {
    val result = mutableListOf<Int>()
    inorderTraversalRecursively(root, result)
    return result
}

private fun inorderTraversalRecursively(root: TreeNode?, traversal: MutableList<Int>) {
    root?.let {
        inorderTraversalRecursively(root.left, traversal)
        traversal.add(root.num)
        inorderTraversalRecursively(root.right, traversal)
    }
}

private fun inorderTraversalIterativeDFS(root: TreeNode?): List<Int> {
    val traversal = mutableListOf<Int>()
    val stack = ArrayDeque<TreeNode>()
    var current = root
    while (current != null || stack.isNotEmpty()) {
        // DFS to the leftmost node
        while (current != null) {
            stack.add(current)
            current = current.left
        }

        // process the node
        current = stack.removeLast()
        traversal.add(current.num)

        // visit the right node
        current = current.right
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

    println(inorderTraversalRecursively(fourNode))
    println(inorderTraversalIterativeDFS(fourNode))
}

