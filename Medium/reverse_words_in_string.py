# String - Reverse Words in a String
# Given an input string, reverse the string word by word.
# 6/17
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
        words = s.split()
        words.reverse()
        return ' '.join(words)

def main():
    test = ReverseWords()
    print test.reverse_words_in_place(" ")

if __name__ == '__main__':
    main()