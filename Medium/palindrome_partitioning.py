# 10/9 - Backtracking (M)
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.
# For example, given s = "aab",
# Return [ ["aa","b"], ["a","a","b"] ]
# 
class PalindromePartitioning(object):
    # Test on LeetCode - 72ms
    # Idea:
    #   use dp to store all palindrome substring
    #   palindrome prefix + palindrome suffix
    def partition_dp_dfs(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if s is None or len(s) == 0:
            return [[]]
        palindrome = set()
        self.find_palindrome_substrings(palindrome, s)
        return self.partition_recursive(palindrome, s)

    # find all substring that is palindrome
    def find_palindrome_substrings(self, palindrome, s):
        length = len(s)
        for i in range(0, length):  # substring length - 1
            for j in range(0, length):  # substring starting position
                end = i + j + 1
                if end <= length:
                    substring = s[j:end]
                    if substring not in palindrome and self.is_palindrome(substring):
                        palindrome.add(substring)

    # O(N) = palindrome(prefix) + O(suffix)
    def partition_recursive(self, palindrome, s):
        ret = []
        length = len(s)
        if s in palindrome:
            ret.append([s])
        for i in range(1, length):
            prefix = s[0:i]
            if prefix in palindrome:  # prefix has to be a palindrome
                suffixes = self.partition_recursive(palindrome, s[i:length])
                for suffix in suffixes:
                    ret.append([prefix] + suffix)
        return ret

    # check if a string is a palindrome
    # O(N)
    def is_palindrome(self, s):
        length = len(s)
        if length == 0:
            return False
        result = True
        for i in range(0, length / 2):
            if s[i] != s[length - 1 - i]:
                result = False
                break
        return result

    # simpler version
    def is_palindrome_two_pointers(self, s):
        start, end = 0, len(s) - 1
        result = True
        while start < end:
            if s[start] != s[end]:
                result = False
                break
            start += 1
            end -= 1
        return result

def main():
    test = PalindromePartitioning()
    print test.partition_dp_dfs("")
    print test.partition_dp_dfs("a")
    print test.partition_dp_dfs("aab")
    print test.partition_dp_dfs("abbaa")

if __name__ == '__main__':
    main()
