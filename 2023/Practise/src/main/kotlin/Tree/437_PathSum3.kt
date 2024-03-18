package Tree

/**
 * Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values
 * along the path equals targetSum.
 *
 * The path does not need to start or end at the root or a leaf, but it must go downwards
 * (i.e., traveling only from parent nodes to child nodes).
 *
 * Solution - Prefix Sum (See 560)
 *   Time Complexity O(N) - traverse the whole tree
 *   Space Complexity O(N) - keep the hashmap
 */

private var result = 0

private fun pathSum(root: TreeNode?, targetSum: Int): Int {
    val sumCount = mutableMapOf<Long, Int>()
    dfs(root, 0L, targetSum, sumCount)
    return result
}

fun dfs(node: TreeNode?, sum: Long, targetSum: Int, sumCount: MutableMap<Long, Int>) {
    if (node == null) return

    val newSum = sum + node.num
    if (sumCount.contains(newSum)) result++
    if (sumCount.contains(newSum-targetSum)) result += sumCount[newSum-targetSum]!!

    // add the new mapping -> add it after updating result, since targetSum == 0 can cause issue.
    sumCount[newSum] = sumCount.getOrDefault(newSum, 0) + 1

    // visit children
    dfs(node.left, newSum, targetSum, sumCount)
    dfs(node.right, newSum, targetSum, sumCount)

    // remove the mapping
    sumCount[newSum] = sumCount[newSum]!! - 1
}

fun main() {
    val one = TreeNode(1)
    val two = TreeNode(-2)
    val three = TreeNode(3)
    val four = TreeNode(4)
    one.left = two
    one.right = three
    two.left = four
    println(pathSum(one, 3))
}