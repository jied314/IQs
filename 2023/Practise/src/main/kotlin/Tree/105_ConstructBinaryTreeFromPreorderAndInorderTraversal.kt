package Tree

/**
 * Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and
 * inorder is the inorder traversal of the same tree, construct and return the binary tree.
 *
 * Similar idea as 104
 */

private var preIndex = 0
private fun buildTree(preorder: IntArray, inorder: IntArray): TreeNode? {
    if (preorder.isEmpty() || inorder.isEmpty()) return null
    return buildTree(preorder, inorder, 0, inorder.size-1)
}

private fun buildTree(preorder: IntArray, inorder: IntArray, inStart: Int, inEnd: Int): TreeNode? {
    if (inStart > inEnd) return null

    val rootValue = preorder[preIndex++]
    val rootNode = TreeNode(rootValue)
    val inIndex = inorder.indexOf(rootValue)
    rootNode.left = buildTree(preorder, inorder, inStart, inIndex-1)
    rootNode.right = buildTree(preorder, inorder, inIndex+1, inEnd)
    return rootNode
}