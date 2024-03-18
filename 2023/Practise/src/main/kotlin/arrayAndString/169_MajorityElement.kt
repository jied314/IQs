package arrayAndString

/**
 * Given an array nums of size n, return the majority element.
 *
 * The majority element is the element that appears more than ⌊n / 2⌋ times.
 * You may assume that the majority element always exists in the array.
 *
 * Input: nums = [2,2,1,1,1,2,2]
 * Output: 2
 */

// O(N) time complexity & O(N) space complexity
private fun majorityElement_HashMap(nums: IntArray): Int {
    if (nums.count() < 3) return nums[0]

    val countMap = hashMapOf<Int, Int>()
    var maxCount = 1
    var majorityElement = 0
    for (n in nums) {
        if (countMap.contains(n)) {
            val count = countMap[n]?.plus(1) ?: 1
            countMap[n] = count
            if (count > maxCount) {
                maxCount = count
                majorityElement = n
            }
        } else {
            countMap[n] = 1
        }
    }
    return majorityElement
}

// Sort the array first and then find the middle element
// Utilizes the fact that the majority element in a sorted array should always occupy the middle position
// 
private fun majorityElement_sort(nums: IntArray): Int {
    nums.sort()
    val size = nums.count()
    return nums[size / 2]
}

