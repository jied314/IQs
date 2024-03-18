package Graph

/**
 * Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
 * The distance between two adjacent cells is 1.
 *
 * Solutions:
 * 1. BFS - instead of regular BFS that starts with one point, we track all eligible starting points (cell[i][j] == 0)
 *          and traverse simultaneously to reduce search space, since we mark visited ones.
 *    Time Complexity O(M*N) - visit all nodes once.
 *    Space Complexity O(M*N) - not update matrix in place and store visit states.
 *
 * 2. Dynamic Programming
 *    Recurrence relation: dp[row][col] = 1 + min(dp[row - 1][col], dp[row + 1][col], dp[row][col - 1], dp[row][col + 1])
 *    But this does not indicate an obvious traversal order of the matrix.
 *    So optimize to 2 traversals:
 *    1. Move down and right: dp[row][col] = 1 + min(dp[row - 1][col], dp[row][col - 1])
 *    2. Move up and left: dp[row][col] = 1 + min(dp[row + 1][col], dp[row][col + 1])
 *
 */

private val DIRECTIONS = arrayOf(intArrayOf(-1, 0), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(0, 1))
private fun updateMatrix(mat: Array<IntArray>): Array<IntArray> {
    val m = mat.size
    if (m == 0) return mat
    val n = mat[0].size
    val matrix = Array<IntArray>(m) { IntArray(n) }
    val seen = Array<BooleanArray>(m) { BooleanArray(n) }
    val queue = ArrayDeque<IntArray>()

    for (i in 0..<m) {
        for (j in 0..<n) {
            matrix[i][j] = mat[i][j]
            if (mat[i][j] == 0) {
                queue.add(intArrayOf(i, j))
                seen[i][j] = true
            }
        }
    }
    var distance = 1
    while (queue.isNotEmpty()) {
        var count = queue.size
        while (count > 0) {
            val cell = queue.removeFirst()
            for (neighbor in getNeighbors(cell[0], cell[1], matrix, seen)) {
                seen[neighbor[0]][neighbor[1]] = true
                matrix[neighbor[0]][neighbor[1]] = distance
                queue.add(neighbor)
            }
            count--
        }
        distance++
    }
    return matrix
}

private fun getNeighbors(row: Int, col: Int, matrix: Array<IntArray>, seen: Array<BooleanArray>): List<IntArray> {
    val neighbors = mutableListOf<IntArray>()
    for (direction in DIRECTIONS) {
        val newRow = row + direction[0]
        val newCol = col + direction[1]
        if (newRow < 0|| newRow >= matrix.size || newCol < 0|| newCol >= matrix[0].size || seen[newRow][newCol]) {
            continue
        }
        neighbors.add(intArrayOf(newRow, newCol))
    }
    return neighbors
}

fun main() {

}
