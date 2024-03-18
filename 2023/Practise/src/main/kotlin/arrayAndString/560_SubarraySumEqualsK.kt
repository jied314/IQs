package arrayAndString


/**
 * Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
 *
 * A subarray is a contiguous non-empty sequence of elements within an array.
 *
 * Example:
 *      Input: nums = [1,1,1], k = 2
 *      Output: 2
 *
 * Solutions:
 * 1. Use cumulative sum - the sum for the subarray nums[i:j] is: sum[i:j] == sum[j+1] − sum[i]
 *    Time Complexity O(N*N)
 *    Space Complexity O(N)
 *
 * 2. Use cumulative sum with constant space
 *    Time Complexity O(N*N)
 *    Space Complexity O(1)
 *
 * 3. Use hash to store sum count, and update result if map contains sum-k
 *    Time Complexity O(N)
 *    Space Complexity O(N)
 */

private fun subarraySumCumulativeSum(nums: IntArray, k: Int): Int {
    var count = 0
    val sum = IntArray(nums.size + 1)
    sum[0] = 0
    // calculate cumulative sum
    for (i in 1..nums.size) sum[i] = sum[i - 1] + nums[i - 1]
    // calculate subarray sum
    for (start in nums.indices) {
        for (end in start + 1..nums.size) {
            if (sum[end] - sum[start] == k) count++
        }
    }
    return count
}

private fun subarraySumCumulativeSumConstantSpace(nums: IntArray, k: Int): Int {
    var count = 0
    for (start in nums.indices) {
        var sum = 0
        for (end in start..<nums.size) {
            sum += nums[end]
            if (sum == k) count++
        }
    }
    return count
}

private fun subarraySumCumulativeSumHash(nums: IntArray, k: Int): Int {
    var count = 0
    var sum = 0
    val map = mutableMapOf<Int, Int>()
    map[0] = 1
    for (i in nums.indices) {
        sum += nums[i]
        if (map.containsKey(sum - k)) count += map[sum - k]!!
        map[sum] = map.getOrDefault(sum, 0) + 1
    }
    return count
}