package BinaryTree


/**
 * Populate each next pointer to point to its next right node. If there is no next right node,
 * the next pointer should be set to NULL.
 *
 * Initially, all next pointers are set to NULL.
 *
 * Solutions:
 * 1. BFS - same code as 116
 * 2. Constant space
 */

private var prev: Node? = null
private var leftmost: Node? = null
private fun processChild(childNode: Node?) {
    if (childNode != null) {
        // If the "prev" pointer is already set, i.e. if we already found at least
        // one node on the next level, set up its next pointer
        if (prev != null) {
            prev!!.next = childNode
        } else {
            // Else this child node is the first node we have encountered on the next level,
            // so it is the leftmost pointer
            leftmost = childNode
        }
        prev = childNode
    }
}
private fun connect(root: Node?): Node? {
    if (root == null) return root

    // The root node is the only node on the first level and hence it's the leftmost node for that level
    leftmost = root

    // Variable to keep track of leading node on the "current" level
    var curr: Node? = leftmost

    // We have no idea about the structure of the tree, so we keep going until the last level.
    // The nodes on the last level won't have any children
    while (leftmost != null) {

        // "prev" tracks the latest node on the "next" level
        // while "curr" tracks the latest node on the current level.
        prev = null
        curr = leftmost

        // We reset this so that we can re-assign it to the leftmost node of the next level.
        // Also, if there isn't one, this would help break us out of the outermost loop.
        leftmost = null

        // Iterate on the nodes in the current level using the next pointers already established.
        while (curr != null) {

            // Process both the children and update the prev and leftmost pointers as necessary.
            processChild(curr.left)
            processChild(curr.right)

            // Move onto the next node.
            curr = curr.next
        }
    }

    return root
}