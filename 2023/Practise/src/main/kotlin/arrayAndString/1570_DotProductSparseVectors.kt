package arrayAndString

/**
 * Given two sparse vectors, compute their dot product.
 *
 * Implement class SparseVector:
 *      SparseVector(nums) Initializes the object with the vector nums
 *      dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
 *      A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently
 *      and compute the dot product between two SparseVector.
 *
 * Follow up: What if only one of the vectors is sparse?
 */

class SparseVector(nums: IntArray) {

    private val values = mutableListOf<Pair<Int, Int>>()
    init {
        for ((i, num) in nums.withIndex()) {
            if (num != 0) values.add(Pair(i, num))
        }
    }

    // Return the dotProduct of two sparse vectors
    fun dotProduct(vec: SparseVector): Int {
        var result = 0
        var i = 0
        var j = 0
        while (i < values.size && j < vec.values.size) {
            if (values[i].first == vec.values[j].first) {
                result += values[i++].second * vec.values[j++].second
            } else if (values[i].first < vec.values[j].first) {
                i++
            } else {
                j++
            }
        }
        return result
    }
}

fun main() {
    val v1 = SparseVector(intArrayOf(1,0,0,2,3))
    val v2 = SparseVector(intArrayOf(0,3,0,4,0))
    println(v1.dotProduct(v2))
}