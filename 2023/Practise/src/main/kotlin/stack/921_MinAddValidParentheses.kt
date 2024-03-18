package stack

import kotlin.math.absoluteValue

/**
 * A parentheses string is valid if and only if:
 *
 * It is the empty string,
 * It can be written as AB (A concatenated with B), where A and B are valid strings, or
 * It can be written as (A), where A is a valid string.
 * You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
 *
 * For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
 * Return the minimum number of moves required to make s valid.
 */

fun minAddToMakeValidStack(s: String): Int {
    val stack = ArrayDeque<Char>()
    for (c in s) {
        if (stack.isNotEmpty() && c == ')' && stack.last() == '(') stack.removeLast()
        else stack.add(c)
    }
    return stack.size
}

fun minAddToMakeValidBalance(s: String): Int {
    var open = 0
    var close = 0
    for (c in s) {
        if (c == '(') {
            open++
        } else if (c == ')') {
            if (open > 0) open--
            else close--
        }
    }
    return open.absoluteValue + close.absoluteValue
}