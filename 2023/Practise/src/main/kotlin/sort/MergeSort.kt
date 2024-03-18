package sort

private fun sortArray(nums: IntArray): IntArray {
    return mergeSort(nums, 0, nums.size-1)
}

private fun mergeSort(nums: IntArray, start: Int, end: Int): IntArray {
    if (start == end) return intArrayOf(nums[start])
    if (start > end) return IntArray(0)

    val mid = start + (end-start)/2
    val sortedLeft = mergeSort(nums, start, mid)
    val sortedRight = mergeSort(nums, mid+1, end)
    return merge(sortedLeft, sortedRight)
}

// merge two sorted arrays into one
private fun merge(nums1: IntArray, nums2: IntArray): IntArray {
    val lSize = nums1.size
    val rSize = nums2.size
    val sorted = IntArray(lSize + rSize)
    var ls = 0
    var rs = 0
    while (ls < lSize && rs < rSize) {
        if (nums1[ls] <= nums2[rs]) {
            sorted[ls+rs] = nums1[ls++]
        } else {
            sorted[ls+rs] = nums2[rs++]
        }
    }
    while (ls < lSize) {
        sorted[ls+rs] = nums1[ls++]
    }
    while (rs < rSize) {
        sorted[ls+rs] = nums2[rs++]
    }
    return sorted
}

fun main() {
    val nums = intArrayOf(1, 10, 4, 3, 15, 4, 8)
    println(sortArray(nums).contentToString())
}
