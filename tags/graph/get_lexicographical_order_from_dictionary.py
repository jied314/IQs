# 2/8 - Graph, Sort
# There is a new language which uses the latin alphabet. However, you do not know the order among letters.
# You receive a list of words lexicographically sorted by the rules of this new language.
# From this list, derive one valid particular ordering of letters in this language.
# e.g. dictionry:
#   {"ze", "yf", "xd", "wd", "vd", "ua", "tt", "sz", "rd",
#   "qd", "pz", "op", "nw", "mt", "ln", "ko", "jm", "il",
#   "ho", "gk", "fa", "ed", "dg", "ct", "bb", "ba"}
# Output:
#   z, y, x, w, v, u, t, s, r, q, p, o, n, m, l, k, j, i, h, g, f, e, d, c, b, a
# Idea:
#   1) Create a graph g with number of vertices equal to the size of alphabet in the given alien language.
#      For example, if the alphabet size is 5, then there can be 5 characters in words.
#      Initially there are no edges in graph.
#   2) Do following for every pair of adjacent words in given sorted array.
#       a) Let the current pair of words be word1 and word2. One by one compare characters of both words and find the
#     first mismatching characters.
#       b) Create an edge in g from mismatching character of word1 to that of word2.
#   3) Print topological sorting of the above created graph.

from graph import Graph


class Solution(object):
    def get_order(self, dict):
        """
        :param dict: List[String]
        :return: List[String]
        """
        g = Graph(26)
        for i in range(0, len(dict)-1):
            self.build_graph(g, dict[i], dict[i+1])
        order = g.topo_sort()
        ret = []
        for c in order:
            ret.append(chr(c + ord('a')))
        return ret

    def build_graph(self, graph, w1, w2):
        length = min(len(w1), len(w2))
        for i in range(0, length):
            if w1[i] != w2[i]:
                graph.add_edge(ord(w1[i]) - ord('a'), ord(w2[i]) - ord('a'))
                break

test = Solution()
print test.get_order(["ze", "yf", "xd", "wd", "vd", "ua", "tt", "sz", "rd", "qd", "pz", "op", "nw", "mt", "ln", "ko",
                      "jm", "il", "ho", "gk", "fa", "ed", "dg", "ct", "bb", "ba"])