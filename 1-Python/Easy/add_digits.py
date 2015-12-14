# 9/9 - Math
# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
# For example:
#   Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
#   Could you do it without any loop/recursion in O(1) runtime?
#   check Wiki - https://en.wikipedia.org/wiki/Digital_root
# Idea:
#   the digital root of a positive integer as the position it holds with respect to the largest multiple of 9
# less than it.

class AddDigits(object):
    def add_digits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return num
        if num % 9 == 0:
            return 9
        return num % 9


