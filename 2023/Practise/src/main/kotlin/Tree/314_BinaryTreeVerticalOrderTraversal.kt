package Tree

import java.util.TreeMap

/**
 * Given the root of a binary tree, return the vertical order traversal of its nodes' values.
 * (i.e., from top to bottom, column by column).
 *
 * If two nodes are in the same row and column, the order should be from left to right.
 *
 * Solutions:
 * Note: cannot use simple recursion since it does not guarantee: on the same col, upper nodes is added earlier than lower nodes.
 * Key: Top -> Bottom, Left -> Right => level order traversal is good to use!
 *
 * 1. BFS with sorting - use a map to store vertical node per each column
 *    Time Complexity O(N*LogN) - O(N) for traversing all nodes and O(N*LogN) for using sorted map
 *    Space Complexity O(N)
 * 2. (Optimization) BFS w/o sorting - the column range is known, so iterate from min to max.
 *    Time Complexity O(N) - for traversing all nodes
 *    Space Complexity O(N) - for storing all nodes
 * 3. DFS - traverse the tree and record column & row for each node. Then iterate per column for all rows top->bottom.
 *    Time Complexity O(W*H*LogH) - W as tree width and H as tree height.
 *    Space Complexity: O(N)
 */

private fun verticalOrderWithSorting(root: TreeNode?): List<List<Int>> {
    if (root == null) return emptyList()
    val sortedMap = TreeMap<Int, MutableList<Int>>()
    val queue = ArrayDeque<Pair<Int, TreeNode>>()
    queue.add(Pair(0, root))
    while (queue.isNotEmpty()) {
        var count = queue.size
        while (count > 0) {
            val (col, node) = queue.removeFirst()
            sortedMap.putIfAbsent(col, mutableListOf())
            sortedMap[col]!!.add(node.num)
            if (node.left != null) queue.add(Pair(col-1, node.left!!))
            if (node.right != null) queue.add(Pair(col+1, node.right!!))
            count--
        }
    }
    return sortedMap.values.toList()
}

private fun verticalOrderWithoutSorting(root: TreeNode?): List<List<Int>> {
    if (root == null) return emptyList()
    val columnMap = mutableMapOf<Int, MutableList<Int>>()
    val queue = ArrayDeque<Pair<Int, TreeNode>>()
    queue.add(Pair(0, root))
    var minCol = Integer.MAX_VALUE
    var maxCol = Integer.MIN_VALUE
    while (queue.isNotEmpty()) {
        var count = queue.size
        while (count > 0) {
            val (col, node) = queue.removeFirst()
            minCol = Math.min(minCol, col)
            maxCol = Math.max(maxCol, col)
            columnMap.putIfAbsent(col, mutableListOf())
            columnMap[col]!!.add(node.num)
            if (node.left != null) queue.add(Pair(col-1, node.left!!))
            if (node.right != null) queue.add(Pair(col+1, node.right!!))
            count--
        }
    }

    val result = mutableListOf<MutableList<Int>>()
    for (col in IntRange(minCol, maxCol)) {
        if (columnMap.contains(col)) result.add(columnMap[col]!!)
    }
    return result
}

fun main() {
    val root = TreeNode(3)
    root.left = TreeNode(9)
    val node20 = TreeNode(20)
    root.right = node20
    node20.left = TreeNode(15)
    node20.right = TreeNode(7)

    println(verticalOrderWithSorting(root))
    println(verticalOrderWithoutSorting(root))
}
