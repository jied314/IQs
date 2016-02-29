# 2/19 - Stack, String - Easy
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


class Solution(object):
    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if str is None or len(s) < 2:
            return False

        stack = []
        for i in range(0, len(s)):
            if s[i] in ("(", "{", "["):
                stack.append(s[i])
            else:
                if len(stack) > 0 and ((s[i] == ")" and stack[-1] == "(") or (s[i] == "}" and stack[-1] == "{") or
                                           (s[i] == "]" and stack[-1] == "[")):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


test = Solution()
print test.is_valid("{}][}}{[))){}{}){(}]))})[({")