/**
 * Given an integer array nums sorted in non-decreasing order,
 * remove some duplicates in-place such that each unique element appears at most twice.
 * The relative order of the elements should be kept the same.
 *
 * E.g. Input: nums = [1,1,1,2,2,3]
 * Output: 5, nums = [1,1,2,2,3,_]
 */
private fun removeDuplicates(nums: IntArray, k: Int): Int {
    // check duplicate count per number and reassign upto k-1 elements
    var i = 0 // the current number for which to check duplicates
    var index = 1 // index to iterate though the array
    var repeatCount = 0
    while (index < nums.count()) {
        if (nums[i] == nums[index]) {
            repeatCount++
            if (repeatCount < k) { // handle allowed count of duplicates -> reassign
                i++
                nums[i] = nums[i-1]
            }
        } else { // not duplicates, change the current number
            i++
            nums[i] = nums[index]
            repeatCount = 0
        }
        index++
    }
    return i + 1
}

// a simple version which better utilizes the sorted order of the array by just comparing the number
// instead of counting the duplicates
private fun removeDuplicatesSimple(nums: IntArray): Int {
    var i = 0
    for (n in nums) {
        if (i < 2 || n > nums[i - 2]) nums[i++] = n
    }
    return i
}

fun main() {
    val nums1 = intArrayOf(2)
    val nums2 = intArrayOf(1,1,2)
    val nums3 = intArrayOf(0,0,1,1,1,1,2,3,3)
    val nums4 = intArrayOf(1,1,1,2,2,3)

    println(removeDuplicates(nums1, 2))
    println(nums1.contentToString())

    println(removeDuplicates(nums2, 2))
    println(nums2.contentToString())

    println(removeDuplicates(nums3, 2))
    println(nums3.contentToString())

    println(removeDuplicates(nums4, 3))
    println(nums4.contentToString())

    var m = hashMapOf<Int, Int>()
}