# 12/28 - DP
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.
# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.


class Solution(object):
    # find the number of minimum cut (partitions)
    # Not knowing why not pass
    def min_cut(self, s):
        length = len(s)
        cut = [0] * (length + 1)  # number of cuts for the first k characters
        for i in range(0, length+1):
            cut[i] = i-1
        for i in range(0, length):
            for j in range(0, i+1):  # odd length palindrome
                if i + j < length and s[i-j] == s[i+j]:
                    cut[i+j+1] = min(cut[i+j+1], 1+cut[i-j])
            for j in range(1, i+2):  # even length palindrome
                if i + j < length and s[i-j+1] == s[i+j]:
                    cut[i+j+1] = min(cut[i+j+1], 1+cut[i-j+1])
        return cut[length]

    # Not knowing why not pass
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 1:
            return 0
        record = [[False] * length for i in range(0, length)]
        for i in range(0, length):  # length-1
            for j in range(0, length-i):  # start position
                end = j + i
                if s[j] == s[end]:
                    if i < 4 or record[j+1][end-1]:
                        record[j][end] = True

        dp = [0] * (length+1)

        for i in range(1, length+1):
            dp[i] = i
            for j in range(1, i+1):
                if record[j-1][i-1]:
                    if j == 1:
                        dp[i] = 0
                    else:
                        dp[i] = min(dp[i], dp[j-1]+1)
        return dp[length]

test = Solution()
print test.min_cut("aab")
print test.minCut("aab")

