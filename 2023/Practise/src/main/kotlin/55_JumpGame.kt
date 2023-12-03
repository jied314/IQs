/**
 * You are given an integer array nums. You are initially positioned at the array's first index,
 * and each element in the array represents your maximum jump length at that position.
 *
 * Return true if you can reach the last index, or false otherwise.
 *
 * Solutions:
 *
 */
private fun canJump(nums: IntArray): Boolean {
    if (nums.size <=1) return true

    var furthest = nums[0]
    for (i in 0..nums.size-2) {
        if (i > furthest) return false
        else {
            val maxJump = i + nums[i]
            if (maxJump >= nums.size-1) return true
            else if (maxJump > furthest) {
                furthest = maxJump
            }
        }

    }
    return false
}

fun main() {
    val nums1 = intArrayOf(2,3,1,1,4)
    println(canJump(nums1))

    val nums2 = intArrayOf(3,2,1,0,4)
    println(canJump(nums2))
}