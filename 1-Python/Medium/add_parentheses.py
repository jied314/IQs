# 10/7,8 - Divide and Conquer
# Given a string of numbers and operators, return all possible results from computing all the different possible ways
# to group numbers and operators. The valid operators are +, - and *.

import re

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class AddParentheses(object):
    result = []

    # Test on LeetCode - 68ms
    def diff_ways_to_compute(self, input):
        """
            :type input: str
            :rtype: List[int]
            """
        AddParentheses.result = []
        operands = re.findall(r'\d+', input)
        operators = re.findall(r'\D', input)
        expr_tree = Node(operands[0])
        self.build_expression_trees(operators, operands, expr_tree, 0, len(operators))
        return AddParentheses.result


    def build_expression_trees(self, operators, operands, expr_tree, i, operator_length):
        if i == operator_length:
            AddParentheses.result.append(self.eval_expression_tree(expr_tree))
        else:
            tree = expr_tree
            parent = None
            while tree is not None:
                # build a expression node on the next operator to replace on right
                new_tree = self.built_next_tree_node(operators[i], operands[i + 1])
                new_tree.left = tree
                if parent is not None:  # new node as the right child
                    parent.right = new_tree
                    self.build_expression_trees(operators, operands, expr_tree, i + 1, operator_length)
                    parent.right = new_tree.left
                else:  # new node as the root
                    self.build_expression_trees(operators, operands, new_tree, i + 1, operator_length)
                    new_tree.left = None
                parent = tree
                tree = tree.right


    def built_next_tree_node(self, operator, operand):
        new_tree = Node(operator)
        new_tree.right = Node(operand)
        return new_tree

    def eval_expression_tree(self, expr_tree):
        if expr_tree.left is not None:
            operator = expr_tree.val
            if operator == '-':
                result = self.eval_expression_tree(expr_tree.left) - self.eval_expression_tree(expr_tree.right)
            elif operator == '*':
                result = self.eval_expression_tree(expr_tree.left) * self.eval_expression_tree(expr_tree.right)
            else:
                result = self.eval_expression_tree(expr_tree.left) + self.eval_expression_tree(expr_tree.right)
            return result
        return int(expr_tree.val)

    # Test on LeetCode - 88ms
    # Idea:
    #   Use Divide-And-Conquer strategy
    #   O(N) = (O(1) + O(N-1)) + (O(2) + O(N-2)) + ... + (O(N-1) + O(1))
    #   Should store intermediate result for future usage - that's why slower
    def diff_ways_to_compute_catalan(self, input):
        ret = []
        length = len(input)
        for i in range(0, length):
            match = re.match(r'\D', input[i])
            if match is not None:
                part1 = input[0:i]
                part2 = input[i+1:]
                part1Ret = self.diff_ways_to_compute_catalan(part1)
                part2Ret = self.diff_ways_to_compute_catalan(part2)
                for p1 in part1Ret:
                    for p2 in part2Ret:
                        c = 0
                        operator = match.group(0)
                        if operator == '+':
                            c = p1 + p2
                        elif operator == '-':
                            c = p1 - p2
                        elif operator == '*':
                            c = p1 * p2
                        ret.append(c)
        if len(ret) == 0:  # deal with special situation - only operands
            ret.append(int(input))
        return ret

    # Test on LeetCode - 44ms
    # Idea:
    #   use catalan number and DP
    #   much faster than just use catalan number - dp caches intermediate results for future uses
    #
    def diff_ways_to_compute_catalan_dp(self, input):
        dp_map = {}
        return self.compute_with_dp(input, dp_map)

    def compute_with_dp(self, input, dp_map):
        if input in dp_map:
            return dp_map[input]
        ret = []
        length = len(input)
        for i in range(0, length):
            match = re.match(r'\D', input[i])
            if match is not None:
                part1 = input[0:i]
                part2 = input[i+1:]
                part1Ret = self.compute_with_dp(part1, dp_map)
                part2Ret = self.compute_with_dp(part2, dp_map)
                for p1 in part1Ret:
                    for p2 in part2Ret:
                        c = 0
                        operator = match.group(0)
                        if operator == '+':
                            c = p1 + p2
                        elif operator == '-':
                            c = p1 - p2
                        elif operator == '*':
                            c = p1 * p2
                        ret.append(c)
        if len(ret) == 0:  # deal with special situation - only operands
            ret.append(int(input))
        dp_map[input] = ret
        return ret

def main():
    test = AddParentheses()
    expr1 = "2-1-1"
    expr2 = "2*3-4*5"
    expr3 = "11"
    print test.diff_ways_to_compute(expr1)
    print test.diff_ways_to_compute_catalan_dp(expr2)
    print test.diff_ways_to_compute(expr3)


if __name__ == '__main__':
    main()

