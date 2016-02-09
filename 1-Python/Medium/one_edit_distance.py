# 1/15 - Array
# Source - Yanxing (LC Locked)
# Implement a function OneEditApart with the following signature:
#   bool OneEditApart(string s1, string s2)
# For example:
#   isOneEditDistance("cat", "dog") = false
#   isOneEditDistance("cat", "cats") = true
#   isOneEditDistance("cat", "cut") = true
#   isOneEditDistance("cat", "cast") = true
#   isOneEditDistance("cat", "at") = true
#   isOneEditDistance("cat", "acts") = false
# Edit is: insertion, removal, replacement

class Solution(object):
    def is_one_edit_apart(self, s1, s2):
        if len(s1) > len(s2):  # make sure s1 has smaller length
            s1, s2 = s2, s1
        l1, l2 = len(s1), len(s2)
        for i in range(0, min(l1, l2)):
            if s1[i] == s2[i]:
                continue
            if l1 == l2:
                return s1[i+1:] == s2[i+1:]
            else:
                return s1[i:] == s2[i+1:]
        return abs(l1 - l2) == 1  # check at the end for case 4 cat v.s. cast

test = Solution()
print test.is_one_edit_apart("cat", "dog")
print test.is_one_edit_apart("cat", "cats")
print test.is_one_edit_apart("cat", "cut")
print test.is_one_edit_apart("cat", "cast")
print test.is_one_edit_apart("cat", "at")
print test.is_one_edit_apart("cat", "acts")