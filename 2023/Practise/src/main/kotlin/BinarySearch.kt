/**
 * Use binary search for the exact value
 * O(LogN) Time Complexity & O(1) Space Complexity
 */
private fun binarySearch(nums: IntArray, target: Int) : Int {
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

    // did not find the exact value, return -1
    return -1
}

/**
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
