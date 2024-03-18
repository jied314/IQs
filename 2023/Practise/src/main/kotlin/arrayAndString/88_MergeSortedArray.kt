package arrayAndString

fun mergeOptimal(nums1: IntArray, m: Int, nums2: IntArray, n: Int): Unit {
    var i = m-1
    var j = n-1
    var k = m+n-1

    while (j >= 0 ) { // can only check j since nums1 is already sorted
        if (i >= 0 && nums1[i] > nums2[j]) {
            nums1[k--] = nums1[i--];
        } else {
            nums1[k--] = nums2[j--];
        }
    }
}

fun mergeFirst(nums1: IntArray, m: Int, nums2: IntArray, n: Int): Unit {
    // edge case
    if (n == 0) return
    if (m == 0) { // copy nums2 to nums1
        nums2.forEachIndexed { index, element ->
            nums1[index] = element
        }
        return
    }

    // merge from tail to head
    var i1 = m-1
    var i2 = n-1
    for (i in m+n-1 downTo 0) {
        if (i1 < 0 && i2 >= 0) {
            nums1[i] = nums2[i2]
            i2--
        } else if (i2 < 0 && i1 >= 0) {
            nums1[i] = nums1[i1]
            i1--
        } else {
            if (nums1[i1] >= nums2[i2]) {
                nums1[i] = nums1[i1]
                i1--
            } else {
                nums1[i] = nums2[i2]
                i2--
            }
        }
    }
}

fun main() {
    val nums1 = intArrayOf(1,2,3,0,0,0)
    val nums2 = intArrayOf(2,5,6)
    mergeOptimal(nums1, 1, nums2, 1)

    println(nums1.contentToString())
}