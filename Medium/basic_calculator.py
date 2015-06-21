# Stack, Math - Basic Calculator
#
class BasicCalculator:
    # @param {string} s
    # @return {integer}
    # Test on LeetCode - 552ms
    def calculate(self, s):
        stack = []
        for i in range(0, len(s)):
            c = s[i]
            if c == ' ':  # space
                continue
            elif self.is_number(c):  # number
                num = int(c)
                if len(stack) > 0:
                    top = stack[-1]
                    if self.is_integer(top):  # number
                        num += top * 10
                        stack.pop()
                stack.append(num)
            else:  # operator
                if c == ')':
                    result = 0
                    while stack[-1] != '(':
                        operand = stack.pop()
                        if stack[-1] != '(':
                            operator = stack.pop()  # pop '('
                        else:
                            operator = '+'
                        if operator == '-':
                            operand *= -1
                        result += operand
                    stack.pop()
                    stack.append(result)
                elif c == '(':
                    stack.append(c)
                else:  # '+' or '-'
                    top = stack[-1]
                    if self.is_integer(top) or top == '(':
                        stack.append(c)
                    else:  # multiple operators
                        if (c == '+' and top == '+') or (c == '-' and top == '-'):
                            stack[-1] = '+'
                        else:
                            stack[-1] = '-'
        if stack:  # make sure only 1 element left in the stack
            result = stack.pop(0)
            while stack:
                operator = stack.pop(0)
                operand = stack.pop(0)
                if operator == '-':
                    operand *= -1
                result += operand
        else:
            result = 0
        return result

    def is_number(self, c):
        return ord('0') <= ord(c) <= ord('9')

    def is_integer(self, c):
        return isinstance(c, (int, long))

    # keep track sign, finish calculating on the run
    def calculate_second(self, s):
        stack = []
        result = 0
        number = 0
        sign = 1
        for i in range(0, len(s)):
            c = s[i]
            if self.is_number(c):  # number
                number = number * 10 + int(c)
            elif c == '+':
                result += sign * number
                number = 0
                sign = 1
            elif c == '-':
                result += sign * number
                number = 0
                sign = -1
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif c == ')':
                result += sign * number
                number = 0
                result *= stack.pop()
                result += stack.pop()
        if number != 0:
            result += sign * number
        return result



def main():
    test = BasicCalculator()
    print test.calculate_second('(1+(4+5+2)-3)+(6+8)')
    #print test.calculate("2147483647")
    print test.calculate_second(" 2-1 + 2 ")


if __name__ == '__main__':
    main()
        