package arrayAndString

/**
 * Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
 *
 * Input: nums = [1,2,3,4,5,6,7], k = 3
 * Output: [5,6,7,1,2,3,4]
 *
 * Solutions:
 * 1. Brute Force - rotate the array by k times
 *    O(N*K) time complexity & O(1) space complexity
 *
 * 2. Use an extra array - store the rotated element in the right order in another array (i + k) % length
 *    and copy to the original array
 *    O(N) time complexity & O(N) space complexity
 *
 * 3. Use cyclic replacement
 *    Note how to store temp values via coding and avoid cycles
 *    O(N) time Complexity & O(1) space complexity
 *
 * 4. Use reverse
 *    First reverse the whole array, then the first k elements, and finally the rest (n-k)
 *    O(N) time complexity & O(1) space complexity
 */

// Create a new array to store rotated array - All O(N) complexity
private fun rotateExtraArray(nums: IntArray, k: Int): Unit {
    // rotation can form repeated loops, find the smallest step
    val size = nums.count()
    val step = k % size
    if (step == 0) return // no need to rotate

    val newArray = Array<Int>(size) {0}
    for ((index, value) in nums.withIndex()) {
        val newIndex = (index + step) % size
        newArray[newIndex] = value
    }
    for ((index, value) in newArray.withIndex()) {
        nums[index] = value
    }
}

private fun rotateWithCyclicReplacement(nums: IntArray, k: Int): Unit {
    // rotation can repeat itself, find the smallest step
    val size = nums.count()
    val step = k % size
    if (step == 0) return // no need to rotate

    var count = 0
    var start = 0
    while (count < size) {
        var current = start
        var prev = nums[start]
        do {
            val next = (current + step) % size
            val temp = nums[next]
            nums[next] = prev
            prev = temp
            current = next
            count++
        } while (start != current)
        start++
    }
}

private fun rotateWithReverse(nums: IntArray, k: Int): Unit {
    val size = nums.count()
    val step = k % size
    if (step == 0) return // no need to rotate

    // reverse the whole
    nums.reverse()
    // reverse the first step
    nums.reverse(0, step)
    // reverse the rest
    nums.reverse(step, size)
}

fun main() {
    val nums1 = intArrayOf(1,2,3,4,5,6,7)
    rotateWithReverse(nums1, 3)
    println(nums1.contentToString())

    val nums2 = intArrayOf(-1,-100,3,99)
    rotateWithReverse(nums2, 2)
    println(nums2.contentToString())

    val nums3 = intArrayOf(1, 2, 3, 4, 5, 6)
    rotateWithReverse(nums3, 4)
    println(nums3.contentToString())
}

