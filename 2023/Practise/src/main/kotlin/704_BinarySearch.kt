/**
 * The most basic and elementary form of BS.
 * Used to search for an element or condition which can be determined by accessing a single index in the array.
 *
 * Search Condition can be determined without comparing to the element's neighbors (or use specific elements around it).
 * No post-processing required because at each step.
 *
 * O(LogN) Time Complexity & O(1) Space Complexity
 */
private fun binarySearchBasic(nums: IntArray, target: Int) : Int {
    var left = 0
    var right = nums.size - 1
    while (left <= right) {
        val mid = left + (right - left) / 2
        if (nums[mid] < target) {
            left = mid + 1
        } else if (nums[mid] > target) {
            right = mid - 1
        } else {
            return mid
        }
    }

    // did not find the exact value, return -1
    return -1
}

/**
 * An advanced form of BS
 * Use the element's right neighbor to determine if the condition is met and decide whether to go left or right.
 * Post-processing required. Loop/Recursion ends when you have 1 element left.
 * Need to assess if the remaining element meets the condition.
 *
 * E.g. First Bad Version
 *
 * Use binary search to find the upper bound to insert the target number
 * O(LogN) Time Complexity & O(1) Space Complexity
 */
private fun binarySearchUpperBoundLC(nums: IntArray, target: Int) : Int {
    var left = 0
    var right = nums.size
    while (left < right) {
        val mid = (left + right) / 2
        if (nums[mid] <= target) {
            left = mid + 1
        } else {
            right = mid
        }
    }

    if (left > 0 && nums[left-1] == target) {
        return left - 1
    } else {
        return -1
    }
}

/**
 * Use
 */
private fun binarySearchUpperBound(nums: IntArray, target: Int) : Int {
    var left = 0
    var right = nums.size - 1
    while (left <= right) {
        val mid = (left + right) / 2
        if (nums[mid] < target) {
            left = mid + 1
        } else if (nums[mid] > target) {
            right = mid - 1
        } else {
            return mid
        }
    }

    return left
}

private fun binarySearchLowerBoundLC(nums: IntArray, target: Int) : Int {
    return -1
}

fun main() {
    val nums1 = intArrayOf(5)
    println(binarySearchUpperBound(nums1, 6))

    val nums2 = intArrayOf(-7, -4, -1, 0, 3, 5, 12)
    println(binarySearchUpperBound(nums2, 9))
    println(binarySearchUpperBoundLC(nums2, 9))
}
