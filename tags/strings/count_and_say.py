# The count-and-say sequence is the sequence of integers beginning as follows: 1, 11, 21, 1211, 111221, ...
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
# Note: The sequence of integers will be represented as a string.


class Solution(object):
    # Note:
    #   handle the last character in the string
    def count_and_say(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""
        ret = "1"
        i = 1
        while i < n:
            temp = ""
            j, k, c = 0, 0, ret[0]
            while j < len(ret)+1:
                if j == len(ret) or ret[j] != c:
                    temp += str(j-k)
                    temp += c
                    if j == len(ret):
                        break
                    k, c = j, ret[j]
                j += 1
            ret = temp
            i += 1
        return ret


test = Solution()
print test.count_and_say(4)
