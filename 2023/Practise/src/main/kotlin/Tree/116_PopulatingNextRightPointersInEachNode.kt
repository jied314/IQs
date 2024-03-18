package Tree


/**
 * You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
 * The binary tree has the following definition:
 *
 * Populate each next pointer to point to its next right node. If there is no next right node,
 * the next pointer should be set to NULL.
 * Initially, all next pointers are set to NULL.
 *
 * Solutions:
 * 1. Use BFS, similar to Binary Tree level order traversal (102)
 * O(N) Time Complexity & O(N) Space Complexity
 *
 * 2. Use recursion & the next pointer - still takes up space in stack
 * O(N) Time Complexity & O(N) Space Complexity
 *
 * 3. Utilize the next pointer to avoid taking up space - iterate as linked list fashion
 * O(N) Time Complexity & O(1) Space Complexity
 */

object Node {
    val num: Int = 0
    var left: Node? = null
    var right: Node? = null
    var next: Node? = null
}

private fun connectBFS(root: Node?): Node? {
    if (root == null) return root
    val queue = ArrayDeque<Node>()
    queue.add(root)
    while (queue.isNotEmpty()) {
        val size = queue.size
        for (i in 0 until size) {
            val prev = queue.removeFirst()
            if (i+1 < size) prev.next = queue.first()
            if (prev.left != null) queue.add(prev.left!!)
            if (prev.right != null) queue.add(prev.right!!)
        }
    }
    return root
}

private fun connectDFSRecursively(root: Node?): Node? {
    if (root == null) return null
    if (root.left != null) { // Connection Type 1
        root.left!!.next = root.right
    }
    if (root.next != null && root.right != null) { // Connection Type 2
        root.right!!.next = root.next!!.left
    }
    // DFS
    if (root.left != null) connectDFSRecursively(root.left)
    if (root.right != null) connectDFSRecursively(root.right)
    return root
}

private fun connectLinkedList(root: Node?): Node? {
    if (root == null) return root

    // Start with the root node. There are no next pointers that need to be set up on the first level
    var leftmost = root

    // Once we reach the final level, we are done
    while (leftmost!!.left != null) {

        // Iterate the "linked list" starting from the head node and using the next pointers,
        // establish the corresponding links for the next level
        var head = leftmost
        while (head != null) {
            // Connection Type 1
            head.left!!.next = head.right

            // Connection Type 2
            if (head.next != null) {
                head.right!!.next = head.next!!.left
            }

            // Progress along the list (nodes on the current level)
            head = head.next
        }

        // Move onto the next level
        leftmost = leftmost.left
    }

    return root
}