# 12/5 Math, BS
# Divide two integers without using multiplication, division and mod operator.
# If it is overflow, return MAX_INT.
# Special Cases:
#   divisor == 0,
#   dividend = -2147483548 (MIN_INT) and divisor = 1


class DivideTwoIntegers(object):
    MAXINT = (1 << 31) - 1

    def has_opposite_sign(self, n1, n2):
        # or use (n1 > 0) ^ (n2 > 0)
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

    # Test on LC - 78ms
    def divide_recursive(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        max_int = (1 << 31) - 1
        min_int = -(1 << 31)
        if divisor == 0 or (dividend == min_int and divisor == -1):
            return max_int

        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        dd, ds = abs(dividend), abs(divisor)
        if ds == 1:
            return sign * dd

        ret = self.divide_helper(dd, ds)
        return ret * sign

    # Note: need to check dd < ds.
    def divide_helper(self, dd, ds):
        if dd == 0 or dd < ds:
            return 0
        ret = 1
        base = ds
        while base + base <= dd:
            base += base
            ret += ret
        dd -= base
        return ret + self.divide_helper(dd, ds)


test = DivideTwoIntegers()
print test.divide(4, 5)
print test.divide(-3, 0)
print test.divide(-2147483648, -1)
print test.divide_bits(-2147483648, -1)
print test.divide_bits(-3, 0)