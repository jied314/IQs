# 7/30 - Data Structure, Trie
# Test on LeetCode - 388ms
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.val = ''
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for character in word:
            if character not in node.children:
                child_node = TrieNode()
                node.children[character] = child_node
            node = node.children[character]
        node.val = word

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.find_position(word)
        if node is not None:
            if node.val == word:
                return True
        return False

    def find_position(self, word):
        node = self.root
        for character in word:
            if character not in node.children:
                return None
            else:
                node = node.children[character]
        return node

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.find_position(prefix)
        if node is not None:
            return True
        return False


# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
