# 10/10 - Bit Manipulation (M)
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range,
# inclusive.
# For example, given the range [5, 7], you should return 4.
# Idea:
#   find the leftmost common digits of m and n
#   e.g. m = 1110111, n = 1110101 => 1110100, but not 1110000
import math
class BitAndOfNumberRanges(object):
    # Test on LeetCode - 584ms
    # Idea:
    #   compare the length of binary format. if not the same, return 0
    #   else, remove the highest bit, and then compare. Recursion.
    #
    def range_bitwise_and(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        bfm = self.binary_format(m)
        bfn = self.binary_format(n)
        return self.compare_binary_format(bfm, bfn)

    # compare each bit of two numbers' binary format
    # if length not the same, return 0;
    # else if the bit is the same, move to the next, and add the current factor
    # e.g. 5 & 7
    #      101 & 111 -> 2^2 + 1 & 11 -> 4
    def compare_binary_format(self, bf1, bf2):
        bf1 = self.remove_starting_0s(bf1)
        bf2 = self.remove_starting_0s(bf2)
        length_bf1, length_bf2 = len(bf1), len(bf2)
        if length_bf1 != length_bf2 or length_bf1 == 0:
            return 0
        else:
            bf1.pop(0)
            bf2.pop(0)
            return (1 << (length_bf1 - 1)) + self.compare_binary_format(bf1, bf2)

    # remove the starting 0s of an array of 0/1s
    def remove_starting_0s(self, bf):
        length = len(bf)
        start_1 = length
        for i in range(0, length):
            if bf[i] == 1:
                start_1 = i
                break
        bf = bf[start_1:]
        return bf

    # decimal to binary
    def binary_format(self, num):
        result = []
        while num > 0:
            result.insert(0, num & 1)
            num >>= 1
        return result

    # Test on LeetCode - 180ms
    # Idea:
    #   Brian Kernighan's Algorithm
    #   n = n & n-1 - help decrease ranges
    #   e.g. n = 7
    #        n = 7 & 6 = 6  (111 & 110 - remove the last bit dif)
    #        n = 6 & 5 = 4  (110 & 101 - remove the mid bit dif)
    def range_bitwise_and_nice1(self, m, n):
        while n > m:
            n &= n-1
        return n

    # Test on LeetCode - 200ms
    # Idea:
    #   if m != n, at least n - m >= 1, remove the last digit
    #   m keeps the base.
    #   e.g. m = 5, n = 7, base = 4
    #        101 & 111 -> 10 & 11 -> 1 & 1 -> 4
    def range_bitwise_and_nice2(self, m, n):
        move_factor = 1
        while m != n:
            m >>= 1
            n >>= 1
            move_factor <<= 1
        return m * move_factor

    # 12/27 - Revisit
    # Test on LeetCode - 196ms
    # Observation:
    #  [4,7] -> 4 go to base 4, -> [0, 3] go to base 0.
    #  [4,8] -> 0, not the same base.
    def range_bitwise_and_revisit(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == n:
            return m
        if m == 0:
            return 0
        log_m, log_n = int(math.log(m, 2)), int(math.log(n, 2))
        if log_m != log_n:
            return 0
        else:
            base = 1 << log_m
            return base + self.range_bitwise_and_revisit(m - base, n - base)

def main():
    test = BitAndOfNumberRanges()
    print test.range_bitwise_and_nice2(0, 0)
    print test.range_bitwise_and_nice2(2, 2)
    print test.range_bitwise_and_nice2(5, 7)
    print test.range_bitwise_and_nice2(10, 18)
    print test.range_bitwise_and_nice2(11, 15)


if __name__ == '__main__':
    main()