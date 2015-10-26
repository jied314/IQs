# 10/25 - BackTracking, Trie, Design
# Design a data structure that supports the following two operations:
#   void addWord(word)
#   bool search(word)
#   search(word) can search a literal word or a regular expression string containing only letters a-z or .. A .
# means it can represent any one letter.
# For example:
#   addWord("bad")
#   addWord("dad")
#   addWord("mad")
#   search("pad") -> false
#   search("bad") -> true
#   search(".ad") -> true
#   search("b..") -> true
# Note:
#   You may assume that all words are consist of lowercase letters a-z.
#
# Third Trial Passes
# Borrow ideas from Implement Trie (Prefix Tree)


class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.val = ''
        self.children = {}


class WordDictionary(object):
    # Test on LeetCode - 568ms
    # Use TrieNode
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def add_word(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            children = node.children
            if c not in children:
                children[c] = TrieNode()
            node = children[c]
        node.val = word

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.search_word(self.root, word, 0, len(word))

    def search_word(self, node, word, index, length):
        if index == length:
            if len(node.val) == len(word):
                return True
            return False
        children = node.children
        if len(children) == 0:
            return False
        c = word[index]
        if c in children:  # c exists
            return self.search_word(children[c], word, index+1, length)
        else:  # c not exist
            if c == ".":
                for key, val in children.iteritems():
                    if self.search_word(val, word, index+1, length):
                        return True
            return False
        

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.add_word("at")
wordDictionary.add_word("and")
wordDictionary.add_word("an")
wordDictionary.add_word("add")
print wordDictionary.search("a")
print wordDictionary.search(".at")
wordDictionary.add_word("bat")
print wordDictionary.search(".at")
print wordDictionary.search("an.")
print wordDictionary.search("a.d.")
print wordDictionary.search("b.")
print wordDictionary.search("a.d")
print wordDictionary.search(".")