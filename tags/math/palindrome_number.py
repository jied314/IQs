# Math - Palindrome Number
# Determine whether an integer is a palindrome. Do this without extra space.
# Note: 
# 1. Negative Numbers are not considered as palindrome
# 2. Overflow (check before happening)


class PalindromeNumber:
    # @param {integer} x
    # @return {boolean}
    # Test on LeetCode - 252ms
    # reverse the whole number and then compare.
    def is_palindrome(self, x):
        result = True
        if x < 0:
            result = False
        if x >= 10:
            n = x
            m = 0
            while n > 0:
                digit = n % 10
                if m > 214748364 or (m == 214748364 and digit > 7):
                    return False
                m = m * 10 + digit
                n /= 10
            result = m == x
        return result

    # check until the mid.
    def is_palindrome_mid(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        if x < 10:
            return True

        n = 0
        while x > n:
            n = n * 10 + x % 10
            x /= 10
        return x == n or x == n/10


def main():
    test = PalindromeNumber()
    print test.is_palindrome(214744447412)


if __name__ == '__main__':
    main()