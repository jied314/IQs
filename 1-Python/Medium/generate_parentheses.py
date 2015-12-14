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
        if m > 0:
            self.add_parenthesis(result, str + ')', n, m-1)
        if n > 0:
            self.add_parenthesis(result, str + '(', n-1, m+1)

    # Test on LeetCode - 52ms
    def generate_parenthesis_dp(self, n):
        result = [['']]
        for i in range(1, n+1):
            str = []
            for j in range(0, i):
                for le in result[j]:
                    for re in result[i-j-1]:
                        str.append('(' + le + ')' + re)
            result.append(str)
        return result[n]

    def generate_parenthesis_error(self, n):
        result = {}
        result[1] = set()
        result[1].add('()')
        for i in range(2, n + 1):
            temp = set()
            previous = result[i-1]
            for e in previous:
                temp.add('()' + e)
                temp.add('(' + e + ')')
                temp.add(e + '()')
            for j in range(2, i/2+1):
                ones = result[j]
                twos = result[i - j]
                for one in ones:
                    for two in twos:
                        temp.add(one + two)
            result[i] = temp
        return list(result[n])



def main():
    test = GenerateParentheses()
    #print test.generate_parenthesis_recursive(4)
    print test.generate_parenthesis_dp(4)


if __name__ == '__main__':
    main()
