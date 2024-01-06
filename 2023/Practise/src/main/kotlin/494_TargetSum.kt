/**
 * You are given an integer array nums and an integer target.
 *
 * You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums
 * and then concatenate all the integers.
 *
 * For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to
 * build the expression "+2-1".
 * Return the number of different expressions that you can build, which evaluates to target.
 *
 * Example:
 *   Input: nums = [1,1,1,1,1], target = 3
 *   Output: 5
 * Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
 *   -1 + 1 + 1 + 1 + 1 = 3
 *   +1 - 1 + 1 + 1 + 1 = 3
 *   +1 + 1 - 1 + 1 + 1 = 3
 *   +1 + 1 + 1 - 1 + 1 = 3
 *   +1 + 1 + 1 + 1 - 1 = 3
 *
 * Example:
 *   Input: nums = [1], target = 1
 *   Output: 1
 *
 * Solutions:
 * 1. Brute Force with all potential values
 *    Need to compare all potential values with target to find all solutions.
 *    O(2^N) Time Complexity and O(N) Space Complexity
 * 2. Brute Force with the count of expressions leading to target.
 *    O(2^N) Time Complexity and O(N) Space Complexity
 * 3. Brute Force with memorization to reduce work
 */

private fun findTargetSumWaysWithAllValues(nums: IntArray, target: Int): Int {
    val results = evaluate(nums, 0)
    var count = 0
    for (i in results) {
        if (i == target) count++
    }
    return count
}

private fun evaluate(nums: IntArray, i: Int): MutableList<Int> {
    if (i >= nums.size) return mutableListOf(0)
    val results = mutableListOf<Int>()
    for (result in evaluate(nums, i+1)) {
        results.add(result + nums[i])
        results.add(result - nums[i])
    }
    return results
}

private fun findTargetSumWaysWithCount(nums: IntArray, target: Int): Int {
    return evaluate(nums, 0, 0, target)
}

private fun evaluate(nums: IntArray, i: Int, sum: Int, target: Int): Int {
    if (i == nums.size) {
        if (sum == target) return 1
    } else {
        return evaluate(nums, i+1, sum+nums[i], target) + evaluate(nums, i+1, sum-nums[i], target)
    }
    return 0
}

fun main() {
    val nums1 = intArrayOf(1,1,1,1,1)
    println(findTargetSumWaysWithAllValues(nums1, 3))
    println(findTargetSumWaysWithCount(nums1, 3))

    val nums2 = intArrayOf(1)
    println(findTargetSumWaysWithAllValues(nums2, 1))
    println(findTargetSumWaysWithCount(nums2, 1))
}