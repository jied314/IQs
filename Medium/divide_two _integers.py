# 12/5 Math, BS
# Divide two integers without using multiplication, division and mod operator.
# If it is overflow, return MAX_INT.
# Special Cases:
#   divisor == 0,
#   dividend = -2147483548 (MIN_INT) and divisor = 1

class DivideTwoIntegers(object):
    MAXINT = (1 << 31) - 1
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 1:
            return dividend
        if dividend == -(DivideTwoIntegers.MAXINT + 1) and divisor == -1 or divisor == 0:
            return DivideTwoIntegers.MAXINT
        is_opposite_sign = self.has_opposite_sign(dividend, divisor)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            level = 1
            base = divisor
            while dividend >= (base + base):
                level += level
                base += base
            dividend -= base
            quotient += level
        if dividend != 0 and is_opposite_sign:
            quotient += 1
        if is_opposite_sign:
            return -quotient
        return quotient

    def has_opposite_sign(self, n1, n2):
        if (n1 > 0 and n2 > 0) or (n1 < 0 and n2 < 0):
            return False
        return True

    # Notes: use to << and >> is accepted
    # Test on LeetCode - 68ms
    def divide_bits(self, dividend, divisor):
        if divisor == 1:
            return dividend
        if dividend == -(DivideTwoIntegers.MAXINT + 1) and divisor == -1 or divisor == 0:
            return DivideTwoIntegers.MAXINT
        quotient = 0
        dd, ds = abs(dividend), abs(divisor)
        while dd >= ds:
            level = 1
            base = ds
            while (base << 1) <= dd:
                level <<= 1
                base <<= 1
            quotient += level
            dd -= base
        if self.has_opposite_sign(dividend, divisor):
            return -quotient
        return quotient


test = DivideTwoIntegers()
print test.divide(4, 5)
print test.divide(-3, 0)
print test.divide(-2147483648, -1)
print test.divide_bits(-2147483648, -1)
print test.divide_bits(-3, 0)