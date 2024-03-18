package arrayAndString

import java.util.*


/**
 * The frequency of an element is the number of times it occurs in an array.
 *
 * You are given an integer array nums and an integer k.
 * In one operation, you can choose an index of nums and increment the element at that index by 1.
 *
 * Return the maximum possible frequency of an element after performing at most k operations.
 *
 * Example:
 *      Input: nums = [1,2,4], k = 5
 *      Output: 3
 *      Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
 *      4 has a frequency of 3.
 *
 * Solutions:
 * 1. Sliding Window - Iterate through the array as the target, shrink left index if exceeds k.
 *    Time Complexity: O(N*LogN) -> for loop takes O(N) since left increases
 *    Space Complexity: O(LogN) for sort
 *
 * 2. Advanced Sliding Window - Instead of shrinking the window, try growing it as much as we can
 *    Replace while loop with if condition - it is impossible for the window size to decrease, since each iteration
 *                                           increases right by 1 and left by either 0 or 1.
 *    Time Complexity: O(N*LogN)
 *    Space Complexity: O(LogN) for sort
 */

fun maxFrequencySlidingWindow(nums: IntArray, k: Int): Int {
    nums.sort()
    var left = 0
    var ans = 0
    var curr: Long = 0
    for (right in nums.indices) {
        val target = nums[right]
        curr += target.toLong() // total existing sum
        // shrink left if total_required_sum - total_existing_sum > k
        while ((right - left + 1) * target - curr > k) {
            curr -= nums[left].toLong()
            left++
        }
        ans = Math.max(ans, (right - left + 1))
    }
    return ans
}

fun maxFrequencyAdvancedSlidingWindow(nums: IntArray, k: Int): Int {
    nums.sort()
    var left = 0
    var curr: Long = 0
    for (right in nums.indices) {
        val target = nums[right]
        curr += target.toLong()
        if ((right - left + 1) * target - curr > k) {
            curr -= nums[left].toLong()
            left++
        }
    }
    return nums.size - left
}

fun main() {
    println(maxFrequencySlidingWindow(intArrayOf(1,2,4), 5))
    println(maxFrequencyAdvancedSlidingWindow(intArrayOf(1,2,4), 5))
}