package arrayAndString

/**
 * A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths.
 * The lengths should not have leading zeros.
 */

fun validWordAbbreviation(word: String, abbr: String): Boolean {
    var i = 0
    var j = 0
    while (i < word.length && j < abbr.length) {
        if (word[i] == abbr[j]) { // same
            i++
            j++
        } else {
            if (abbr[j] <= '0' || abbr[j] > '9') return false
            // get number from abbr
            var num = 0
            while (j < abbr.length && abbr[j] - '0' in 0..9) {
                num = 10 * num + (abbr[j++] - '0')
            }
            i += num
        }
    }
    return i == word.length && j == abbr.length
}

fun main() {
    println(validWordAbbreviation("internationalization", "i5a11o1"))
    println(validWordAbbreviation("apple", "a2e"))
    println(validWordAbbreviation("substitution", "sub4u4"))
}