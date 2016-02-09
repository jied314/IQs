# 1/16 - DP
# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty
# substrings recursively.
# Below is one possible representation of s1 = "great":
#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#           / \
#          a   t
# To scramble the string, we may choose any non-leaf node and swap its two children.
# For example, if we choose the node "gr" and swap its two children,
# it produces a scrambled string "rgeat".
#      rgeat
#     /    \
#    rg    eat
#   / \    /  \
#  r   g  e   at
#            / \
#           a   t
# We say that "rgeat" is a scrambled string of "great".
# Similarly, if we continue to swap the children of nodes "eat" and "at",
# it produces a scrambled string "rgtae".
#        rgtae
#       /    \
#     rg    tae
#    / \    /  \
#   r   g  ta  e
#         / \
#        t   a
# We say that "rgtae" is a scrambled string of "great".
#
# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
# Note:
#   scramble string is different from permutations of the string
#   once the string is partitioned, it cannot be repartitioned
#   e.g. ABCDE & CADBE -> False


class Solution(object):
    # Test on LC - 68ms, 83%
    # Idea:
    #   recursively checking split at pos 1...length
    def is_scramble_recursive(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        length = len(s1)
        # split string at pos 1 to length-1, check the two split part.
        # note reverse string also needs to be checked
        for i in range(1, length):
            # check regular split
            if self.is_scramble_recursive(s1[:i], s2[:i]) and self.is_scramble_recursive(s1[i:], s2[i:]):
                return True
            # check reversed split
            if self.is_scramble_recursive(s1[:i], s2[length-i:]) and self.is_scramble_recursive(s1[i:], s2[:length-i]):
                return True
        return False

    # DP - TLE
    # dp[i][j][l] means whether s2[j:j+l] is a scrambled string of s1[i:i+l] or not
    def is_scramble_dp(self, s1, s2):
        length = len(s1)
        dp = [[[False] * 100 for _ in range(100)] for __ in range(100)]
        for i in range(length-1, -1, -1):
            for j in range(length-1, -1, -1):
                dp[i][j][1] = s1[i] == s2[j]
                for l in range(2, min(length-i, length-j)+1):
                    for n in range(1, l):
                        dp[i][j][l] |= dp[i][j][n] and dp[i+n][j+n][l-n]
                        dp[i][j][l] |= dp[i][j+l-n][n] and dp[i+n][j][l-n]
        return dp[0][0][length]

test = Solution()
print test.is_scramble_recursive("great", "rgtae")
print test.is_scramble_dp("great", "rgtae")
print test.is_scramble_dp("abcd", "bcda")