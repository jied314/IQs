package Graph

/**
 * Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
 * If there is no clear path, return -1.
 *
 * A clear path in a binary matrix is a path from the top-left cell i.e., (0, 0)) to the bottom-right cell
 * (i.e., (n - 1, n - 1)) such that:
 *   All the visited cells of the path are 0.
 *   All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge
 * or a corner).
 *
 * The length of a clear path is the number of visited cells of this path.
 */

private const val GATE = 0
private const val WALL = 1
private val DIRECTIONS = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1),
    intArrayOf(-1, -1), intArrayOf(-1, 1), intArrayOf(1, -1), intArrayOf(1, 1))
private fun shortestPathBinaryMatrix(grid: Array<IntArray>): Int {
    val m = grid.size
    val n = grid[0].size
    val queue = ArrayDeque<IntArray>()
    if (grid[0][0] == GATE) {
        grid[0][0] = WALL
        queue.add(intArrayOf(0, 0))
    }
    var result = -1
    var levelCount = 0
    while (queue.isNotEmpty()) {
        levelCount++
        val size = queue.size
        for (i in 1..size) {
            val cell = queue.removeFirst()
            for (direction in DIRECTIONS) {
                val row = cell[0] + direction[0]
                val col = cell[1] + direction[1]
                if (row in 0..<m && col in 0..< n && grid[row][col] == GATE) {
                    if (row == m-1 && col == n-1) {
                        result = levelCount+1
                        return result
                    }
                    grid[row][col] = WALL
                    queue.add(intArrayOf(row, col))
                }
            }
        }
    }
    return result
}

fun main() {
    val matrix1 = arrayOf(intArrayOf(0,1), intArrayOf(1,0))
    println(shortestPathBinaryMatrix(matrix1))

    val matrix2 = arrayOf(intArrayOf(0,0,0), intArrayOf(1,1,0), intArrayOf(1,1,0))
    println(shortestPathBinaryMatrix(matrix2))

    val matrix3 = arrayOf(intArrayOf(1,0,0), intArrayOf(1,1,0), intArrayOf(1,1,0))
    println(shortestPathBinaryMatrix(matrix3))
}
