# Math - Factorial Trailing Zeroes
# Given an integer n, return the number of trailing zeroes in n!.
#
class FactorialTrailingZeroes:
    # @param {integer} n
    # @return {integer}
    # Test on LeetCode - 52ms
    def trailing_zeroes(self, n):
        result = 0
        i = 5
        while n / i > 0:
            result += n / i
            i *= 5
        return result

    # Test on LeetCode - 60ms
    def trailing_zeroes_nice(self, n):
        result = 0
        while n > 0:
            n /= 5
            result += n
        return result

def main():
    test = FactorialTrailingZeroes()
    print test.trailing_zeroes_nice(100)

if __name__ == '__main__':
    main()