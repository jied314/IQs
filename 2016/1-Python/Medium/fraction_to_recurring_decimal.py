# 12/12 - Hash Table, Math
# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.
# For example,
#   Given numerator = 1, denominator = 2, return "0.5".
#   Given numerator = 2, denominator = 1, return "2".
#   Given numerator = 2, denominator = 3, return "0.(6)".
# Not fully passed
class FractiontoRecurringDecimal(object):

    # Test on LeetCode - 40ms
    # Idea:
    #   compute integral and fractional part
    #   for fractional part, increase value ten times each time and store the position of each numerator
    #   break if a numerator recurs or == 0
    # Note - avoid using list if possible
    #        use string 40ms V.S. use list 54ms
    def fraction_to_decimal(self, numerator, denominator):
        """
            :type numerator: int
            :type denominator: int
            :rtype: str
            """
        # check if 0 is involved
        if numerator == 0:
            return '0'
        if denominator == 0:
            maxint = (1 << 31) - 1
            if numerator > 0:
                return str(maxint)
            else:
                return str(-maxint - 1)
        ret = ""

        # resolve sign
        if (numerator < 0) ^ (denominator < 0):
            ret += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)

        # Division
        # compute the integral part
        quotient, numerator = divmod(numerator, denominator)
        ret += str(quotient)

        # no fraction part, return
        if numerator == 0:
            return ret

        ret += '.'
        numerator_dict = {}

        while numerator != 0:
            # a known numerator
            if numerator in numerator_dict:
                ret = ret[:numerator_dict[numerator]] + '(' + ret[numerator_dict[numerator]:] + ')'
                break
            numerator_dict[numerator] = len(ret)
            numerator *= 10
            quotient, numerator = divmod(numerator, denominator)
            ret += str(quotient)
        return ret


test = FractiontoRecurringDecimal()
print test.fraction_to_decimal(-50, 8)