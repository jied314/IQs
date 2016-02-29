# Math, String - String to Integer
# Consider special cases:
# 1. leading and trailing white spaces
# 	2. non-numeric characters
# 	3. sign character
# 	4. integer range
class StringToInteger:
    # @param {string} str
    # @return {integer}
    # Test on LeetCode - 88ms
    def myAtoi(self, str):
        result = 0
        length = len(str)
        if length > 0:
            i = 0
            # read all leading zeroes
            for i in range(0, length):
                if not self.is_space(str[i]):
                    break
            # read characters
            if i < length:
                # read sign if exists
                sign = self.get_sign(str[i])
                if sign is not None:
                    i += 1
                for j in range(i, length):
                    if self.is_numeric(str[j]):
                        result = result * 10 + ord(str[j]) - ord('0')
                    else:
                        break
                if sign is not None:
                    result *= sign
                result = self.check_range(result)
        return result

    def get_sign(self, c):
        if c == '+':
            return 1
        elif c == '-':
            return -1
        else:
            return None

    def is_numeric(self, c):
        return ord('0') <= ord(c) <= ord('9')

    def is_space(self, c):
        return c == ' '

    def check_range(self, num):
        if num > 0 and num > 2147483647:
            return 2147483647
        if num < 0 and num < -2147483648:
            return -2147483648
        return num

    # Test on LeetCode - 72ms
    def myAtoi_overflow(self, str):
        result = 0
        length = len(str)
        if length > 0:
            i = 0
            # read all leading zeroes
            for i in range(0, length):
                if not self.is_space(str[i]):
                    break
            # read characters
            if i < length:
                # read sign if exists
                sign = self.get_sign(str[i])
                if sign is not None:
                    i += 1
                for j in range(i, length):
                    if self.is_numeric(str[j]):
                        if result > 214748364 or (result == 214748364 and (ord(str[j]) - ord('0') >= 8)):
                            return self.process_overflow(result, sign)
                        result = result * 10 + ord(str[j]) - ord('0')
                    else:
                        break
                if sign is not None:
                    result *= sign
        return result

    def process_overflow(self, num, sign):
        if sign == 1 or sign is None:
            return 2147483647
        else:
            return -2147483648


def main():
    test = StringToInteger()
    print test.myAtoi('989 ')
    print test.myAtoi('tutorialspoint1')
    print test.myAtoi(' -1')
    print test.myAtoi('-2147483649')
    print test.myAtoi_overflow('2147483649')


if __name__ == '__main__':
    main()
