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
 *
 * Solutions:
 * 1. BFS with overwrite the input (in-place update)
 *   Starting from the top-left cell, visit all OPEN cells and update its distance from the beginning.
 *   Update matrix in-place to help track distance and avoid revisits.
 *   Note: no need to do level-order traversal since we store distance in the matrix.
 *   Time Complexity O(V) - visit all nodes at most once.
 *   Space Complexity O(V) - store all nodes in the queue
 * 2. BFS w/o overwrite the input
 *    2.1 Can restore the matrix at the end by replacing all cell values greater than 1 to 0.
 *    2.2 Track visited cells separately and follow level order traversal to track distance
 *    Time Complexity O(V) - visit all nodes at most once.
 *    Space Complexity O(V) - store all nodes in the queue
 */

private const val OPEN = 0
private const val CLOSED = 1
private val DIRECTIONS = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1),
    intArrayOf(-1, -1), intArrayOf(-1, 1), intArrayOf(1, -1), intArrayOf(1, 1))

private fun shortestPathBinaryMatrixBFSInPlace(grid: Array<IntArray>): Int {
    var result = -1

    // handle edge cases
    val m = grid.size
    if (m == 0) return result
    val n = grid[0].size
    if (n == 0 || grid[0][0] == CLOSED || grid[m-1][n-1] == CLOSED) return result

    // set up BFS
    val queue = ArrayDeque<IntArray>()
    queue.add(intArrayOf(0, 0))
    grid[0][0] = 1

    // carry out BFS
    while (queue.isNotEmpty()) {
        val cell = queue.removeFirst()
        val distance = grid[cell[0]][cell[1]]
        if (cell[0] == m-1 && cell[1] == n-1) {
            result = distance
            break
        }

        for (neighbor in getNeighbors(cell[0], cell[1], grid)) {
            grid[neighbor[0]][neighbor[1]] = distance+1
            queue.add(neighbor)
        }
    }
    // The target was unreachable.
    return result
}

private fun getNeighbors(row: Int, col: Int, grid: Array<IntArray>): List<IntArray> {
    val neighbors = mutableListOf<IntArray>()
    for (direction in DIRECTIONS) {
        val newRow = row + direction[0]
        val newCol = col + direction[1]
        if (newRow < 0|| newRow >= grid.size || newCol < 0|| newCol >= grid[0].size || grid[newRow][newCol] != OPEN) {
            continue
        }
        neighbors.add(intArrayOf(newRow, newCol))
    }
    return neighbors
}

private fun shortestPathBinaryMatrixBFSNotInPlace(grid: Array<IntArray>): Int {
    val result = -1

    // handle edge cases
    val m = grid.size
    if (m == 0) return result
    val n = grid[0].size
    if (n == 0 || grid[0][0] == CLOSED || grid[m-1][n-1] == CLOSED) return result

    // set up BFS
    val queue = ArrayDeque<IntArray>()
    queue.add(intArrayOf(0, 0))
    val visited = Array<BooleanArray>(m) { BooleanArray(n) }
    var distance = 1

    while (queue.isNotEmpty()) {
        var count = queue.size
        while (count > 0) {
            val cell = queue.removeFirst()
            if (cell[0] == m-1 && cell[1] == n-1) {
                return distance
            }
            for (neighbor in getNeighbors(cell[0], cell[1], grid, visited)) {
                visited[neighbor[0]][neighbor[1]] = true
                queue.add(neighbor)
            }
            count--
        }
        distance++
    }
    return result
}

private fun getNeighbors(row: Int, col: Int, grid: Array<IntArray>, visited: Array<BooleanArray>): List<IntArray> {
    val neighbors = mutableListOf<IntArray>()
    for (direction in DIRECTIONS) {
        val newRow = row + direction[0]
        val newCol = col + direction[1]
        if (newRow < 0|| newRow >= grid.size || newCol < 0|| newCol >= grid[0].size || grid[newRow][newCol] != OPEN ||
            visited[newRow][newCol]) {
            continue
        }
        neighbors.add(intArrayOf(newRow, newCol))
    }
    return neighbors
}



fun main() {
    val matrix1 = arrayOf(intArrayOf(0,1), intArrayOf(1,0))
    println(shortestPathBinaryMatrixBFSNotInPlace(matrix1))
    println(shortestPathBinaryMatrixBFSInPlace(matrix1))

    val matrix2 = arrayOf(intArrayOf(0,0,0), intArrayOf(1,1,0), intArrayOf(1,1,0))
    println(shortestPathBinaryMatrixBFSNotInPlace(matrix2))
    println(shortestPathBinaryMatrixBFSInPlace(matrix2))

    val matrix3 = arrayOf(intArrayOf(1,0,0), intArrayOf(1,1,0), intArrayOf(1,1,0))
    println(shortestPathBinaryMatrixBFSNotInPlace(matrix3))
    println(shortestPathBinaryMatrixBFSInPlace(matrix3))
}
