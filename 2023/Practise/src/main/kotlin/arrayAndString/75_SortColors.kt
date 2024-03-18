package arrayAndString

/**
 * Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color
 * are adjacent, with the colors in the order red, white, and blue.
 *
 * We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
 *
 * You must solve this problem without using the library's sort function.
 */

fun sortColors(nums: IntArray): Unit {
    var i = 0
    var j = nums.size - 1
    var curr = 0
    while (curr <= j) {
        if (nums[curr] == 0) {
            nums[curr++] = nums[i]
            nums[i++] = 0
        } else if (nums[curr] == 2) {
            nums[curr] = nums[j]
            nums[j--] = 2
        } else {
            curr++
        }
    }
}

fun main() {
    val nums = intArrayOf(2,0,1)
    sortColors(nums)
    println(nums.contentToString())
}