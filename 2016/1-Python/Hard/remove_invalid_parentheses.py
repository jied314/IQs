# 1/14 - DFS, BFS
# Remove the minimum number of invalid parentheses in order to make the input string valid.
# Return all possible results.
# Note: The input string may contain letters other than the parentheses ( and ).
# Examples:
#   "()())()" -> ["()()()", "(())()"]
#   "(a)())()" -> ["(a)()()", "(a())()"]
#   ")(" -> [""]
# Idea:
#   generate all possible states by removing one ( or ), check if they are valid.
#  if found valid ones, add to the result list; otherwise, add them to a queue and continue.
# T(n) = n x C(n, n) + (n-1) x C(n, n-1) + ... + 1 x C(n, 1) = n x 2^(n-1).

import collections


class Solution(object):
    # Test on LC - 456ms, 31%
    def remove_invalid_parentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s is None or len(s) == 0:
            return [""]
        res = []
        visited = set()
        queue = collections.deque()
        queue.append(s)
        visited.add(s)
        flag = False

        while len(queue) > 0:
            s = queue.popleft()
            if self.is_valid(s):
                res.append(s)
                flag = True
            if flag:
                continue
            for i in range(0, len(s)):
                if s[i] != '(' and s[i] != ')':
                    continue
                t = s[:i] + s[i+1:]
                if t not in visited:
                    queue.append(t)
                    visited.add(t)
        return res

    def is_valid(self, s):
        count = 0
        for i in range(0, len(s)):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                if count == 0:
                    return False
                count -= 1
        return count == 0

test = Solution()
print test.remove_invalid_parentheses("()())()")