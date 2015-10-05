# 10/3 - Math, Bit Manipulation
# Given an integer, write a function to determine if it is a power of two.

class PowerOfTwo(object):
    # Test on LeetCode - 120ms
    def is_power_of_two(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = True
        if n <= 0:
            return False
        while n > 1:
            if n % 2 == 0:
                n >>= 1
            else:
                result = False
                break
        return result

    # Test on LeetCode - 120ms
    # The binary representation of a power-of-two 2y is a 1 followed only by 0s.
    # In such a case, x - 1 generates a binary number where the 1s turn into 0s and the former 0s turn into 1s.
    # For example, 8 = 1000b and 8 - 1 = 7 = 0111b.
    def is_power_of_two_nice(self, n):
        if n <= 0:
            return False
        return n & (n - 1) == 0

def main():
    test = PowerOfTwo()
    print test.is_power_of_two(1)
    print test.is_power_of_two(-16)


if __name__ == "__main__":
    main()