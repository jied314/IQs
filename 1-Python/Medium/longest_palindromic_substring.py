class LongestPalindromicSubstring(object):
    def longest_palindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_map = self.process_word(s)
        candidate, length = "", 0
        for c in char_map:
            positions = char_map[c]
            occurrence = len(positions)
            if occurrence == 1 and length == 0:
                candidate, length = c, 1
            for i in range(0, occurrence - 1):
                start = positions[i]
                for j in range(1, occurrence):
                    end = positions[j]
                    span = end - start + 1
                    if span > length:
                        if self.is_palindrome(s, start, end):
                            candidate, length = s[start:end + 1], span
        return candidate


    def process_word(self, s):
        char_map = {}
        length = len(s)
        for i in range(0, length):
            c = s[i]
            if c not in char_map:
                char_map[c] = []
            char_map[c].append(i)
        return char_map

    # check if s is a palindrome
    def is_palindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True



def main():
    test = LongestPalindromicSubstring()
    print test.longest_palindrome("a")


if __name__ == "__main__":
    main()

