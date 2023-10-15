import java.util.Arrays

/**
 * Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
 * The order of the elements may be changed.
 * Then return the number of elements in nums which are not equal to val.
 *
 * Input: nums = [3,2,2,3], val = 3
 * Output: 2, nums = [2,2,_,_]
 *
 * 2 pointers
 */
fun removeElement(nums: IntArray, `val`: Int): Int {
    var pStart = 0 // start of non-duplicates
    var pEnd = nums.count() - 1
    while (pStart <= pEnd) {
        if (nums[pStart] == `val`) { // find duplicate, swap & shift pEnd
            nums[pStart] = nums[pEnd]
            nums[pEnd] = `val`
            pEnd--
        } else { // not duplicate, shift pStart
            pStart++
        }
    }
    return pStart
}

fun main() {
    var nums1 = intArrayOf(2)
    val nums2 = intArrayOf(3,2,2,3)
    var nums3 = intArrayOf(0,1,2,2,3,0,4,2)
    println(removeElement(nums3, 3))

    println(Arrays.toString(nums3))
}