# 1/13 - BackTracking (DFS)
# Follow up for N-Queens problem.
#   Now, instead outputting board configurations, return the total number of distinct solutions.


class Solution(object):
    # Test on LC - 152ms, 45%
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        self.queens(n, 0, [0] * n)
        return self.count

    # only need one col, keep updating its values.
    def queens(self, n, i, col):
        if i == n:
            self.count += 1
        else:
            for j in range(0, n):
                if self.is_promising(i, j, col):
                    col[i] = j
                    self.queens(n, i+1, col)
        
    def is_promising(self, i, j, col):
        k = 0
        flag = True
        while k < i and flag:
            if col[k] == j or i - k == abs(j - col[k]):
                flag = False
            k += 1
        return flag

test = Solution()
print test.totalNQueens(4)