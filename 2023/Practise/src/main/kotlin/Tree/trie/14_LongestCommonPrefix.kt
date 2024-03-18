package Tree.trie

/**
 * Write a function to find the longest common prefix string amongst an array of strings.
 *
 * If there is no common prefix, return an empty string "".
 *
 * Solutions:
 * 1. Horizontal Scanning - find prefix horizontally word by word
 *    Not optimal since it requires comparing all characters.
 *    Time Complexity O(S) where S=M*N - the total number of characters in strs.
 *    Space Complexity O(1)
 *
 * 2. Vertical Scanning - compare the ith char of all strings before moving onto the (i+1)th char
 *    Good when prefix is short and locate at the end of the input
 *    Time Complexity O(S) worst case, O(M*minLength)
 *    Space Complexity O(1)
 *
 * 3. Divide & Conquer - divide into smaller input and find prefix, and then merge
 * 4. Trie - good to use if query often
 */

private fun longestCommonPrefixHorizontal(strs: Array<String>): String {
    if (strs.isEmpty()) return ""
    var prefix = strs[0]
    for (i in 1..<strs.size) {
        // compare prefix
        val next = strs[i]
        var j = 0
        while (j < prefix.length && j < next.length) {
            if (prefix[j] != next[j]) break
            j++
        }
        // update prefix
        prefix = prefix.substring(0, j)
        if (prefix.isEmpty()) return ""
    }
    return prefix
}

fun main() {
    val strs = arrayOf("flower","flow","flight")
    println(longestCommonPrefixHorizontal(strs))
}