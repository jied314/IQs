# 7/2 - Math, String
# Given an integer, convert it to a roman numeral.
# Input is guaranteed to be within the range from 1 to 3999.
# Note:
#   easy code can be more time consuming


import collections

class IntegerToRoman:
    # @param {integer} num
    # @return {string}

    # Test on LeetCode - 176ms
    def int_to_roman(self, num):
        result = []
        roman_dict = {1: ['I', 'V', 'X'], 2: ['X', 'L', 'C'], 3: ['C', 'D', 'M'], 4: ['M']}
        loop = 1
        while num > 0:
            romans = []
            roman_candidates = roman_dict[loop]
            digit = num % 10
            base = 0
            small = roman_candidates[0]
            flag = 4

            if loop < 4:  # adjust for thousands
                big = roman_candidates[1]

            if digit >= 5:  # adjust base, big and flag
                base = 5
                big = roman_candidates[2]
                flag = 9

            if digit < flag:  # 1 - 3, 6 - 8
                if base > 0:
                    romans.append(roman_candidates[1])
                while digit > base:
                    romans.append(small)
                    digit -= 1
            else:
                romans = [small, big]
            result = romans + result
            num /= 10
            loop += 1
        return ''.join(result)

    # Test on LeetCode - 384ms
    def int_to_roman_nice(self, num):
        numToRoman = collections.OrderedDict()
        numToRoman[1000] = 'M'
        numToRoman[900] = 'CM'
        numToRoman[500] = 'D'
        numToRoman[400] = 'CD'
        numToRoman[100] = 'C'
        numToRoman[90] = 'XC'
        numToRoman[50] = 'L'
        numToRoman[40] = 'XL'
        numToRoman[10] = 'X'
        numToRoman[9] = 'IX'
        numToRoman[5] = 'V'
        numToRoman[4] = 'IV'
        numToRoman[1] = 'I'
        return self.convert(num, numToRoman)

    def convert(self, num, map):
        for key in map.keys():
            if num >= key:
                return map[key] + self.convert(num - key, map)
        return ''

    # Test on LC - 140ms, 35%
    # Subtract values and print roman letters.
    # Same idea as above.
    def int_to_roman_conditions(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            return ""
        ret = []
        while num > 0:
            if num >= 1000:
                ret.append("M")
                num -= 1000
            elif num >= 900:
                ret.append("CM")
                num -= 900
            elif num >= 500:
                ret.append("D")
                num -= 500
            elif num >= 400:
                ret.append("CD")
                num -= 400
            elif num >= 100:
                ret.append("C")
                num -= 100
            elif num >= 90:
                ret.append("XC")
                num -= 90
            elif num >= 50:
                ret.append("L")
                num -= 50
            elif num >= 40:
                ret.append("XL")
                num -= 40
            elif num >= 10:
                ret.append("X")
                num -= 10
            elif num == 9:
                ret.append("IX")
                num -= 9
            elif num >= 5:
                ret.append("V")
                num -= 5
            elif num == 4:
                ret.append("IV")
                num -= 4
            else:
                ret.append("I")
                num -= 1
        return "".join(ret)

def main():
    test = IntegerToRoman()
    print test.int_to_roman(399)
    print test.int_to_roman(1000)
    print test.int_to_roman(5)

    print test.int_to_roman_nice(399)
    print test.int_to_roman_nice(1000)
    print test.int_to_roman_nice(5)


if __name__ == '__main__':
    main()