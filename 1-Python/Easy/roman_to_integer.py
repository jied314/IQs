# Math, String - Roman to Integer
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.
# Note:
# A smaller number in front of a larger number means subtraction, all else means addition.
# 	For example, IV means 4, VI means 6.
# 	You would not put more than one smaller number in front of a larger number to subtract. 
# 	For example, IIV would not mean 3.
# 	You must separate ones, tens, hundreds, and thousands as separate items. That means that 99 is XCIX, 90 + 9, 
# 	but never should be written as IC. Similarly, 999 cannot be IM and 1999 cannot be MIM.
#
class RomanToInteger:
    # @param {string} s
    # @return {integer}
    # Test on LeetCode - 160ms
    def roman_to_int(self, s):
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(0, len(s)):
            current_value = dict[s[i]]
            if i < len(s) - 1:
                next_value = dict[s[i + 1]]
                if current_value < next_value:
                    current_value *= -1
            result += current_value
        return result


def main():
    test = RomanToInteger()
    print test.roman_to_int('IV')
    print test.roman_to_int('VI')
    print test.roman_to_int('XCIX')
    print test.roman_to_int('CMXCIX')
    print test.roman_to_int('MCMXCIX')


if __name__ == '__main__':
    main()