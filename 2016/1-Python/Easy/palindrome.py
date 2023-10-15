class Palindrome:
    # @param {string} s
    # @return {boolean}
    # Test on LeetCode - 160ms, memory O(n)
    def is_palindrome_n(self, s):
        if len(s) < 2:
            return True
        chars = []
        for i in range(0, len(s)):
            if ord('a') <= ord(s[i]) <= ord('z') or ord('0') <= ord(s[i]) <= ord('9'):
                chars.append(s[i])
            elif ord('A') <= ord(s[i]) <= ord('Z'):
                chars.append(s[i].lower())
        #print chars
        length = len(chars)
        for i in range(0, length / 2):
            if chars[i] != chars[length - 1 - i]:
                return False
        return True

    # Test on LeetCode - 168ms, memory O(1)
    def is_palindrome_1(self,s):
        if len(s) < 2:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not self.is_valid_alphanumeric(s[i]):
                i += 1
            while i < j and not self.is_valid_alphanumeric(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

    def is_valid_alphanumeric(self, c):
        return ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9')


def main():
    test = Palindrome()
    print test.is_palindrome_1('mam')
    print test.is_palindrome_1('A man, a plan, a canal: Panama')
    print test.is_palindrome_1('race a car')
    print test.is_palindrome_1("0k.;r0.k;")

if __name__ == '__main__':
    main()