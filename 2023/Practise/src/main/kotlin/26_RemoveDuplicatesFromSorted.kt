import java.util.Arrays

/**
 * Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place
 * such that each unique element appears only once.
 * The relative order of the elements should be kept the same.
 * Then return the number of unique elements in nums.
 *
 * Input: nums = [0,0,1,1,1,2,2,3,3,4]
 * Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
 */
private fun removeDuplicates(nums: IntArray): Int {
    var i = 0 // track non-duplicate
    var index = 1
    // if duplicate, move index; else move i and assign
    while (index < nums.count()) {
        if (nums[i] != nums[index]) { // non-duplicate
            i++
            nums[i] = nums[index]
        }
        index++
    }
    return i+1
}

fun main() {
    var nums1 = intArrayOf(2)
    val nums2 = intArrayOf(1,1,2)
    var nums3 = intArrayOf(0,0,1,1,1,2,2,3,3,4)
    println(removeDuplicates(nums3))

    println(Arrays.toString(nums3))
}