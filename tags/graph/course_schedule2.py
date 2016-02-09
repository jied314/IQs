# 2/5 - Graph, DFS, BFS, Topological Sort
# There are a total of n courses you have to take, labeled from 0 to n - 1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
# which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take
# to finish all courses.
# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses,
# return an empty array.
#
# For example:
#   2, [[1,0]]
#   There are a total of 2 courses to take. To take course 1 you should have finished course 0.
# So the correct course order is [0,1]
#   4, [[1,0],[2,0],[3,1],[3,2]]
#   There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
# Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3].
# Another correct ordering is[0,2,1,3].
from collections import deque

class Solution(object):
    def find_order(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # store outgoing edges pre -> cur
        out_adj_list = [[] for _ in range(numCourses)]
        # store degree of incoming edges -> decide whether is a new root
        in_degrees = [0] * numCourses
        self.init(out_adj_list, in_degrees, prerequisites)
        # return self.solve_BFS(out_adj_list, in_degrees, numCourses)
        return self.solve_DFS(out_adj_list, numCourses)

    # initialize variables
    def init(self, adj, in_degrees, prerequisites):
        for cur, pre in prerequisites:
            adj[pre].append(cur)  # pre -> cur
            in_degrees[cur] += 1

    # Test on LC - 72ms, 89%
    # BFS traver the graph
    def solve_BFS(self, adj, in_degrees, numCourses):
        ret = []
        to_visit = deque()  # store all starting nodes
        for i in range(0, numCourses):
            if in_degrees[i] == 0:
                to_visit.append(i)

        while to_visit:
            pre = to_visit.popleft()
            ret.append(pre)
            # for each starting node, update in-degree for the destination node and check if it becomes starting node
            for cur in adj[pre]:
                in_degrees[cur] -= 1
                if in_degrees[cur] == 0:
                    to_visit.append(cur)

        # if has cycle or graph is not connected, len(ret) != numCourses
        return ret if len(ret) == numCourses else []

    # Test on LC - 80, 64%
    def solve_DFS(self, adj, numCourses):
        visited, in_visit = set(), set()
        not_visit = set([i for i in range(numCourses)])
        ret = []
        while not_visit:
            node = not_visit.pop()
            if not self.visit(node, adj, not_visit, visited, in_visit, ret):
                return []
        ret.reverse()
        return ret

    def visit(self, node, adj, not_visit, visited, in_visit, ret):
        if node in in_visit:  # cycle
            return False
        if node in visited:  # already visited, return
            return True
        in_visit.add(node)
        # visit all tos
        for to in adj[node]:
            if not self.visit(to, adj, not_visit, visited, in_visit, ret):
                return False
        # update for current node
        ret.append(node)
        in_visit.remove(node)
        visited.add(node)
        return True


test = Solution()
print test.find_order(2, [[1, 0]])

