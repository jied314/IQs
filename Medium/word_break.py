# 10/17 - Dynamic Programming
# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
#
# For example, given
#   s = "leetcode", dict = ["leet", "code"].
#   Return true because "leetcode" can be segmented as "leet code".
#
# Revisit 12/2
# Note: if the word is in dict, return True.
#       Time Complexity - Use DP
class WordBreak(object):
    # BackTracking/Recursive - Time Complexity not good O(2^N)
    # T(N) = kN + T(N-1) + T(N-2) + ... + T(1) => T(N) - T(N-1) - kN = T(N-2) + ... + T(1)
    # T(N-1) = k(N-1) + T(N-2) + T(N-3) + ... + T(1) => T(N-1) - k(N-1) = T(N-2) + ... + T(1)
    # combine the two => T(N) - T(N-1) - kn = T(N-1) - k(N-1)
    # T(N) = 2T(N-1) + k => O(2^N)
    def word_break_tle(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return False
        return self.check(s, 0, wordDict)

    # Check if the word or its substring exists in dict
    # Backtracking - if s[i:length] not in dict, try s[i:length-1] and so on.
    def check(self, s, start, wordDict):
        length = len(s)
        if start == length:
            return True
        for i in range(length, start, -1):
            substring = s[start: i]
            if substring in wordDict and self.check(s, i, wordDict):
                return True
        return False

    # Test on LeetCode - 64ms
    # DP - dp[i+1] = dp[j] & s[j+1:i+1] in wordDict for 0 <= j <= i
    def word_break_dp(self, s, wordDict):
        if s is None or len(s) == 0:
            return False
        length = len(s)
        dp = [False] * (length + 1)
        dp[0] = True
        for i in range(1, length+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[length]


def main():
    test = WordBreak()
    wordDict = set()
    wordDict.add("leet")
    wordDict.add("code")
    wordDict.add("a")
    wordDict.add("an")
    wordDict.add("gram")
    print test.word_break_dp("leetcode", wordDict)
    print test.word_break_dp("an", wordDict)
    print test.word_break_dp("anagram", wordDict)


if __name__ == "__main__":
    main()
