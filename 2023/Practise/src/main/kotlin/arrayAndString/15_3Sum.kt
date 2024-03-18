package arrayAndString

/**
 * Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
 * such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
 *
 * Notice that the solution set must not contain duplicate triplets.
 *
 * Solutions:
 * 1. Two Pointers -> iterate on array and apply two sum (reduce search space based on sum)
 *    Time Complexity: O(N*N)
 *    Space Complexity: O(1)
 * 2. HashMap
 */

fun threeSum(nums: IntArray): List<List<Int>> {
    nums.sorted()
    nums.sort()
    val result = mutableListOf<List<Int>>()
    for (i in 0..<nums.size-2) {
        // skip the current i since it is a duplicate
        if (i> 0 && nums[i] == nums[i-1]) continue

        // same solution for two sum
        var l = i+1
        var r = nums.size-1
        while (l < r) {
            val sum = nums[i] + nums[l] + nums[r]
            if (sum == 0) {
                result.add(listOf(nums[i], nums[l++], nums[r--]))
                // skip the current l since it is a duplicate
                while (l < r && nums[l] == nums[l-1]) l++
            }
            else if (sum < 0) l++
            else r--
        }
    }
    return result
}

fun main() {
    val nums = intArrayOf(-1,0,1,2,-1,-4)
    println(threeSum(nums))
}
