package stack

import kotlin.math.absoluteValue

/**
 * Given a string s of '(' , ')' and lowercase English characters.
 *
 * Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that
 * the resulting parentheses string is valid and return any valid string.
 *
 * Formally, a parentheses string is valid if and only if:
 *      It is the empty string, contains only lowercase characters, or
 *      It can be written as AB (A concatenated with B), where A and B are valid strings, or
 *      It can be written as (A), where A is a valid string.
 *
 * Solutions:
 * 1. Stack + String Builder
 * 2. Two passes String Builder
 */

fun minRemoveToMakeValidStack(s: String): String {
    // store invalid parentheses
    val deque = ArrayDeque<Pair<Int, Char>>()
    for ((i,c) in s.withIndex()) {
        if (c == '(' || c == ')') {
            if (deque.isNotEmpty() && isValidPair(deque.last().second, c)) {
                deque.removeLast()
            } else {
                deque.add(Pair(i, c))
            }
        }
    }

    // remove invalid parentheses
    val sb = StringBuilder()
    for (i in s.indices) {
        if (deque.isNotEmpty() && i == deque.first().first) {
            deque.removeFirst()
        } else {
            sb.append(s[i])
        }
    }
    return sb.toString()
}

private fun isValidPair(c1: Char, c2: Char): Boolean {
    return c1 == '(' && c2 == ')'
}

fun minRemoveToMakeValidStringBuilder(s: String): String {
    // Pass 1: Remove all invalid ")"
    val sb = java.lang.StringBuilder()
    var openSeen = 0
    var balance = 0
    for (c in s) {
        if (c == '(') {
            openSeen++
            balance++
        }
        if (c == ')') {
            if (balance == 0) continue
            balance--
        }
        sb.append(c)
    }

    // Pass 2: Remove the rightmost "("
    val result = java.lang.StringBuilder()
    var openToKeep = openSeen - balance
    for (c in sb) {
        if (c == '(') {
            openToKeep--
            if (openToKeep < 0) continue
        }
        result.append(c)
    }
    return result.toString()
}

fun main() {
    println(minRemoveToMakeValidStack("lee(t(c)o)de)"))
    println(minRemoveToMakeValidStringBuilder("lee(t(c)o)de)"))

    println(minRemoveToMakeValidStack("a)b(c)d"))
    println(minRemoveToMakeValidStringBuilder("a)b(c)d"))

    println(minRemoveToMakeValidStack("))(("))
    println(minRemoveToMakeValidStringBuilder("))(("))
}
