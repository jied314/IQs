# 1/10 - Hash Table, Two Pointers, String
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc",
# which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
# Note:
#   use two pointers and use left is essentially the same.


class Solution(object):
    # Test on LC 120ms, 40%
    # Idea:
    #   use set to store all unique characters
    #   use dp to store the length of the prev position
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        dp = 0   # store the longest length for the prev position
        ret = 0
        unique = set()  # unique characters
        for i in range(0, len(s)):
            if s[i] not in unique:  # unique
                dp += 1
                unique.add(s[i])
            else:  # not unique
                j = i - dp
                while j < i and s[j] != s[i]:  # starting from j, eliminate characters
                    unique.remove(s[j])
                    j += 1
                dp = len(unique)
            ret = max(ret, dp)
        return ret

    # Borrow from Yanxing - Test on LC 116ms 45%
    # Idea:
    #   not use set to store unique letter.
    #   use a dictionary to store the most recent index of a letter.
    #   use left to indicate search scope - left = dict[c] + 1
    #   if letter_dict[c] < left, c should be included. - no need to update set.
    def length_of_longest_substring_nice(self, s):
        if len(s) == 0:
            return 0
        left = 0
        max_length, length = 0, 0
        dict = {}

        for i in range(0, len(s)):
            c = s[i]
            if c not in dict or dict[c] < left:  # unique
                dict[c] = i
                length += 1
            else:
                left = dict[c] + 1
                length = i - dict[c]
                dict[c] = i
            max_length = max(max_length, length)
        return max_length


