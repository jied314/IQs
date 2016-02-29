# Two Pointers (Easy)
# Implement strStr().
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None or len(needle) > len(haystack):
            return -1

        m, n = len(haystack), len(needle)
        for i in range(0, m-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1