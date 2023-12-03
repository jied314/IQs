import kotlin.math.max

/**
 * Given an integer array nums, return the length of the longest strictly increasing
 * subsequence.
 *
 * Example 1:
 * Input: nums = [10,9,2,5,3,7,101,18]
 * Output: 4
 * Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
 *
 * Solutions:
 * 1. Dynamic Programming
 *    dp[i] = max(dp[j] + 1) with j < i and nums[j] < nums[i]
 *    O(N*N) Time Complexity and O(N) Space Complexity
 *
 * 2. Intelligently build a subsequence
 *    If nums[i] is greater than the largest element in the subsequence, append it;
 *    or else, replace the min element that is greater than nums[i].
 *    O(N*N) Time Complexity and O(N) Space Complexity
 *    Note: this algorithm does not produce the correct subsequence, but the length is correct
 * since the list hosting the subsequence grows as needed but does not shrink.
 *
 * 3. Improve 2 with Binary Search
 *    O(N*LogN) Time Complexity and O(N) Space Complexity
 */

private fun lengthOfLISCommonDP(nums: IntArray): Int {
    val result = IntArray(nums.size) { 1 }
    for (i in 1 until nums.size) {
        for (j in 0 until i) {
            if (nums[i] > nums[j]) {
                result[i] = max(result[i], result[j] + 1)
            }
        }
    }
    return result.max()
}

private fun lengthOfLISIntelligentSubsequence(nums: IntArray): Int {
    if (nums.isEmpty()) return 0

    val result = mutableListOf<Int>()
    result.add(nums[0])
    for (i in 1 until nums.size) {
        if (nums[i] > result.last) {
            result.add(nums[i])
        } else {
            // Find the first element in result that is greater than or equal to num
            var j = 0
            while (result[j] < nums[i]) {
                j++
            }
            result[j] = nums[i]
        }
    }
    return result.size
}

fun main() {
    val nums1 = intArrayOf(10,9,2,5,3,7,101,18)
    println(lengthOfLISIntelligentSubsequence(nums1))
}