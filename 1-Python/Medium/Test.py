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
    """
    def canFinish(self, numCourses, prerequisites):
        """
    """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
    """
        if len(prerequisites) == 0:
            return False
        if numCourses <= 1:
            return True
        adj = self.build_adj(numCourses, prerequisites)
        reverse_adj = self.build_reverse_adj(numCourses, prerequisites)
        starts = [i for i in xrange(numCourses) if len(reverse_adj[i]) == 0]
        visited = set()
        while reverse_adj:
            new_starts = []
            for start in starts:
                visited.add(start)
                del reverse_adj[start]
                tails = adj[start]
                for tail in tails:
                    if tail in visited:
                        return False
                    reverse_adj[tail].pop(start)
                    if len(reverse_adj[tail]) == 0:
                        new_starts.append(tails)
            starts = new_starts
        return True

    # [1, 0] -> {1: [0]}
    def build_reverse_adj(self, numCourses, prerequisites):
        reverse_adj = [[] for _ in xrange(numCourses)]
        for i, j in prerequisites:
            reverse_adj[i].append(j)
        return reverse_adj

    # [1, 0] -> {0: [1]}
    def build_adj(self, numCourses, prerequisites):
        adj = [[] for _ in xrange(numCourses)]
        for i, j in prerequisites:
            adj[j].append(i)
        return adj

    def can_finish_dfs_revisit(self, numCourses, prerequisites):
        matrix = self.generate_adjacent_matrix(numCourses, prerequisites)
        incoming_degrees = [0] * numCourses
        for i in range(0, numCourses):
            for course in matrix[i]:
                incoming_degrees[course] += 1
        for j in range(0, numCourses):
            for i in range(0, numCourses):
                if incoming_degrees[i] > 0:
                    continue
                if i == numCourses:  # no starting nodes
                    return False
                incoming_degrees[i] = -1
                for
        return True

    def generate_adjacent_matrix(self, numCourses, edge_list):
        matrix = [set() for _ in xrange(numCourses)]
        for cur, pre in edge_list:
            matrix[pre].add(cur)
        return matrix"""



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
        return ret"""

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
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
        return nl

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if numCourses == 0:
            return []
        if numCourses == 1:
            return[0]

        ret = []
        visited = set()
        # store outgoing edges pre -> cur
        matrix_out = [set() for _ in range(numCourses)]
        # store degree of incoming edges -> decide whether is a new root
        num_in = [0] * numCourses
        # store root nodes (only have outgoing edges)
        roots = set([i for i in range(0, numCourses)])
        self.generate_adjacent_list(matrix_out, num_in, roots, numCourses, prerequisites)

        while len(visited) < numCourses:  # not visit all nodes
            if not roots:
                return []
            # for each root node, remove outgoing edges, store new root nodes
            temp = set()
            for root in roots:
                visited.add(root)
                courses = matrix_out[root]
                for course in courses:
                    if course in visited:  # detect a cycle
                        return []
                    else:
                        num_in[course] -= 1
                        if num_in[course] == 0:
                            temp.add(course)
            ret.extend(list(roots))
            roots = temp
        return ret

    def generate_adjacent_list(self, matrix, num_in, roots, numCourses, prerequisites):
        for cur, pre in prerequisites:
            matrix[pre].add(cur)
            num_in[cur] += 1
            roots.discard(cur)  # not start nodes

test = Solution()
print test.findOrder(4, [[0,1],[3,1],[1,3],[3,2]])
