# 6/17 String - Reverse Words in a String
# Given an input string, reverse the string word by word.
# For example, Given s = "the sky is blue", return "blue is sky the".
# Clarification:
#   1. What constitutes a word?
#   A sequence of non-space characters constitutes a word.
#   2. Could the input string contain leading or trailing spaces?
#   Yes. However, your reversed string should not contain leading or trailing spaces.
#   3. How about multiple spaces between two words?
#   Reduce them to a single space in the reversed string.
# Revisit - 1/11
class ReverseWords:
    # @param s, a string
    # @return a string
    # Test on LeetCode - 202ms
    def reverse_words_in_place(self, s):
        indexes = []
        start = 0
        for i in range(0, len(s)):
            if s[i] == ' ':
                if i > 0 and s[i - 1] != ' ':
                    indexes.append([start, i - 1])
                    start = i
            else:
                if i > 0 and s[i - 1] == ' ':
                    indexes.append([start, start])
                    start = i
        if start <= len(s) - 1:
            indexes.append([start, len(s) - 1])
        #print indexes

        if indexes:
            # delete leading and trailing white spaces
            if s[indexes[0][0]] == ' ':
                indexes.pop(0)
            if indexes:
                if s[indexes[len(indexes) - 1][0]] == ' ':
                    indexes.pop()
                print indexes

            if indexes:
                result = []
                for i in range(len(indexes) - 1, -1, -1):
                    index = indexes[i]
                    for i in range(index[0], index[1] + 1):
                        result.append(s[i])
                return ''.join(result)
        return ""

    # Test on LeetCode - 70ms
    def reverse_words_list(self, s):
        words = s.split()  # split by multiple spaces
        words.reverse()
        return ' '.join(words)

    # 1/11 - Revisit, Test on LC - 80ms 7%
    def reverse_words_revisit(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        chars.reverse()
        chars.append(' ')
        i, length = 0, len(chars)
        start = 0
        words = []
        while i < length:
            if chars[i] == ' ' and i > 0 and chars[i-1] != ' ':
                words.append(''.join(reversed(chars[start:i])))
            elif chars[i] != ' ' and i > 0 and chars[i-1] == ' ':
                start = i
            i += 1
        return ' '.join(words)

    # 1/11 - Borrow from Yanxing
    # Test on LC - 76ms 7%
    def reverse_words_nice(self, s):
        ret = ""
        end = len(s)
        for i in range(len(s)-1, -2, -1):
            if i < 0 or s[i] == ' ':
                if i < len(s)-1 and s[i+1] != ' ':
                    ret += s[i+1: end]
                    ret += ' '
            elif s[i] != ' ' and i < len(s)-1 and s[i+1] == ' ':
                end = i+1
        return ret.rstrip()

def main():
    test = ReverseWords()
    print ',', test.reverse_words_revisit(" "), ','
    print ',', test.reverse_words_in_place(" "), ','
    print test.reverse_words_nice('a'), ','

if __name__ == '__main__':
    main()