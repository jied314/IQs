# 3/7 - Medium
# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation
# sequence from beginWord to endWord, such that:
# 1. Only one letter can be changed at a time
# 2. Each intermediate word must exist in the word list
#
# For example,
# Given:
#   beginWord = "hit"
#   endWord = "cog"
#   wordList = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.
#
# Followup:
#   find all shortest transformation sequence(s) from beginWord to endWord
#   [
#       ["hit","hot","dot","dog","cog"],
#       ["hit","hot","lot","log","cog"]
#   ]
#
# Note:
#   Return 0 if there is no such transformation sequence.
#   All words have the same length.
#   All words contain only lowercase alphabetic characters.
from collections import deque


class WordLadder(object):
    # Idea:
    #   BFS - start from the beginWord, visit all neighbors before expanding, keep track of distance.
    #   only one direction BFS.
    # Note:
    #   insert end_word into the dictionary
    #   words visited earlier result shorter paths (that's why can remove those words from dictionary)
    #   Faster to remove words from dictionary than keeping a history of visited words
    def ladder_length_bfs_tle(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList.add(endWord)
        to_visit = deque()
        to_visit.append(beginWord)
        visited = set()  # prefer to use visited instead of removing from dictionary
        visited.add(beginWord)
        dist = 1
        while len(to_visit) > 0:
            cur_size = len(to_visit)
            for i in range(0, cur_size):
                word = to_visit.popleft()
                if word == endWord:
                    return dist
                self.add_neighbors(word, wordList, to_visit, visited)
            dist += 1
        return 0

    # find all neighbors exist in the dictionary, add them to the queue.
    def add_neighbors(self, word, wordList, to_visit, visited):
        for i in range(0, len(word)):
            for j in range(0, 26):
                c = chr(ord('a')+j)
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordList and next_word not in visited:
                    to_visit.append(next_word)
                    visited.add(next_word)

    # borrowed from Yanxing
    # one direction BFS, a variation of BFS.
    def ladder_length_bfs_one(self, beginWord, endWord, wordList):
        queue = deque()
        queue.append(beginWord)
        visited = {beginWord: 1}

        while queue:
            word = queue.popleft()
            dist = visited[word]
            for i in range(0, len(word)):
                for j in range(0, 26):
                    c = chr(ord('a') + j)
                    new_word = word[:i] + c + word[i+1:]
                    if new_word == endWord:
                        return dist+1
                    if new_word in wordList and new_word not in visited:
                        queue.append(new_word)
                        visited[new_word] = dist + 1
        return 0

    # Test on LC - 136ms, 90%
    # borrowed from Yanxing - two direction BFS
    def ladder_length_bfs_two(self, beginWord, endWord, wordList):
        # two queues and two dictionaries
        q0, q1 = deque(), deque()
        q0.append(beginWord)
        q1.append(endWord)
        visited0 = {beginWord: 1}
        visited1 = {endWord: 1}

        while q0 and q1:
            # always expand the shorter queue
            if len(q0) >= len(q1):
                q0, q1 = q1, q0
                visited0, visited1 = visited1, visited0

            word = q0.popleft()
            dist = visited0[word]

            # generate word neighbors, return if exists in the other dictionary.
            for i in range(0, len(word)):
                for j in range(0, 26):
                    c = chr(ord('a') + j)
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in visited1:  # stop
                        return dist + visited1[new_word]
                    if new_word in wordList and new_word not in visited0:  # add new_word
                        q0.append(new_word)
                        visited0[new_word] = dist + 1
        return 0

    # BFS on both directions
    # Test on LC - 140ms, 89%
    def ladder_length_bfs(self, beginWord, endWord, wordList):
        head, tail, visited = set(), set(), set()
        head.add(beginWord)
        tail.add(endWord)
        dist = 2
        while head and tail:
            if len(head) > len(tail):
                head, tail = tail, head

            temp = set()
            while head:
                word = head.pop()
                visited.add(word)
                for i in range(0, len(word)):
                    for j in range(0, 26):
                        c = chr(ord('a')+j)
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in tail:
                            return dist
                        if next_word in wordList and next_word not in visited:
                            temp.add(next_word)
                            visited.add(next_word)

            dist += 1
            head = temp
        return 0

    # follow-up: find all shortest paths
    def find_ladders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        q1, q2 = deque(), deque()
        q1.append(beginWord)
        q2.append(endWord)
        visited1, visited2 = {beginWord: ""}, {endWord: ""}
        ret = []
        flag = False

        while q1 and q2:
            if len(q1) >= len(q2):
                q1, q2 = q2, q1
                visited1, visited2 = visited2, visited1
            temp = deque()
            while q1:
                word = q1.popleft()
                for i in range(0, len(word)):
                    for j in range(0, 26):
                        c = chr(ord('a') + j)
                        neighbor = word[:i] + c + word[i+1:]
                        if neighbor in visited2:
                            flag = True
                            if beginWord in visited1:
                                ret.append(self.assemble_path(word, neighbor, visited1, visited2))
                            else:
                                ret.append(self.assemble_path(neighbor, word, visited2, visited1))
                        if neighbor not in visited1 and neighbor in wordlist:
                            temp.append(neighbor)
                            visited1[neighbor] = word
            if flag:
                break
            q1 = temp
        return ret

    def assemble_path(self, word1, word2, visited1, visited2):
        path1, path2 = [], []

        path1.append(word1)
        while visited1[word1]:
            word1 = visited1[word1]
            path1.append(word1)
        path1.reverse()

        path2.append(word2)
        while visited2[word2]:
            word2 = visited2[word2]
            path2.append(word2)

        return path1 + path2

class WordNode:
    def __init__(self, word, step):
        self.word = word
        self.step = step


test = WordLadder()
# print test.ladder_length_bfs_tle("hit", "cog", {"hot","dot","dog", "lot", "log"})
# print test.ladder_length_bfs_one("hit", "cog", {"hot","dot","dog", "lot", "log"})
# print test.ladder_length_bfs_two("hit", "cog", {"hot","dot","dog", "lot", "log"})
#print test.ladder_length_bfs("hit", "cog", {"hot","dot","dog", "lot", "log"})
print test.find_ladders("hot", "dog", ["hot","dog","dot"])