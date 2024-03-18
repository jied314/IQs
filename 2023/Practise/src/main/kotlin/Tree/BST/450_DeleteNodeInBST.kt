package Tree.BST

import Tree.TreeNode


/**
 * Given a root node reference of a BST and a key, delete the node with the given key in the BST.
 * Return the root node reference (possibly updated) of the BST.
 *
 * Basically, the deletion can be divided into two stages:
 *  Search for a node to remove.
 *  If the node is found, delete the node.
 *
 *  Solutions - very hard!
 *  Recursively divide space for search & recursively delete target.
 *      If a leaf node, set itself to null;
 *      If has right child, swap the value with its successor and delete the successor;
 *      Else, swap the value with its predecessor and delete the predecessor.
 *
 *  O(H) Time Complexity & O(H) Space Complexity, where H is the tree height.
 */

private fun successorValue(root: TreeNode): Int {
    var node: TreeNode = root.left!!
    while (node.left != null) node = node.left!!
    return node.num
}

private fun predecessorValue(root: TreeNode): Int {
    var node: TreeNode = root.right!!
    while (node.right != null) node = node.right!!
    return node.num
}

private fun deleteNode(root: TreeNode?, key: Int): TreeNode? {
    if (root == null) return null

    var result = root
    if (key > result.num) { // delete from the right subtree
        result.right = deleteNode(result.right, key)
    } else if (key < root.num) { // delete from the left subtree
        result.left = deleteNode(result.left, key)
    } else {
        if (result.left == null && result.right == null) { // the node is a leaf
            result = null
        } else if (result.right != null) { // the node is not a leaf and has a right child
            result.num = successorValue(result)
            result.right = deleteNode(result.right, result.num)
        } else { // the node is not a leaf, has no right child, and has a left child
            result.num = predecessorValue(result)
            result.left = deleteNode(result.left, result.num)
        }
    }
    return result
}

fun main() {
    val root = TreeNode(5)
    val node2 = TreeNode(2)
    val node3 = TreeNode(3)
    val node4 = TreeNode(4)
    val node6 = TreeNode(6)
    val node7 = TreeNode(7)

    root.left = node3
    root.right = node6
    node3.left = node2
    node3.right = node4
    node6.right = node7
    val delete = deleteNode(root, 5)
    println(delete)
}