# 2/10 -
# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
# reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK.
# Thus, the itinerary must begin with JFK.
#
# Note:
#   If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order
# when read as a single string.
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
#   All airports are represented by three capital letters (IATA code).
#   You may assume all tickets may form at least one valid itinerary.
#
# Idea:
#   Greedy DFS, building the route backwards when retreating.
#   1. DFS - if stuck, record the end; go back to see if has new paths.
#   2. BFS - always process from the end of the stack.
# Refer: https://leetcode.com/discuss/84659/short-ruby-python-java-c


class Solution(object):
    def find_itinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        tickets.sort(reverse=True)
        adjs = self.get_adjs(tickets)
        route = []
        # self.visit("JFK", adjs, route)
        self.find_itinerary_bfs(adjs, route)
        route.reverse()
        return route

    # Test on LC - 96ms, 74%
    # BFS with stack - always update based on the tail of the stack
    def find_itinerary_bfs(self, adjs, ret):
        stack = ["JFK"]
        while stack:
            while stack[-1] in adjs and adjs[stack[-1]]:
                    stack.append(adjs[stack[-1]].pop())
            ret.append(stack.pop())

    # Test on LC - 84ms, 93%
    def visit(self, node, adjs, ret):
        # if not stuck, rewind to find a new path
        if node in adjs:
            while adjs[node]:
                self.visit(adjs[node].pop(), adjs, ret)
        # record current since all its children have been visited (or has no children)
        ret.append(node)

    def get_adjs(self, edges):
        adjs = {}
        for start, end in edges:
            if start not in adjs:
                adjs[start] = []
            adjs[start].append(end)
        return adjs


test = Solution()
print test.find_itinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])
