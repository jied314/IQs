# 1/14 - DP
# Given a string S and a string T, count the number of distinct sub-sequences of T in S.
# A sub-sequence of a string is a new string which is formed from the original string by deleting some
# (can be none) of the characters without disturbing the relative positions of the remaining characters.
# (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
# Here is an example:
#   S = "rabbbit", T = "rabbit", Return 3.
#
# Not understand the solution
# Solution:
# We keep a m*n matrix and scanning through string S, while m = T.length() + 1 and n = S.length() + 1
# each cell in matrix Path[i][j] means the number of distinct sub-sequences of T.substr(1...i) in S(1...j)
#
# Path[i][j] = Path[i][j-1]            (discard S[j])
#              +     Path[i-1][j-1]    (S[j] == T[i] and we are going to use S[j])
#                 or 0                 (S[j] != T[i] so we could not use S[j])
# while Path[0][j] = 1 and Path[i][0] = 0.


class Solution(object):
    # Test on LC - 180ms, 77%
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        len_t, len_s = len(t), len(s)
        if len_t > len_s:
            return 0
        path = [[0] * (len_s+1) for _ in range(len_t+1)]
        for k in range(0, len_s+1):
            path[0][k] = 1
        for i in range(1, len_t+1):
            for j in range(1, len_s+1):
                path[i][j] = path[i][j-1]
                if t[i-1] == s[j-1]:
                    path[i][j] += path[i-1][j-1]
        return path[len_t][len_s]

test = Solution()
print test.numDistinct("rabbbit", "rabbit")