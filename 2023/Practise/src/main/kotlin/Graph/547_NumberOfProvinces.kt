package Graph

/**
 * There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b,
 * and city b is connected directly with city c, then city a is connected indirectly with city c.
 *
 * A province is a group of directly or indirectly connected cities and no other cities outside of the group.
 *
 * You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are
 * directly connected, and isConnected[i][j] = 0 otherwise.
 *
 * Return the total number of provinces.
 *
 * Solutions:
 * 1. Use UnionFind
 *    O(N*N) Time Complexity since the double loop. Operations for optimized UnionFind is O(1) Time.
 *    O(N) Space Complexity
 *    Note: cannot assume the num of unique roots as the number of groups since it may not be updated yet.
 *
 * 2. Use Graph DFS - start from an unvisited node, recursively search for unvisited vertex
 *    O(N*N) Time Complexity & O(N) Space Complexity
 */

private fun findCircleNumUnionFind(isConnected: Array<IntArray>): Int {
    var numGroup = isConnected.size
    val unionFind = UnionFind(isConnected.size)
    for (i in 0..<isConnected.size) {
        for (j in i+1..<isConnected.size) {
            if (isConnected[i][j] == 1 && !unionFind.connected(i, j)) {
                numGroup--
                unionFind.union(i, j)
            }
        }
    }
    return numGroup
}

private fun findCircleNumDFS(isConnected: Array<IntArray>): Int {
    var numberOfComponents = 0
    val visit = BooleanArray(isConnected.size)
    for (i in 0 until isConnected.size) {
        if (!visit[i]) {
            numberOfComponents++
            dfs(i, isConnected, visit)
        }
    }
    return numberOfComponents
}

private fun dfs(node: Int, isConnected: Array<IntArray>, visit: BooleanArray) {
    visit[node] = true
    for (i in isConnected.indices) {
        if (isConnected[node][i] == 1 && !visit[i]) {
            dfs(i, isConnected, visit)
        }
    }
}

fun main() {
    val isConnected = arrayOf(
        intArrayOf(1,0,0,1),
        intArrayOf(0,1,1,0),
        intArrayOf(0,1,1,1),
        intArrayOf(1,0,1,1)
    )
    println(findCircleNumUnionFind(isConnected))
}