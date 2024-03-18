package arrayAndString

import kotlin.math.max


/**
 * Given a string s, find the length of the longest substring without repeating characters.
 *
 * Example:
 *      Input: s = "abcabcbb"
 *      Output: 3
 *      Explanation: The answer is "abc", with the length of 3.
 *
 * Solutions:
 * 1. Hash - store the index of the last appearance
 *    Time Complexity: O(N)
 *    Space Complexity: O(N)
 * 2. Sliding Window - drop left until no duplicate characters
 *    Time Complexity: O(N)
 *    Space Complexity: O(N)
 */

private fun lengthOfLongestSubstringHash(s: String): Int {
    var result = 0
    var start = -1
    val charIndex = mutableMapOf<Char, Int>()
    for ((i,c) in s.withIndex()) {
        if (charIndex.contains(c)) {
            start = Math.max(charIndex[c]!!, start)
        }
        result = Math.max(result, i-start)
        charIndex[c] = i
    }
    return result
}

fun lengthOfLongestSubstringSlidingWindow(s: String): Int {
    val charCount = mutableMapOf<Char, Int>()
    var left = 0
    var right = 0
    var res = 0
    while (right < s.length) {
        val r = s[right]
        charCount[r] = charCount.getOrDefault(r, 0) + 1
        while (charCount[r]!! > 1) {
            val l = s[left]
            charCount[l] = charCount[l]!! - 1
            left++
        }
        res = Math.max(res, (right - left + 1))
        right++
    }
    return res
}

fun main() {
    println(lengthOfLongestSubstringHash("abba"))
    println(lengthOfLongestSubstringSlidingWindow("abba"))
}