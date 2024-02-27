package Graph

/**
 * Optimized implementation for UnionFind with path compression & union by rank
 * All operations are considered O(1) on average
 */
class UnionFind(size: Int) {
    private val root: IntArray
    private val rank: IntArray
    private var numGroups: Int

    init {
        numGroups = size
        root = IntArray(size)
        rank = IntArray(size)
        for (i in 0 until size) {
            root[i] = i
            rank[i] = 1
        }
    }

    fun find(x: Int): Int {
        if (root[x] != x) root[x] = find(root[x])
        return root[x]
    }

    fun union(x: Int, y: Int) {
        val rootX = find(x)
        val rootY = find(y)
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                root[rootY] = rootX
            } else if (rank[rootX] < rank[rootY]) {
                root[rootX] = rootY
            } else {
                root[rootY] = rootX
                rank[rootX] += 1
            }
            numGroups--
        }
    }

    fun connected(x: Int, y: Int): Boolean {
        return find(x) == find(y)
    }

    fun getNumGroups(): Int = numGroups
}

internal class DisjointSetWithQuickFind(size: Int) {

    private var root: IntArray

    init {
        root = IntArray(size)
        for (i in 0 until size) {
            root[i] = i
        }
    }

    // O(1) Time Complexity
    fun find(x: Int): Int {
        return root[x]
    }

    // O(N) Time Complexity - mark all y's connected vertexes with rootX
    fun union(x: Int, y: Int) {
        val rootX = find(x)
        val rootY = find(y)
        if (rootX != rootY) {
            for (i in 0 until root.size) {
                if (root[i] == rootY) {
                    root[i] = rootX
                }
            }
        }
    }

    // O(1) Time Complexity
    fun connected(x: Int, y: Int): Boolean {
        return find(x) == find(y)
    }
}

internal class DisjointSetWithQuickUnion(size: Int) {

    private var root: IntArray

    init {
        root = IntArray(size)
        for (i in 0 until size) {
            root[i] = i
        }
    }

    // Worst Time Complexity O(N) - recursively find x's root
    fun find(x: Int): Int {
        var y = x
        while (y != root[y]) {
            y = root[y]
        }
        return y
    }

    // Optimized to mark all x's connected vertexes with root to avoid a long chain (e.g. 0-1-2-3-4 -> 0-0-0-0-0)
    // Average O(LogN) Time Complexity
    fun findWithPathCompression(x: Int): Int {
        if (root[x] != x) root[x] = findWithPathCompression(root[x])
        return root[x]
    }

    // Worst Time Complexity O(N)
    fun union(x: Int, y: Int) {
        val rootX = find(x)
        val rootY = find(y)
        if (rootX != rootY) {
            root[rootY] = rootX
        }
    }

    // Worst Time Complexity O(N)
    fun connected(x: Int, y: Int): Boolean {
        return find(x) == find(y)
    }
}

internal class UnionFindByRank(size: Int) {
    private val root: IntArray
    private val rank: IntArray

    init {
        root = IntArray(size)
        rank = IntArray(size)
        for (i in 0 until size) {
            root[i] = i
            rank[i] = 1
        }
    }

    // O(LogN) Time Complexity
    fun find(x: Int): Int {
        var y = x
        while (y != root[y]) {
            y = root[y]
        }
        return y
    }

    // O(LogN) Time Complexity - choose the node with higher rank as the root to avoid long chain
    fun union(x: Int, y: Int) {
        val rootX = find(x)
        val rootY = find(y)
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                root[rootY] = rootX
            } else if (rank[rootX] < rank[rootY]) {
                root[rootX] = rootY
            } else {
                root[rootY] = rootX
                rank[rootX] += 1
            }
        }
    }

    // O(LogN) Time Complexity
    fun connected(x: Int, y: Int): Boolean {
        return find(x) == find(y)
    }
}

fun main() {
    val quickFind = DisjointSetWithQuickFind(10)
    // 1-2-5-6-7 3-8-9 4
    // 1-2-5-6-7 3-8-9 4
    quickFind.union(1, 2)
    quickFind.union(2, 5)
    quickFind.union(5, 6)
    quickFind.union(6, 7)
    quickFind.union(3, 8)
    quickFind.union(8, 9)
    println(quickFind.connected(1, 5)) // true
    println(quickFind.connected(5, 7)) // true
    println(quickFind.connected(4, 9)) // false

    // 1-2-5-6-7 3-8-9-4
    // 1-2-5-6-7 3-8-9-4
    quickFind.union(9, 4)
    println(quickFind.connected(4, 9)) // true

    val quickUnion = DisjointSetWithQuickUnion(10)
    // 1-2-5-6-7 3-8-9 4
    // 1-2-5-6-7 3-8-9 4
    quickUnion.union(1, 2)
    quickUnion.union(2, 5)
    quickUnion.union(5, 6)
    quickUnion.union(6, 7)
    quickUnion.union(3, 8)
    quickUnion.union(8, 9)
    println(quickUnion.connected(1, 5)) // true
    println(quickUnion.connected(5, 7)) // true
    println(quickUnion.connected(4, 9)) // false

    // 1-2-5-6-7 3-8-9-4
    // 1-2-5-6-7 3-8-9-4
    quickUnion.union(9, 4)
    println(quickUnion.connected(4, 9))
}
