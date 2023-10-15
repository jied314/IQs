# 8/4 - Hash Table, Sort
# Given two strings s and t, write a function to determine if t is an anagram of s.
# Solution:
#   1) Hash Table
#   2) Array
class ValidAnagram:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    # Test on LeetCode - 88ms
    def is_anagram_hash_table(self, s, t):
        if s is not None and t is not None and len(s) != len(t):
            return False
        dic = {}
        for i in range(0, len(s)):
            c = s[i]
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
        for i in range(0, len(t)):
            c = t[i]
            if c in dic and dic[c] > 0:
                dic[c] -= 1
            else:
                return False
        return True

    # Test on LeetCode - 96ms
    def is_anagram_array(self, s, t):
        if s is not None and t is not None and len(s) != len(t):
            return False
        array = [0 for i in range(0, 26)]
        for i in range(0, len(s)):
            c = s[i]
            array[ord(c) - ord('a')] += 1
        for i in range(0, len(t)):
            index = ord(t[i]) - ord('a')
            if array[index] == 0:
                return False
            else:
                array[index] -= 1
        return True

def main():
    test = ValidAnagram()
    test.is_anagram('ab', 'ba')


if __name__ == '__main__':
    main()