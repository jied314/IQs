# 7/4 - BackTracking, String


class GenerateParentheses:
    # @param {integer} n
    # @return {string[]}
    # From LeetCode Solution:
    # Use two integers to count the remaining left parenthesis (n) and the right parenthesis (m) to be added.
    # At each function call add a left parenthesis if n >0 and add a right parenthesis if m>0.
    # Append the result and terminate recursive calls when both m and n are zero.
    # Test on LeetCode - 64ms
    def generate_parenthesis_recursive(self, n):
        result = []
        self.add_parenthesis(result, '', n, 0)
        return result

    def add_parenthesis(self, result, str, n, m):
        if m == 0 and n == 0:
            result.append(str)
            return
        if n > 0:
            self.add_parenthesis(result, str + '(', n-1, m+1)
        if m > 0:
            self.add_parenthesis(result, str + ')', n, m-1)

    # Test on LeetCode - 52ms
    def generate_parenthesis_dp(self, n):
        dp = [['']]
        for i in range(1, n+1):
            temp = []
            for j in range(0, i):
                for le in dp[j]:
                    for re in dp[i-j-1]:
                        temp.append('(' + le + ')' + re)
            dp.append(temp)
        return dp[n]


def main():
    test = GenerateParentheses()
    print test.generate_parenthesis_recursive(4)
    print test.generate_parenthesis_dp(4)

if __name__ == '__main__':
    main()
