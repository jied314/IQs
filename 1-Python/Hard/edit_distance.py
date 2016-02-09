# 1/15 - DP
# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
# (each operation is counted as 1 step.)
# You have the following 3 operations permitted on a word:
#   a) Insert a character
#   b) Delete a character
#   c) Replace a character
# Idea:
#   M*N space, dp[i][j] is the min distance of matching w1[:i] to w2[:j]
#   if w1[i-1] == w2[j-1], dp[i][j] = dp[i-1][j-1]
#   else dp[i][j] = min(insert, delete, replace)


class Solution(object):
    # Test on LC - 292ms, 62%
    # Space Complexity - O(M*N)
    def min_distance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1, w2 = word1.lower(), word2.lower()
        l1, l2 = len(w1), len(w2)
        dp = [[0] * (l2+1) for _ in range(l1+1)]
        for j in range(1, l2+1):
            dp[0][j] = j
        for i in range(1, l1+1):
            dp[i][0] = i
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if w1[i-1] == w2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    insert = dp[i][j-1] + 1  # add after w1[i-1]
                    delete = dp[i-1][j] + 1  # delete w1[i-1]
                    replace = dp[i-1][j-1] + 1
                    dp[i][j] = min(insert, delete, replace)
        return dp[l1][l2]

    # Test on LC - 280ms, 76%
    # Space Complexity - O(N)
    # Notice we only need three values for each new dp[i][j], we can reduce space consumption by just recording
    # dp values of the previous row and the current and previous value.
    def min_distance_nice(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1, w2 = word1.lower(), word2.lower()
        l1, l2 = len(w1), len(w2)
        dp = [i for i in range(0, len(w2)+1)]
        for i in range(1, l1+1):
            pre = i
            for j in range(1, l2+1):
                if w1[i-1] == w2[j-1]:
                    cur = dp[j-1]
                else:
                    insert = pre + 1  # add after w1[i-1]
                    delete = dp[j] + 1  # delete w1[i-1]
                    replace = dp[j-1] + 1
                    cur = min(insert, delete, replace)
                dp[j-1] = pre
                pre = cur
            dp[-1] = pre
        return dp[-1]

test = Solution()
print test.min_distance("ab", "bc")
print test.min_distance_nice("ab", "bc")