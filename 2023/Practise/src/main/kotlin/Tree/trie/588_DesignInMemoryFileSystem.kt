package Tree.trie

import java.util.TreeMap

/**
 * Design a data structure that simulates an in-memory file system.
 */

class FileSystem {

    val root = Node()

    /**
     * If path is a file path, returns a list that only contains this file's name.
     * If path is a directory path, returns the list of file and directory names in this directory.
     * The answer should be in lexicographic order.
     */
    fun ls(path: String): List<String> {
        var node = root
        val steps = parsePath(path)
        for (step in steps) {
            if (!node.children.containsKey(step)) break
            node = node.children[step]!!
        }
        val result = mutableListOf<String>()
        if (node.isFile) result.add(steps.last)
        else {
            result.addAll(node.children.keys)
        }
        return result
    }

    /**
     * Makes a new directory according to the given path.
     * The given directory path does not exist.
     * If the middle directories in the path do not exist, you should create them as well.
     */
    fun mkdir(path: String) {
        var node = root
        for (step in parsePath(path)) {
            if (!node.children.containsKey(step)) node.children[step] = Node()
            node = node.children[step]!!
        }
    }

    /**
     * If filePath does not exist, creates that file containing given content.
     * If filePath already exists, appends the given content to original content.
     */
    fun addContentToFile(filePath: String, content: String) {
        var node = root
        for (step in parsePath(filePath)) {
            if (!node.children.containsKey(step)) node.children[step] = Node()
            node = node.children[step]!!
        }
        node.isFile = true
        node.content.append(content)
    }

    /**
     * Returns the content in the file at filePath.
     */
    fun readContentFromFile(filePath: String): String {
        var node = root
        for (step in parsePath(filePath)) {
            if (!node.children.containsKey(step)) node.children[step] = Node()
            node = node.children[step]!!
        }
        return node.content.toString()
    }

    private fun parsePath(path: String): List<String> {
        return path.split("/").drop(1)
    }
}

class Node {
    val children = TreeMap<String, Node>()
    var isFile = false
    val content = StringBuilder()
}

fun main() {
    val fs = FileSystem()
    println(fs.ls("/"))                               // return []
    fs.mkdir("/a/b/c")
    fs.addContentToFile("/a/b/c/d", "hello");
    println(fs.ls("/"))                               // return ["a"]
    println(fs.readContentFromFile("/a/b/c/d"))     // return "hello"
}