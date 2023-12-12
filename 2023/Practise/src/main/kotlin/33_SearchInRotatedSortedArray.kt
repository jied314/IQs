/**
 * There is an integer array nums sorted in ascending order (with distinct values).
 * Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
 * such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
 * For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
 *
 * Given the array nums after the possible rotation and an integer target,
 * return the index of target if it is in nums, or -1 if it is not in nums.
 *
 * You must write an algorithm with O(log n) runtime complexity.
 *
 * Example:
 * Input: nums = [4,5,6,7,0,1,2], target = 0
 * Output: 4
 *
 * Solutions:
 * 1. Find pivot index + Binary Search
 *    O(LogN) Time Complexity & O(1) Space Complexity
 * 2. Binary search directly on the rotated sorted array
 *    O(LogN) Time Complexity & O(1) Space Complexity
 */

private fun search(nums: IntArray, target: Int): Int {
    var left = 0
    var right = nums.size - 1
    while (left <= right) {
        val mid = (left + right) / 2
        if (nums[mid] == target) return mid
        else if ((isSorted(nums, left, mid) && isWithinRange(nums, left, mid, target)) ||
            (isSorted(nums, mid+1, right) && !isWithinRange(nums, mid+1, right, target))) {
            // search the right side if:
            // 1. the left side is sorted and the target lies within or
            // 2. the right side is sorted but the target does not lie within
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    return -1
}

private fun isSorted(nums: IntArray, startIndex: Int, endIndex: Int) : Boolean {
    return startIndex <= endIndex && nums[startIndex] <= nums[endIndex]
}

private fun isWithinRange(nums: IntArray, startIndex: Int, endIndex: Int, target: Int) : Boolean {
    return target >= nums[startIndex] && target <= nums[endIndex]
}

fun main() {
    val nums1 = intArrayOf(4,5,6,7,0,1,2)
    println(search(nums1, 0))

    val nums2 = intArrayOf(4,5,6,7,0,1,2)
    println(search(nums2, 3))

    val nums3 = intArrayOf(1)
    println(search(nums3, 0))

    val nums4 = intArrayOf(3,4,5,6,1,2)
    println(search(nums4, 2))
}