# 10/1 - Math (Easy), not understand the question correctly
# Write a program to check whether a given number is an ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
# Note that 1 is typically treated as an ugly number.

class UglyNumber(object):
    # Test on LeetCode - 68ms
    def is_ugly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        prime_factors = [2, 3, 5]
        for p in prime_factors:
            while num % p == 0:
                num /= p
        return num == 1


def main():
    test = UglyNumber()
    print test.is_ugly(3)
    print test.is_ugly(14)
    lst = []
    for i in range(65, 128):
        if test.is_ugly(i):
            lst.append(i)
    print len(lst)
    print lst


if __name__ == '__main__':
    main()
