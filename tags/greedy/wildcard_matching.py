class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.match(s, 0, p, 0)
        
    def match(self, s, i, p, j):
        # both reach end
        if i == len(s) and j == len(p):
            return True
        # exhaust s, but not p
        if i == len(s):  
            while j < len(p) and p[j] == '*':
                j += 1
            return j == len(p)
        # exhaust p, but not s
        if j == len(p) and i < len(s):
            return False
            
        # not exhaust s and p
        if s[i:] == p[j:]:  # rest are the same
            return True
        if s[i] != p[j]:  # not a match
            if p[j] == '?':  # match a character
                return self.match(s, i+1, p, j+1)
            elif p[j] == '*':  # match a sequence, advance i accordingly
                rest = len(p) - j - 1
                if len(s) - rest <= i:
                    i = len(s)
                else:
                    i = len(s) - rest
                return self.match(s, i, p, j+1)
            else:
                return False
        else:
            return self.match(s, i+1, p, j+1)


test = Solution()
print test.isMatch("b", "*?*?")