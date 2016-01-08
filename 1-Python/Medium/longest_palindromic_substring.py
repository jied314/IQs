# 1/7 - Revisit String
# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000,
# and there exists one unique longest palindromic substring.
#
# Idea:
#   Palindromes are made up of smaller palindromes. So, a palindrome of length 100 (for example), will have a
# palindrome of length 98 inside it, and one of length 96, ... 50, ... 4, and 2.
class LongestPalindromicSubstring(object):
    # TLE - Time Complexity O(N^3)
    def longest_palindrome_tle(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return ''
        length = len(s)
        if length == 1:
            return s

        char_dict = {}
        candidate = ""
        for i in range(0, length):
            c = s[i]
            if c not in char_dict:
                char_dict[c] = []
            for prev_pos in char_dict[c]:
                if self.is_palindrome(s[prev_pos+1:i]):
                    if i-prev_pos+1 > len(candidate):
                        candidate = s[prev_pos: i+1]
                    break
            char_dict[c].append(i)
        return candidate

    # Time Complexity - O(N)
    def is_palindrome(self, s):
        if len(s) > 1:
            start, end = 0, len(s) - 1
            while start < end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    return False
        return True

    # Idea:
    # S(n) is the longest palindrome for substring of s with indices from 0 to n
    # string(i,l) is a substring of s where i is the start index and l is the length
    # if S(n-1) = string(i, l)
    # then S(n) = string(n-l, l+1), string(n-l-1, l+2), S(n-1)
    def longest_palindrome_nice(self, s):
        longest_starting_index = 0
        max_length = 0
        for i in xrange(len(s)):
            if self.is_palindrome1(s, i - max_length, i):  # check string(n-l, l+1)
                longest_starting_index = i - max_length
                max_length += 1
            # check string(n-l-1, l+2)
            elif i - max_length - 1 >= 0 and self.is_palindrome1(s, i - max_length - 1, i):
                longest_starting_index = i - max_length - 1
                max_length += 2
        return s[longest_starting_index:longest_starting_index + max_length]

    def is_palindrome1(self, s, start, end):
        if start == end:
            return True
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

    # Adapted from Yanxing - DP
    # Still TLE - But faster then naive version.
    # Time - O(N^2), Memory - O(N^2)
    # similar idea: build from smaller unit, length = 1, 2, 3, ...
    def longest_palindrome_dp(self, s):
        n = len(s)
        begin, max_len = 0, 1
        dp = [[False] * n for _ in range(n)]
        # length = 1
        for i in range(0, n):
            dp[i][i] = True
        # length = 2
        for i in range(0, n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                begin = i
                max_len = 2
        # length = 3...n
        for length in range(3, n+1):
            for i in range(0, n-length+1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    begin = i
                    max_len = length
        return s[begin:begin+max_len]


def main():
    test = LongestPalindromicSubstring()
    print test.longest_palindrome_dp("ccaabbaac")


if __name__ == "__main__":
    main()

