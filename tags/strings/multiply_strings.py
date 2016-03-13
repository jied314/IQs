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

    # Revisit - 2/29
    # Test on LC - 344ms, 50%
    # Idea:
    #   123 * 456 = 1 * 456 * 100 + 2 * 456 * 10 + 3 * 456
    #   Use int array for efficiency
    def multiply_revisit(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 is None or num2 is None or len(num1) == 0 or len(num2) == 0:
            return "0"
        if len(num1) < len(num2):  # num1 is longer
            num1, num2 = num2, num1
        ret = []
        lst1 = [int(e) for e in num1]

        for digit in num2:
            temp = self.list_num_multiply(lst1, int(digit))
            ret.append(0)
            ret = self.list_num_add(ret, temp)
        return str(int("".join([str(e) for e in ret])))

    def list_num_add(self, lst1, lst2):
        ret = []
        length1 = len(lst1)
        length2 = len(lst2)
        length = max(length1, length2)
        carry = 0
        for i in range(0, length):
            sum = carry
            if i < length1:
                sum += lst1[length1-1-i]
            if i < length2:
                sum += lst2[length2-1-i]
            carry, digit = divmod(sum, 10)
            ret.append(digit)
        if carry != 0:
            ret.append(carry)
        ret.reverse()
        return ret

    def list_num_multiply(self, lst, num):
        ret = []
        carry = 0
        for i in range(len(lst)-1, -1, -1):
            sum = carry + num * lst[i]
            carry, digit = divmod(sum, 10)
            ret.append(digit)
        if carry != 0:
            ret.append(carry)
        ret.reverse()
        return ret


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


if __name__ == '__main__':
    main()

