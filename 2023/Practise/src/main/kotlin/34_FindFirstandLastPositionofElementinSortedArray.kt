/**
 * Given an array of integers nums sorted in non-decreasing order,
 * find the starting and ending position of a given target value.
 * If target is not found in the array, return [-1, -1].
 *
 * You must write an algorithm with O(log n) runtime complexity.
 *
 * Example:
 * Input: nums = [5,7,7,8,8,10], target = 8
 * Output: [3,4]
 *
 * Solutions:
 * 1. Use recursion - O(LogN) Time Complexity & O(LogN) Space Complexity
 * 2. Use 2 BS, one for the lower bound and one for the upper bound
 *    O(LogN) Time Complexity & O(1) Space Complexity
 */

private fun searchRangeRecursive(nums: IntArray, target: Int): IntArray {
    val result = intArrayOf(-1, -1)
    searchRangeRecursive(nums, target, 0, nums.size-1, result)
    return result
}

private fun searchRangeRecursive(nums: IntArray, target: Int, startIndex: Int, endIndex: Int, resultRange: IntArray) {
    if (startIndex > endIndex || nums[startIndex] > target || nums[endIndex] < target) return

    val mid = startIndex + (endIndex - startIndex) / 2
    if (target > nums[mid]) searchRangeRecursive(nums, target, mid+1, endIndex, resultRange)
    else if (target < nums[mid]) searchRangeRecursive(nums, target, startIndex, mid-1, resultRange)
    else { // target == nums[mid]
        val leftRange = resultRange[0]
        val rightRange = resultRange[1]
        if (leftRange < 0 || leftRange > mid) resultRange[0] = mid
        if (rightRange < 0 || rightRange < mid) resultRange[1] = mid
        searchRangeRecursive(nums, target, mid+1, endIndex, resultRange)
        searchRangeRecursive(nums, target, startIndex, mid-1, resultRange)
    }
}
private fun searchRangeTwoBS(nums: IntArray, target: Int): IntArray {
    return intArrayOf(searchLeftRange(nums, target), searchRightRange(nums, target))
}

private fun searchLeftRange(nums: IntArray, target: Int): Int {
    var leftRange = -1
    var left = 0
    var right = nums.size - 1
    while (left <= right) {
        val mid = left + (right - left) / 2
        if (nums[mid] < target) left = mid + 1
        else if (nums[mid] > target) right = mid - 1
        else {
            if (leftRange < 0 || mid < leftRange) leftRange = mid
            right = mid - 1
        }
    }
    return leftRange
}

private fun searchRightRange(nums: IntArray, target: Int): Int {
    var rightRange = -1
    var left = 0
    var right = nums.size - 1
    while (left <= right) {
        val mid = left + (right - left) / 2
        if (nums[mid] < target) left = mid + 1
        else if (nums[mid] > target) right = mid - 1
        else {
            if (rightRange < 0 || mid > rightRange) rightRange = mid
            left = mid + 1
        }
    }
    return rightRange
}
fun main() {
    val nums1 = intArrayOf(5,7,7,8,8,10)
    println(searchRangeTwoBS(nums1, 8).contentToString())
    println(searchRangeRecursive(nums1, 8).contentToString())

    val nums2 = intArrayOf(5,7,7,8,8,10)
    println(searchRangeTwoBS(nums2, 6).contentToString())
    println(searchRangeRecursive(nums2, 6).contentToString())

    val nums3 = intArrayOf()
    println(searchRangeTwoBS(nums3, 0).contentToString())
    println(searchRangeRecursive(nums3, 0).contentToString())

    val nums4 = intArrayOf(1)
    println(searchRangeTwoBS(nums4, 1).contentToString())
    println(searchRangeRecursive(nums4, 1).contentToString())

    val nums5 = intArrayOf(1,2,3,3,3,3,4,5,9)
    println(searchRangeTwoBS(nums5, 3).contentToString())
    println(searchRangeRecursive(nums5, 3).contentToString())
}