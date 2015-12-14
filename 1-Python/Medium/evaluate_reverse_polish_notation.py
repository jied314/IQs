# 10/20 - Stack (M)
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
# Some examples: ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#               ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6


class EvaluateReversePolishNotation(object):
    operators = set('+-*/')

    # Test on LeetCode -72MS
    # Idea:
    #   use stack to store operands. if operators, pop two operands and do arithmetic; push the result back.
    #   after the evaluation, result is stored in the stack. There should be only one element in the stack.
    # Note:
    #   6 / -132 == -1 in Python. use int(float(6) / -132) to work around.
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if tokens is None:
            return 0
        operands = []
        for token in tokens:
            if token in EvaluateReversePolishNotation.operators:
                if len(operands) == 1:
                    break
                opd2 = operands.pop()
                opd1 = operands.pop()
                if token == "+":
                    r = opd1 + opd2
                elif token == '-':
                    r = opd1 - opd2
                elif token == "*":
                    r = opd1 * opd2
                else:
                    r = int(float(opd1) / opd2)
                operands.append(r)
            else:
                operands.append(int(token))
        return operands[-1]


def main():
    test = EvaluateReversePolishNotation()
    print test.evalRPN(["4", "+"])
    print test.evalRPN(["2", "1", "+", "3", "*"])
    print test.evalRPN(["4", "13", "5", "/", "+"])
    print test.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])


if __name__ == "__main__":
    main()