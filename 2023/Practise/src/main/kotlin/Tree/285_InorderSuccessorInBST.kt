package Tree


/**
 * Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST.
 * If the given node has no in-order successor in the tree, return null.
 *
 * The successor of a node p is the node with the smallest key greater than p.val.
 *
 * Solutions:
 * 1. Not utilizing the property of Binary Search Tree
 *    Case 1: P has right child -> inorder successor is the leftmost node of its right subtree
 *    Case 2: P does not have right child -> inorder traverse the whole tree and track previous node.
 *        If previous == p, then the current node is the inorder successor.
 *    O(N) Time Complexity & O(N) Space Complexity
 *
 * 2. Utilize the sorted property of BST - can discard half search space for each comparison
 *    O(LogN) Time Complexity for balanced BST, O(N) Worst Time Complexity & O(1) Space Complexity
 */

private var previous: TreeNode? = null
private var inorderSuccessorNode: TreeNode? = null

private fun inorderSuccessorNoBST(root: TreeNode?, p: TreeNode?): TreeNode? {
    if (p == null) return null

    // Case 1: We simply need to find the leftmost node in the subtree rooted at p.right.
    if (p.right != null) {
        var leftmost = p.right
        while (leftmost!!.left != null) {
            leftmost = leftmost.left
        }
        inorderSuccessorNode = leftmost
    } else {
        // Case 2: We need to perform the standard in-order traversal and keep track of the previous node.
        inorderCase2(root, p)
    }
    return inorderSuccessorNode
}

private fun inorderCase2(node: TreeNode?, p: TreeNode) {
    if (node == null) return

    // DFS to the leftmost
    inorderCase2(node.left, p)

    // Check if previous is the inorder predecessor of node
    if (previous == p && inorderSuccessorNode == null) {
        inorderSuccessorNode = node
        return
    }

    // process the current - keep previous up-to-date for further recursions
    previous = node

    // visit the right
    inorderCase2(node.right, p)
}

private fun inorderSuccessorBSTIterative(root: TreeNode?, p: TreeNode?): TreeNode? {
    if (p == null) return null

    var current: TreeNode? = root
    var successor: TreeNode? = null
    while (current != null) {
        if (p.num >= current.num) {
            current = current.right
        } else {
            successor = root
            current = current.left
        }
    }
    return successor
}

private fun inorderSuccessorBSTRecursive(root: TreeNode?, p: TreeNode?): TreeNode? {
    if (p == null) return null
    return dfs(root, p, null)
}

private fun dfs(root: TreeNode?, p: TreeNode, successor: TreeNode?): TreeNode? {
    if (root == null) return successor
    return if (p.num >= root.num) dfs(root.right, p, successor) else dfs(root.left, p, root)
}