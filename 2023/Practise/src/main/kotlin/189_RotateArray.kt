/**
 * Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
 *
 * Input: nums = [1,2,3,4,5,6,7], k = 3
 * Output: [5,6,7,1,2,3,4]
 */

// reverse the first k elements, then the rest, and reverse the whole array
private fun rotate(nums: IntArray, k: Int): Unit {
    val length = nums.count()
    var step = k % length; // if we have let's say 101 to rotate, then we only rotate it 1 time not 101 times
    if(step < 0){ // if we get -ve value, then -ve is just equals to it's -ve + array.length
        step += length;
    }
    // part 1 reverse
    nums.reverse(0, step+1)
    // part 2 reverse
    nums.reverse(step+1, length)
    // complete reverse
    nums.reverse()
}

private fun rotate_failure(nums: IntArray, k: Int): Unit {
    val size = nums.count()
    val step = k % size
    if (step == 0) return // no need to rotate

    // rotate can form repeated loops
    val totalRotationPerLoop = if (size % step == 0) size / step else size
    val totalLoops = size / totalRotationPerLoop
    var loop = 0
    while (loop < totalLoops) {
        var rotation = 0
        var index = loop
        var prev = nums[index]
        var temp = prev
        while (rotation < totalRotationPerLoop) {
            prev = temp
            val tempIndex = (index + step) % size
            temp = nums[tempIndex]
            nums[tempIndex] = prev
            index = tempIndex
            rotation++
        }
        loop++
    }
}

fun main() {
    val nums1 = intArrayOf(1,2,3,4,5,6,7)
    rotate(nums1, 3)
    println(nums1.contentToString())

    val nums2 = intArrayOf(-1,-100,3,99)
    rotate(nums2, 2)
    println(nums2.contentToString())

    val nums3 = intArrayOf(1, 2, 3, 4, 5, 6)
    rotate(nums3, 4)
    println(nums3.contentToString())
}

