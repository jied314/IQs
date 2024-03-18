package Tree.trie

class Trie {

    private val root = TrieNode()

    fun insert(word: String) {
        var node = root
        for (c in word) {
            if (!node.children.containsKey(c)) node.children[c] = TrieNode()
            node = node.children[c]!!
        }
        node.isWord = true
    }

    fun search(word: String): Boolean {
        val tail = trace(word)
        return tail != null && tail.isWord
    }

    fun startsWith(prefix: String): Boolean {
        val tail = trace(prefix)
        return tail != null
    }

    private fun trace(word: String): TrieNode? {
        var node = root
        for (c in word) {
            if (!node.children.containsKey(c)) return null
            node = node.children[c]!!
        }
        return node
    }

    internal class TrieNode {
        var isWord: Boolean = false
        val children = mutableMapOf<Char, TrieNode>()
    }
}

fun main() {
    val trie = Trie()
    trie.insert("apple")
    println(trie.search("apple")) // return True

    println(trie.search("app")) // return False

    println(trie.startsWith("app")) // return True

    trie.insert("app")
    println(trie.search("app")) // return True

}
