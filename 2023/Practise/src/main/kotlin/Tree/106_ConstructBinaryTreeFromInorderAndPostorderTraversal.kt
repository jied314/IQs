package Tree

/**
 * Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and
 * postorder is the postorder traversal of the same tree, construct and return the binary tree.
 *
 * Solutions:
 *   Based on the value from preorder/postorder traversal to split the inorder traversal into left and right subtrees.
 *   Only use inorder to check:
 *      if the current subtree is empty (= return Null)
 *      or not (= continue to construct the subtree).
 *
 * O(N) Time Complexity & O(N) Space Complexity
 */

// traverse postOrder backward (Root -> Right -> Left), postIndex always decrease, never skip
private var postIndex = -1
private fun buildTree(inorder: IntArray, postorder: IntArray): TreeNode? {
    if (inorder.isEmpty() || postorder.isEmpty()) return null
    postIndex = postorder.size - 1
    return buildTree(inorder, 0, inorder.size-1, postorder)
}

private fun buildTree(inorder: IntArray, inStart: Int, inEnd: Int, postorder: IntArray): TreeNode? {
    if (inStart > inEnd) return null

    val rootValue = postorder[postIndex--]
    val rootNode = TreeNode(rootValue)
    val rootInIndex = inorder.indexOf(rootValue) // can speed up by building element->index map
    rootNode.right = buildTree(inorder, rootInIndex+1, inEnd, postorder)
    rootNode.left = buildTree(inorder, inStart, rootInIndex-1, postorder)
    return rootNode
}

fun main() {
//    val node3 = TreeNode(3)
//    val node9 = TreeNode(9)
//    val node20 = TreeNode(20)
//    val node15 = TreeNode(15)
//    val node7 = TreeNode(7)
//
//    node3.left = node9
//    node3.right = node20
//    node20.left = node15
//    node20.right = node7

    val inOrder = intArrayOf(9,3,15,20,7)
    val postOrder = intArrayOf(9,15,7,20,3)
    val rootNode = buildTree(inOrder, postOrder)
    println(levelOrderBFS(rootNode))
}