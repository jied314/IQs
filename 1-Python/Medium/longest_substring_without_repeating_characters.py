# 1/10 - Hash Table, Two Pointers, String
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc",
# which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
#
class Solution(object):
    # first trail - Test on LC 136ms 26%
    # Idea:
    #   use set to store all unique characters
    #   use a list to store the longest substring ending with current character
    def length_of_longest_substring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        max_length = 0
        unique = set()  # current unique letter
        sub_s = []  # store current longest substring
        for c in s:
            if c not in unique:  # unique
                unique.add(c)
                sub_s.append(c)
                max_length = max(max_length, len(sub_s))
            else:
                pos = sub_s.index(c)
                for i in range(0, pos):
                    unique.remove(sub_s[i])
                sub_s = sub_s[pos+1:]
                sub_s.append(c)
        return max_length

    # Borrow from Yanxing - Test on LC 112ms 52%
    # Idea:
    #   use left to indicate search scope. if letter_dict[c] < left, c should be included.
    def length_of_longest_substring_nice(self, s):
        if len(s) == 0:
            return 0
        left = 0
        max_length, length = 0, 0
        letter_dict = {}

        for i in range(0, len(s)):
            c = s[i]
            if c not in letter_dict or letter_dict[c] < left:  # unique
                letter_dict[c] = i
                length += 1
            else:
                left = letter_dict[c] + 1
                letter_dict[c] = i
                max_length = max(max_length, length)
                length = i - left + 1
        return max(max_length, length)


