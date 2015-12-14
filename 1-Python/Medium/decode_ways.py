# 12/4 - DP, String
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#   'A' -> 1
#   'B' -> 2
#   ...
#   'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
# For example,
#   Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#   The number of ways decoding "12" is 2.
#
# Solution:
#   T(N) = T(N-1). if s[i-1:i+1] valid, add T(N-2)
#
# Note:
#   invalid encoding - return 0
#   e.g. "", "0", "1200", "30" -> 0
class DecodeWays(object):
    # Test on LeetCode - 56ms
    def num_decodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0

        length = len(s)
        dp = [0] * (length + 1)
        dp[0] = 1

        if self.is_valid_encoding(0, s):
            dp[1] = 1
        else:
            return 0

        for i in range(1, length):
            if not self.is_valid_encoding(i, s):
                return 0
            if s[i] == '0':  # use T(N-2)
                dp[i + 1] = dp[i - 1]
            else:
                dp[i + 1] = dp[i]  # use T(N-1)
                if s[i-1] != '0' and s[i - 1:i + 1] < '27':
                    dp[i + 1] += dp[i - 1]
        return dp[-1]

    # check if s[i] is valid
    # s[i] has to be a number. if s[i] == '0', s[i-1]
    def is_valid_encoding(self, i, s):
        digit = s[i]
        if '0' < digit <= '9' or (digit == '0' and i > 0 and '0' < s[i-1] < '3'):
            return True
        return False

    # Test on LeetCode - 44ms
    # Backward, avoid condition checking
    def num_decodings_backward(self, s):
        if s is None or len(s) == 0:
            return 0

        length = len(s)
        dp = [0] * (length + 1)
        dp[length] = 1

        for i in range(length, -1, -1):
            if s[i] == '0':
                continue
            dp[i] = dp[i+1]
            if i < length-1 and (s[i] == '1' or (s[i] == '2' and s[i+1] < '7')):
                dp[i] += dp[i+2]
        return dp[0]


test = DecodeWays()
print test.num_decodings('101')