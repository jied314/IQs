import kotlin.math.max

/**
 * You are a professional robber planning to rob houses along a street.
 * Each house has a certain amount of money stashed, the only constraint stopping you
 * from robbing each of them is that adjacent houses have security systems connected and
 * it will automatically contact the police if two adjacent houses were broken into on the same night.
 *
 * Given an integer array nums representing the amount of money of each house,
 * return the maximum amount of money you can rob tonight without alerting the police.
 *
 * Example 1:
 *
 * Input: nums = [1,2,3,1]
 * Output: 4
 * Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
 * Total amount you can rob = 1 + 3 = 4.
 *
 * Solutions:
 * 1. DP with iteration - optimal
 *    robFrom(0..i) = max(robFrom(0..i-1), robFrom(0..i+2) + nums[i])
 *    O(N) Time Complexity & O(1) Space Complexity
 *
 * 2. DP with recursion
 *    O(2^N) Time Complexity & O(N) Space Complexity without memorization
 *    O(N) Time Complexity & O(N) Space Complexity with memorization
 *    Note: Space complexity of recursive algorithm is the tree depth
 */

private fun rob(nums: IntArray): Int {
    return robRecursiveWithMemorization(nums)
}

private fun robIterative(nums: IntArray): Int {
    if (nums.isEmpty()) return 0
    if (nums.size == 1) return nums[0]

    var first = nums[0]
    var second = nums[1]
    for (j in 2 until nums.size) {
        val next = max(first + nums[j], second)
        first = max(first, second)
        second = next
    }
    return max(first, second)
}

// Recursion without memorization
private fun robRecursive(nums: IntArray, startIndex: Int, length: Int): Int {
    return if (length < 1) 0
    else if (length == 1) nums[startIndex]
    else if (length == 2) max(nums[startIndex], nums[startIndex+1])
    else max(nums[startIndex] + robRecursive(nums, startIndex+2, length-2),
        nums[startIndex+1] + robRecursive(nums,startIndex+3, length-3))
}

private fun robRecursiveWithMemorization(nums: IntArray): Int {
    return robRecursiveWithMemorization(nums, 0, nums.size, hashMapOf())
}

private fun robRecursiveWithMemorization(
    nums: IntArray,
    startIndex: Int,
    length: Int,
    visited: MutableMap<Int, Int>
): Int {
    if (length < 1) return 0
    if (length == 1) return nums[startIndex]
    if (visited.contains(startIndex)) {
        visited[startIndex]?.let {
            return it
        }
    }

    val result = max(nums[startIndex] + robRecursiveWithMemorization(nums, startIndex + 2, length-2, visited),
        nums[startIndex+1] + robRecursiveWithMemorization(nums, startIndex+3, length-3, visited))
    visited[startIndex] = result
    return result
}
fun main() {
    val nums1 = intArrayOf(1, 2, 3, 1)
    println(rob(nums1))

    val nums2 = intArrayOf(2,7,9,3,1)
    println(rob(nums2))

    val nums3 = intArrayOf(2,1,1,2)
    println(rob(nums3))
}