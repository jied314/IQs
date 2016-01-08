# 1/3 - Revisit. Bit Manipulation
# Write a function that takes an unsigned integer and returns the number of '1' bits it has
# (also known as the Hamming weight).
# For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011,
# so the function should return 3.

class NumberOf1Bits:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        digits = self.decimal_to_binary(n)
        print digits
        return self.num_1s(digits)

    def decimal_to_binary(self, n):
        digits = []
        while True:
            digit = n % 2
            n /= 2
            if digit is 0 and n is 0:
                break
            digits.insert(0, digit)
        return digits

    def num_1s(self, digits):
        num = 0
        for digit in digits:
            if digit is 1:
                num += 1
        return num

    # Test on LC - 52ms, 45%
    # Note: due to python int range is 64 bits, use 32 to control
    def hamming_weight_revisit(self, n):
        """
        :type n: int
        :rtype: int
        """
        count, loop = 0, 0
        while loop < 32 and n != 0:
            count += n & 1
            n >>= 1
            loop += 1
        return count

    # Test on LC - 48ms, 72%
    # use n & n-1 to eliminate the rightmost '1'
    def hamming_weight_revisit_nice(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            count += 1
            n &= n-1
        return count


# use bit operators to count 1s - slower 60ms
def solution1(n):
    count = 0
    while n != 0:
        if (1 & n) != 0:
            count += 1
        n >>= 1
    return count


# use recursion - faster 48ms
def solution2(n):
    if n > 0:
        return (1 & n) + solution2(n >> 1)
    else:
        return 0


# use bit operator to convert decimal to binary
def d_to_b1(n):
    digits = []
    while n > 0:
        digits.insert(0, 1 & n)
        n >>= 1
    return digits


# use recursion to convert decimal to binary.
# Note: return None for most of Python code
def d_to_b2(n):
    if n > 1:
        temp = d_to_b2(n >> 1)
        temp.append(1 & n)
        return temp
    else:
        return [n]


def main():
    s = NumberOf1Bits()
    n = 11
    #print 'hamming weight of {0} is {1}'.format(n, s.hammingWeight(n))
    #print 'hamming weight of {0} is {1}'.format(n, solution2(n))
    print d_to_b2(n)

if __name__ == '__main__':
    main()