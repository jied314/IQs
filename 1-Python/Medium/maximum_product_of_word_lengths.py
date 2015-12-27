# 12/21 - Bit Manipulation
# Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not
# share common letters.
# You may assume that each word will contain only lower case letters.
# If no such two words exist, return 0.
# TLE on first trial

class Solution(object):
    def max_product_tle(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        length = len(words)
        matrix = []
        for i in range(0, length-1):
            matrix.append(set([j for j in range(i+1, length)]))
        for i in range(0, 26):
            c = chr(ord('a') + i)
            temp = []
            for j in range(0, length):
                if c in words[j]:
                    temp.append(j)
            for j in range(0, len(temp)-1):
                for k in range(0, len(temp)):
                    matrix[temp[j]].discard(temp[k])
        
        max_length = 0
        for i in range(0, length-1):
            word = words[i]
            if matrix[i]:
                matrix[i] = list(matrix[i])
                for j in range(0, len(matrix[i])):
                    max_length = max(max_length, len(word) * len(words[matrix[i][j]]))
        return max_length

    # Idea:
    #   Use bit manipulation (mask) to record character appearances.
    #   e.g. 'a' -> 0, 'b' -> 10
    #   Then use & to see whether there are any common character
    def max_product_bit(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        max_length = 0
        length = len(words)
        masks = [0] * length
        for i in range(0, length):
            for c in words[i]:
                masks[i] |= 1 << (ord(c) - ord('a'))
            for j in range(0, i):
                if (masks[j] & masks[i]) == 0:
                    max_length = max(max_length, len(words[i]) * len(words[j]))
        return max_length


test = Solution()
print test.max_product_tle(["abcw","baz","foo","bar","xtfn","abcdef"])