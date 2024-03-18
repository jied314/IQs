package arrayAndString

import java.math.BigInteger




/**
 * Given two binary strings a and b, return their sum as a binary string.
 *
 * Example 1:
 *     Input: a = "11", b = "1"
 *     Output: "100"
 *
 * Solution:
 * 1. Bit-by-Bit manipulation
 *   Time complexity: O(max(N,M)), where M and N are lengths of the input strings a and b.
 *   Space complexity: O(max(N,M)) to keep the answer.
 *
 * 2. Bit manipulation (XOR, AND) - not use addition (+)
 *   Time complexity: O(max(N,M)), where M and N are lengths of the input strings a and b.
 *   Space complexity: O(max(N,M)) to keep the answer.
 *
 * Example:
 *    a =   [1,1,1,1],
 *    b =   [0,0,1,0],
 *    x = [  1,1,0,1] -> [  1,0,0,1] -> [  0,0,0,1] -> [1,0,0,0,1]
 *    y = [0,0,1,0,0] -> [0,1,0,0,0] -> [1,0,0,0,0] -> [0,0,0,0,0]
 * Code:
 *    while (y != 0) {
 *        x = a ^ b
 *        y = (a & b) << 1 // carry
 *    }
 *    return x
 */

private fun addBinaryBitByBit(a: String, b: String): String {
    val m: Int = a.length
    val n: Int = b.length
    if (m < n) return addBinaryBitByBit(b, a)

    val sb = StringBuilder()
    var carry = 0
    var j = n - 1
    for (i in m-1 downTo 0) {
        if (a[i] == '1') ++carry
        if (j >= 0 && b[j--] == '1') ++carry
        if (carry % 2 == 1) sb.append('1') else sb.append('0')
        carry /= 2
    }
    if (carry == 1) sb.append('1')
    sb.reverse()

    return sb.toString()
}

private fun addBinaryBitManipulation(a: String, b: String): String {
    var x = BigInteger(a, 2)
    var y = BigInteger(b, 2)
    val zero = BigInteger("0", 2)
    var carry: BigInteger
    var answer: BigInteger
    while (y.compareTo(zero) != 0) {
        answer = x.xor(y)
        carry = x.and(y).shiftLeft(1)
        x = answer
        y = carry
    }
    return x.toString(2)
}

fun main() {
    println(addBinaryBitByBit("1111", "0010"))
    println(addBinaryBitManipulation("1111", "0010"))
}
