package BinaryTree

/**
 * Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
 *
 * BSTIterator(TreeNode root) Initializes an object of the BSTIterator class.
 * The root of the BST is given as part of the constructor.
 * The pointer should be initialized to a non-existent number smaller than any element in the BST.
 *
 * boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer,
 * otherwise returns false.
 * int next() Moves the pointer to the right, then returns the number at the pointer.
 * Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will
 * return the smallest element in the BST.
 *
 * You may assume that next() calls will always be valid.
 * That is, there will be at least a next number in the in-order traversal when next() is called.
 *
 * Solutions:
 * 1. Flatten BST - recursive or iterative
 *    O(1) Time Complexity & O(N) Space Complexity
 *
 * 2. Build on top of iterative traversal, but only keep leftmost node in the stack
 *    O(1) Time Complexity & O(H) Space Complexity
 */

class BSTIteratorFlatten(root: TreeNode?) {

    private var curr: TreeNode = TreeNode(Int.MIN_VALUE)
    private val nodes = mutableListOf<TreeNode>()

    init {
        val stack = ArrayDeque<TreeNode>()
        var node = root
        while (stack.isNotEmpty() || node != null) {
            while (node != null) {
                stack.add(node)
                node = node.left
            }
            node = stack.removeLast()
            nodes.add(node)
            node = node.right
        }
        if (nodes.isNotEmpty()) curr.right = nodes[0]
    }

    fun next(): Int {
        val result = curr.right!!.num
        curr = curr.right!!
        return result
    }

    fun hasNext(): Boolean {
        return curr.right != null
    }
}

class BSTIteratorOptimized(root: TreeNode?) {

    private val stack = ArrayDeque<TreeNode>()
    init { dfsLeft(root) }

    fun next(): Int {
        val next = stack.removeLast()
        if (next.right != null) dfsLeft(next.right)
        return next.num
    }

    fun hasNext(): Boolean {
        return stack.isNotEmpty()
    }

    private fun dfsLeft(root: TreeNode?) {
        var node = root
        while (node != null) {
            stack.add(node)
            node = node.left
        }
    }
}