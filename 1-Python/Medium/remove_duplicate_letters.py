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
            if cnt[i] >= 1:
                candidate[i] = 1
                cnt[i] -= 1
            if cnt[i] == 0:  # find one single character
                break

        for i in xrange(0, 26):
            if candidate[i]:
                ch = chr(ord('a') + i)  # the leftmost small character
                return ch + self.remove_duplicate_letters(s[s.find(ch):].replace(ch, ""))
        return ""


test = RemoveDuplicateLetters()
print test.remove_duplicate_letters("bcabc")
print test.remove_duplicate_letters("cbacdcbc")
print test.remove_duplicate_letters("ccacbaba")
print test.remove_duplicate_letters("abacb")
print test.remove_duplicate_letters("abcab")
print test.remove_duplicate_letters("rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws")

