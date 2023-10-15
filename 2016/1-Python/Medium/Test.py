class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

import copy
import sys
import math
from collections import deque
import re
import lib

class Solution:
    """def calculate(self, s):

        :type s: str
        :rtype: int

        if s is None or len(s) == 0:
            return 0
        open_paren_pos = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                open_paren_pos.append(i)
            elif s[i] == ')':
                open_pos = open_paren_pos.pop()
                local_eval = self.eval(s, open_pos+1, i-1)
                if local_eval > 0 and prev_opt
                    s = s[:open_pos] + str(local_eval) + s[i+1:]
                else:

                i = open_pos + 1
            i += 1
        return self.eval(s, 0, len(s)-1)

    def eval(self, s, start, end):
        ss = s[start:end+1]
        opds = re.findall(r'\d+', ss)
        for i in range(0, len(opds)):
            opds[i] = int(opds[i])
        opts = re.findall(r'[\+\-]', ss)
        ret = opds[0]
        for i in range(0, len(opts)):
            ret = self.do_arithmetic(opts[i], ret, opds[i+1])
        return ret

    def do_arithmetic(self, opt, opd1, opd2):
        if opt == '+':
            ret = opd1 + opd2
        else:
            ret = opd1 - opd2
        return ret

    def multiply(self, num1, num2):

        :type num1: str
        :type num2: str
        :rtype: str

        # make sure len(num1) >= len(num2)
        nl1, nl2 = self.convert_string_to_list(num1), self.convert_string_to_list(num2)
        if len(nl2) > len(nl1):
            nl1, nl2 = nl2, nl1

        length2 = len(nl2)
        ret = self.single_multiply(nl1, nl2[-1])
        for i in range(length2-2, -1, -1):
            single_product = self.single_multiply(nl1, nl2[i])
            trailing_zeroes = [0] * (length2 - i - 1)
            single_product = trailing_zeroes + single_product
            ret = self.add(ret, single_product)

        if ret[0] == 0 and ret[-1] == 0:
            i = 0
            while ret:
                if ret[i] == 0:
                    ret.pop()
                else:
                    break
        if not ret:
            return '0'
        for i in range(0, len(ret)):
            ret[i] = str(ret[i])
        ret.reverse()
        return ''.join(ret)

    # list of digits addition, note l1 and l2 are reverse order
    def add(self, l1, l2):
        carry = 0
        len1, len2 = len(l1), len(l2)
        ret = []
        for i in range(0, max(len1, len2)):
            if i >= len1:
                d1 = 0
            else:
                d1 = l1[i]
            if i >= len2:
                d2 = 0
            else:
                d2 = l2[i]
            single_sum = d1 + d2 + carry
            ret.append(single_sum % 10)
            carry = single_sum / 10
        if carry != 0:
            ret.append(carry)
        return ret

    # perform a large string multiplied by a single digit
    # return a list of digit
    def single_multiply(self, num, digit):
        if digit == 0:
            return [0] * len(num)
        if digit == 1:
            ret = list(num)
            ret.reverse()
            return ret
        ret = []
        carry = 0
        for i in range(len(num)-1, -1, -1):
            temp = digit * num[i] + carry
            ret.append(temp % 10)
            carry = temp / 10
        if carry != 0:
            ret.append(carry)
        return ret

    def convert_string_to_list(self, num):
        nl = list(num)
        for i in range(0, len(nl)):
            nl[i] = int(nl[i])
        return nl"""


    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            return ""
        ret = []
        while num > 0:
            if num > 1000:
                ret.append("M")
                num -= 1000
            elif num > 900:
                ret.append("CM")
                num -= 900
            elif num > 500:
                ret.append("D")
                num -= 500
            elif num > 400:
                ret.append("CD")
                num -= 400
            elif num > 100:
                ret.append("C")
                num -= 100
            elif num > 90:
                ret.append("XC")
                num -= 90
            elif num > 50:
                ret.append("L")
                num -= 50
            elif num > 40:
                ret.append("XL")
                num -= 40
            elif num > 10:
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

test = Solution()
print test.intToRoman(6)
