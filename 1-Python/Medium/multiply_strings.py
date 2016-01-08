# 10/22 - Math, String (M)
# Given two numbers represented as strings, return multiplication of the numbers as a string.
# Note: The numbers can be arbitrarily large and are non-negative.
# Fail on first trial


class MultiplyStrings(object):
    # Test on LeetCode - 456ms
    # Idea:
    #   123 * 456 = 3 * 456 + 20 * 456 + 100 * 456
    #               1368
    #               912
    #              456  +
    #            ------------
    #              56088
    # Note: the final result should exclude leading 0s if any.
    def multiply_nice(self, num1, num2):
        l1, l2 = len(num1), len(num2)
        if l1 == 0 or l2 == 0:
            return 0
        l3 = l1 + l2
        sums = ["0" for i in range(0, l3)]
        for i in range(l1-1, -1, -1):
            carry = 0
            digit1 = int(num1[i])
            if digit1 == 0:
                continue
            for j in range(l2-1, -1, -1):
                digit2 = int(num2[j])
                original = int(sums[i + j + 1])
                temp = original + digit1 * digit2 + carry
                carry, mod = divmod(temp, 10)
                sums[i + j + 1] = str(mod)
            if carry > 0:
                sums[i] = str(int(sums[i]) + carry)

        start = -1
        for i in range(0, l3):
            if sums[i] != "0":
                start = i
                break
        if start == -1:
            return "0"
        return "".join(sums[start:])

    # Idea:
    #   slice num into (a + b + ...) * (d + e + ...)
    #   product = ad + ae + bd + be + ...
    #   ad, ae ... are small enough to do direct multiplication.
    #   do addition is easy.
    # Not very elegant. Not finished.
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        """if num1 is None or len(num1) < 1 or num2 is None or len(num2) < 1:
            return ""
        if len(num1) + len(num2) < 9:
            return int(num1) * int(num2)"""
        substrings1 = self.divide_string(num1)
        substrings2 = self.divide_string(num2)
        products = []
        for s1 in substrings1:
            for s2 in substrings2:
                products.append(self.string_multiply(s1, s2))
        """ret = products[0]
        length = len(products)
        for i in range(1, length):
            ret = self.string_add(ret, products[i])
        return ret.get_full_str()"""
        return products

    def divide_string(self, num):
        length = len(num)
        div, mod = divmod(length, 5)
        ret = []
        start, base = 0, length
        for i in range(0, div):
            string = num[start: start+5]
            str_val = int(string)
            if str_val == 0:
                start += 5
                continue
            string = str(str_val)
            base -= 5
            #ret.append([string, base])
            ret.append(StringNumber(string, base))
            start += 5
        if mod != 0:
            string = num[start:]
            ret.append(StringNumber(string, 0))
            #ret.append([string, 0])
        return ret

    def string_multiply(self, str_num1, str_num2):
        new_str = int(str_num1.string) * int(str_num2.string)
        new_base = str_num1.base + str_num2.base
        return [new_str, new_base]
        #return StringNumber(new_str, new_base)

    def string_add(self, one, another):
        l1, l2 = len(one), len(another)
        length = max(l1, l2)
        ret = []
        carry = 0
        for i in range(1, length + 1):
            if i > l1:
                d1 = 0
            else:
                d1 = int(one[l1 - i])
            if i > l2:
                d2 = 0
            else:
                d2 = int(another[l2 - i])
            carry, mod = divmod(d1 + d2 + carry, 10)
            ret.insert(0, str(mod))
        return "".join(ret)


class StringNumber(object):
    def __init__(self, string, base):
        self.string = string
        self.base = base

    def get_full_str(self):
        full_str = self.string
        for i in range(0, self.base):
            full_str += "0"
        return full_str

def main():
    test = MultiplyStrings()
    print test.multiply_nice("12", "308")
    print test.multiply_nice("0", "0")
    #print test.string_add("0001239", "456000")



if __name__ == '__main__':
    main()

