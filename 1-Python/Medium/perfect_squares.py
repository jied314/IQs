# 10/5 - DP, BFS, Math
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
# Note:
#   1. DP - find pattern
#   2. use static variables to avoid duplicate calculation
#      static variables can reuse previous results

import sys
import math

class PerfectSquares(object):
    dp = [0]
    # idea: d[i + j * j] = min(d[i + j * j], d[i] + 1)
    # for example: n = 10, i = 1, j = 1, 2, 3,
    # d[2]  = min(d[2],  d[1] + 1),
    # d[5]  = min(d[5],  d[1] + 1),
    # d[10] = min(d[10], d[1] + 1)
    # num_squres for i is already found.
    def num_squares_dp1(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [sys.maxint] * (n + 1)
        dp[0] = 0
        for i in range(0, n + 1):
            max_j = int(math.sqrt(n - i))
            for j in range(1, max_j + 1):
                num = i + j * j
                dp[num] = min(dp[num], dp[i] + 1)
        return dp[n]

    def num_squares_dp2(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [sys.maxint] * (n + 1)
        dp[0] = 0
        for i in range(0, n + 1):
            max_j = int(math.sqrt(i))
            for j in range(1, max_j + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]

    # Test on LeetCode - 300ms
    # use static variables to keep previous results
    def num_squares_static_dp(self, n):
        length = len(self.dp)
        if n < length:
            return self.dp[n]
        for i in range(length, n + 1):
            self.dp.append(sys.maxint)
            max_j = int(math.sqrt(i))
            for j in range(1, max_j + 1):
                self.dp[i] = min(self.dp[i], self.dp[i - j * j] + 1)
        return self.dp[n]

    # 12/25 - revisit
    # Similar idea, not as fast as dp1
    # T(N) = min(T(1) + T(N-1), T(4) + T(N-4), ...
    def num_squares_revisit(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1]
        for i in range(2, n+1):
            val = i
            j = 2
            while j * j <= i:
                sqr = j * j
                val = min(val, i / sqr + dp[i%sqr])
                j += 1
            dp.append(val)
        return dp[-1]

def main():
    test = PerfectSquares()
    print test.num_squares_dp1(12)
    print test.num_squares_dp1(13)
    print test.num_squares_dp2(12)
    print test.num_squares_dp2(13)
    print test.num_squares_static_dp(12)
    print test.num_squares_static_dp(13)
    print test.num_squares_revisit(12)
    print test.num_squares_revisit(13)


if __name__ == '__main__':
    main()
