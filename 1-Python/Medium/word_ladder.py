class WordLadder(object):
    # TLE - DFS stack overflow
    # Think of BFS (use queue)
    def ladder_length_tle(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        dp_dict = {}
        self.get_transformation_length(beginWord, endWord, set(), dp_dict, wordList)
        return dp_dict[beginWord]

    def get_transformation_length(self, beginWord, endWord, visited, dp_dict, wordList):
        # if already visited
        if beginWord in dp_dict:
            return dp_dict[beginWord]
        # if beginWord can directly reach endWord
        if self.word_distance(beginWord, endWord) == 1:
            dp_dict[beginWord] = 2
            return

        # use visited to record the search path
        # e.g. hot -> hit -> hot (Wrong)
        visited.add(beginWord)

        next_words = self.get_transformation_candidates(beginWord, visited, wordList)
        if len(next_words) == 0:  # exhaust all possible words in the dictionary -> not able to reach end
            dp_dict[beginWord] = 0
        for next_word in next_words:
            self.get_transformation_length(next_word, endWord, visited, dp_dict, wordList)
            if dp_dict[next_word] > 0:
                if beginWord in dp_dict:
                    dp_dict[beginWord] = min(dp_dict[beginWord], 1 + dp_dict[next_word])
                else:
                    dp_dict[beginWord] = 1 + dp_dict[next_word]
            else:
                dp_dict[beginWord] = 0

    # find all candidates of distance == 1
    def get_transformation_candidates(self, beginWord, visited, wordList):
        candidates = set()
        for word in wordList:
            if word not in visited and self.word_distance(beginWord, word) == 1:
                candidates.add(word)
        return candidates

    # measure word distance by number of char changes
    def word_distance(self, word1, word2):
        word_length = len(word1)
        distance = 0
        for i in range(0, word_length):
            if word1[i] != word2[i]:
                distance += 1
        return distance

    # BFS, still TLE
    # Idea:
    #   visit intermediate words by levels - avoid stack overflow
    # Note:
    #   insert end_word into the dictionary
    #   words visited earlier result shorter paths (that's why can remove those words from dictionary)
    # Faster to remove words from dictionary than keeping a history of visited words
    def ladder_length_bfs_tle(self, begin_word, end_word, word_list):
        word_list.add(end_word)
        queue = [WordNode(begin_word, 1)]
        # visited = set()
        while len(queue) > 0:
            top = queue.pop(0)
            cur_word = top.word
            if cur_word == end_word:
                return top.step
            #visited.add(cur_word)
            char_arr = list(cur_word)
            for i in range(0, len(cur_word)):
                temp_char = char_arr[i]
                for j in range(ord('a'), ord('z')):
                    if temp_char != chr(j):
                        char_arr[i] = chr(j)
                        next_word = "".join(char_arr)
                        #if next_word not in visited and next_word in word_list:
                        if next_word in word_list:
                            queue.append(WordNode(next_word, top.step+1))
                            word_list.remove(next_word)
                        char_arr[i] = temp_char
        return 0


class WordNode:
    def __init__(self, word, step):
        self.word = word
        self.step = step


test = WordLadder()
print test.ladder_length_tle("hit", "cog", {"hot","dot","dog", "lot", "log"})
print test.ladder_length_bfs("hit", "cog", {"hot","dot","dog", "lot", "log"})