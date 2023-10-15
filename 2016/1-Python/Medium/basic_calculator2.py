# 10/24 - String
# Implement a basic calculator to evaluate a simple expression string.
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
# The integer division should truncate toward zero.
# You may assume that the given expression is always valid.
# Some examples:
#   "3+2*2" = 7
#   " 3/2 " = 1
#   " 3+5 / 2 " = 5
# Note: Do not use the eval built-in library function.
# First Trial - multiple submissions


import re


class BasicCalculatorII(object):
    # Test on LeetCode - 372ms
    # 1. use "+-*/" to extract operators and use "\d+"" to extract operands
    # 2. use two stacks - opd_stack and opr_stack
    # 3. if operator == "+" or "-", push to stack. else, do arithmetic for the "*" or "/" operators.
    # 4. evaluate the stack (only "+" and "-")
    # return the top of the stack
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operator_pattern = re.compile(r"[\+\-\*\/]")
        operand_pattern = re.compile(r"\d+")
        operators = re.findall(operator_pattern, s)
        operands = re.findall(operand_pattern, s)
        opd_length, opr_length = len(operands), len(operators)
        if opd_length == 0:
            return 0
        if opd_length == 1:
            return int(operands[0])
        opd_stack, opr_stack = [operands[0]], []

        for i in range(0, opr_length):
            operator = operators[i]
            if operator == "*" or operator == "/":
                opd_stack[-1] = self.do_arithmetic(opd_stack[-1], operands[i+1], operator)
            else:  # operator == "+" or "-"
                if len(opr_stack) > 0:
                    self.eval_once(opd_stack, opr_stack)
                # now opr_stack is empty, populate it with current operator
                opr_stack.append(operator)
                opd_stack.append(operands[i+1])
        self.eval_once(opd_stack, opr_stack)  # in case for one "+" or "-"
        return opd_stack[-1]

    def eval_once(self, opd_stack, opr_stack):
        if len(opr_stack) > 0:
            opd2 = opd_stack.pop()
            opd1 = opd_stack.pop()
            operator = opr_stack.pop()
            opd_stack.append(self.do_arithmetic(opd1, opd2, operator))

    def do_arithmetic(self, opd1, opd2, operator):
        if operator == "+":
            ret = int(opd1) + int(opd2)
        elif operator == "-":
            ret = int(opd1) - int(opd2)
        elif operator == "*":
            ret = int(opd1) * int(opd2)
        else:
            ret = int(opd1) / int(opd2)
        return ret

    # read s on the run and only calculate "*" and "/" operators - a bit awkward
    #   1. split s into a list of characters
    #   2. read chars as numbers or operators
    #   3. remember previous opd and opr.
    def calculate_nice(self, s):
        l = list(s)
        length = len(l)
        if length == 0:
            return 0
        opd, opr = 0, "+"
        stack = []
        for idx, e in enumerate(l):
            if e.isdigit():
                opd = opd * 10 + int(e)
            elif e in ("+", "-", "*", "/") or idx == length - 1:
                if opr == "+":
                    stack.append(opd)
                elif opr == "*":
                    stack.append(int(stack.pop()) * opd)
                elif opr == "-":
                    stack.append(-opd)
                elif opr == "/":
                    top = int(stack.pop())
                    if top >= 0:
                        stack.append(top / opd)
                    else:
                        stack.append(-(abs(top) / opd))
                opd, opr = 0, e
        return sum(stack)

    # 1/3 - Revisit
    # Test on LC - 232ms 74%
    # Idea:
    #   opd_stack and opr_stack.
    #   first do * and /, then + and -. Note, add fake values to avoid list operations.
    # e.g.
    #   opds = [1, 2, 3, 4]  ->  [1, 0, 0, 24]  -> 25
    #   oprs = [+, *, *]    ->   [+, +, +]
    #
    def calculate_revisit(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        opds = re.findall(r'\d+', s)
        for i in range(0, len(opds)):
            opds[i] = int(opds[i])
        opts = re.findall(r'[\+\-\*\\/]', s)
        opt_length = len(opts)
        for i in range(0, opt_length):
            if opts[i] == '*' or opts[i] == '/':
                opds[i+1] = self.simple_calculate(opts[i], opds[i], opds[i+1])
                opds[i] = 0
                if i == 0:
                    opts[i] = '+'
                else:
                    opts[i] = opts[i-1]  # inherit previous operator
        for i in range(0, opt_length):
            opds[i+1] = self.simple_calculate(opts[i], opds[i], opds[i+1])
        return opds[-1]

    def simple_calculate(self, opt, opd1, opd2):
        ret = 0
        if opt == '+':
            ret = opd1 + opd2
        elif opt == '-':
            ret = opd1 - opd2
        elif opt == '*':
            ret = opd1 * opd2
        else:
            ret = opd1 / opd2
        return ret


def main():
    test = BasicCalculatorII()
    print test.calculate("0")
    print test.calculate("1-1+1")
    print test.calculate_nice("1+2*5/3+6/4*2")
    print test.calculate(" 3+5 / 2 ")
    print test.calculate("12-3*4")
    print test.calculate("2*3*4")


if __name__ == "__main__":
    main()