# Revisit - 1/7, Greedy
# Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once
# and only once.
# You must make sure your result is the smallest in lexicographical order among all possible results.
# Example:
#   Given "bcabc"
#   Return "abc"
#   Given "cbacdcbc"
#   Return "acdb"


class RemoveDuplicateLetters(object):
    # Adapt from Online Solution
    # Given the string s, the greedy choice (i.e., the leftmost letter in the answer) is the smallest s[i],
    # s.t. the suffix s[i .. ] contains all the unique letters.
    def remove_duplicate_letters(self, s):
        idx = lambda c: ord(c) - ord('a')
        cnt = [0] * 26  # store character appearances
        for c in s:
            cnt[idx(c)] += 1

        candidate = [0] * 26  # record visited characters
        for c in s:
            i = idx(c)
            if cnt[i] >= 1:  # duplicate
                candidate[i] = 1
                cnt[i] -= 1
            if cnt[i] == 0:  # find one single character
                break

        for i in xrange(0, 26):
            if candidate[i]:
                ch = chr(ord('a') + i)  # the leftmost small character
                return ch + self.remove_duplicate_letters(s[s.find(ch):].replace(ch, ""))
        return ""

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s

        # record character appearing indices
        chars = [[] for _ in range(26)]
        length = len(s)
        for i in range(length):
            chars[self.get_char_index(s[i])].append(i)

        j = 0
        last = -1
        for c in s:
            index = self.get_char_index(c)
            if len(chars[index]) == 1:
                last = chars[index][0]
                j += 1
            else:
                if last == -1:
                    last = chars[index][0]
                indices = chars[index]
                while len(indices) > 1 and indices[0] < last:
                    indices.pop(0)

        ret = [""] * length
        for i in range(26):
            if chars[i]:
                ret[chars[i][0]] = self.get_char(i)
        return "".join(ret)



    def get_char_index(self, char):
        return ord(char) - ord('a')

    def get_char(self, index):
        return chr(ord('a') + index)


test = RemoveDuplicateLetters()
print test.remove_duplicate_letters("bcabc")
print test.removeDuplicateLetters("bcabc"), "\n"

print test.remove_duplicate_letters("cbacdcbc")
print test.removeDuplicateLetters("cbacdcbc"), "\n"

print test.remove_duplicate_letters("ccacbaba")
print test.removeDuplicateLetters("ccacbaba"), "\n"

print test.remove_duplicate_letters("abacb")
print test.removeDuplicateLetters("abacb"), "\n"

print test.remove_duplicate_letters("abcab")
print test.removeDuplicateLetters("abcab"), "\n"

print test.remove_duplicate_letters("rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws")
print test.removeDuplicateLetters("rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws")

