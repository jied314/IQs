/**
 * A peak element is an element that is strictly greater than its neighbors.
 *
 * Given a 0-indexed integer array nums, find a peak element, and return its index.
 * If the array contains multiple peaks, return the index to any of the peaks.
 *
 * You may imagine that nums[-1] = nums[n] = -∞.
 * In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
 *
 * You must write an algorithm that runs in O(log n) time.
 *
 * Constraints:
 *     1 <= nums.length <= 1000
 *     -231 <= nums[i] <= 231 - 1
 *     nums[i] != nums[i + 1] for all valid i.
 *
 * Example:
 * Input: nums = [1,2,3,1]
 * Output: 2
 * Explanation: 3 is a peak element and your function should return the index number 2.
 *
 * Solutions:
 * 1. Linear Scan until nums[i] > nums[i+1]
 *   O(N) Time Complexity & O(1) Space Complexity
 *
 * 2. Recursive Binary Search
 *   Since the peak element always exists in such array, narrow down the search space of the array
 * based on neighbors of the middle element.
 *   O(LogN) Time Complexity & O(LogN) Space Complexity (due to the recursion)
 *
 * 3. Iterative Binary Search - rewrite Approach#2 with iteration
 *   O(LogN) Time Complexity & O(1) Space Complexity
 */

private fun findPeakElementLinearScan(nums: IntArray): Int {
    for (i in 0 until nums.size-1) {
        if (nums[i] > nums[i+1]) return i
    }
    return nums.size-1
}

private fun findPeakElementRecursiveBS(nums: IntArray) : Int {
    return search(nums, 0, nums.size - 1)
}

private fun search(nums: IntArray, l: Int, r: Int): Int {
    if (l == r) return l
    val mid = (l + r) / 2
    return if (nums[mid] > nums[mid + 1]) search(nums, l, mid) else search(nums, mid + 1, r)
}

private fun findPeakElementIterativeBS(nums: IntArray) : Int {
    var left = 0
    var right = nums.size - 1
    while (left < right) {
        val mid = left + (right - left) / 2
        if (nums[mid] > nums[mid+1]) right = mid
        else left = mid + 1
    }
    return left
}

fun main() {
    val nums1 = intArrayOf(1, 2, 3, 1)
    println(findPeakElementLinearScan(nums1))
    println(findPeakElementRecursiveBS(nums1))
    println(findPeakElementIterativeBS(nums1))

    val nums2 = intArrayOf(1,2,1,3,5,6,4)
    println(findPeakElementLinearScan(nums2))
    println(findPeakElementRecursiveBS(nums2))
    println(findPeakElementIterativeBS(nums2))
}