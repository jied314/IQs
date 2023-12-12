/**
 * Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
 *
 * For example, the array nums = [0,1,2,4,5,6,7] might become:
 * [4,5,6,7,0,1,2] if it was rotated 4 times.
 * [0,1,2,4,5,6,7] if it was rotated 7 times.
 *
 * Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array
 * [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
 *
 * Given the sorted rotated array nums of unique elements, return the minimum element of this array.
 * You must write an algorithm that runs in O(log n) time.
 *
 * Example:
 * Input: nums = [3,4,5,1,2]
 * Output: 1
 * Explanation: The original array was [1,2,3,4,5] rotated 3 times.
 */

private fun findMin(nums: IntArray): Int {
    var left = 0
    var right = nums.size - 1
    while (left < right) {
        val mid = left + (right - left) / 2
        if (!isSorted(nums, left, mid)) {
            right = mid
        } else if (!isSorted(nums, mid+1, right)) {
            left = mid + 1
        } else { // both sides are sorted
            if (nums[left] < nums[mid+1]) right = mid
            else left = mid + 1
        }
     }
    return nums[left]
}

private fun isSorted(nums: IntArray, left: Int, right: Int): Boolean {
    return left <= right && nums[left] <= nums[right]
}

fun main() {
    val nums1 = intArrayOf(3,4,5,1,2)
    println(findMin(nums1))

    val nums2 = intArrayOf(4,5,6,7,0,1,2)
    println(findMin(nums2))

    val nums3 = intArrayOf(11,13,15,17)
    println(findMin(nums3))
}