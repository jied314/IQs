import kotlin.collections.ArrayDeque
import kotlin.collections.isNotEmpty
import kotlin.collections.removeFirst


/**
 * Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
 * return the number of islands.
 *
 * An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
 * You may assume all four edges of the grid are all surrounded by water.
 *
 * Example:
 * Input: grid = [
 *   ["1","1","1","1","0"],
 *   ["1","1","0","1","0"],
 *   ["1","1","0","0","0"],
 *   ["0","0","0","0","0"]
 * ]
 * Output: 1
 *
 * Solutions:
 * 1. BFS
 *   O(M*N) Time Complexity & O(M*N) Space Complexity
 * 2. DFS with recursion - no need to maintain queue
 *   O(M*N) Time Complexity & O(M*N) Space Complexity
 */

private const val LAND = '1'
private const val WATER = '0'
private val DIRECTIONS = arrayOf(intArrayOf(-1, 0), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(0, 1))

fun numIslandsBFS(grid: Array<CharArray>): Int {
    val m = grid.size
    if (m == 0) return 0
    val n = grid[0].size
    var result = 0

    for (i in 0 until m) {
        for (j in 0 until n) {
            if (grid[i][j] == LAND) {
                result++
                val queue = ArrayDeque<IntArray>()
                queue.add(intArrayOf(i, j))
                while (queue.isNotEmpty()) {
                    val cell = queue.removeFirst()
                    grid[cell[0]][cell[1]] = WATER
                    for (direction in DIRECTIONS) {
                        val r = cell[0] + direction[0]
                        val c = cell[1] + direction[1]
                        if (r < 0 || r >= m || c < 0 || c >= n) continue
                        if (grid[r][c] == LAND) queue.add(intArrayOf(r, c))
                    }
                 }
            }
        }
    }
    return result
}

fun numIslandsDFS(grid: Array<CharArray>): Int {
    val m = grid.size
    if (m == 0) return 0
    val n = grid[0].size
    var result = 0

    for (i in 0 until m) {
        for (j in 0 until n) {
            if (grid[i][j] == LAND) {
                result++
                dfs(grid, i, j)
            }
        }
    }
    return result
}

fun dfs(grid: Array<CharArray>, row: Int, col: Int) {
    val m = grid.size
    val n = grid[0].size

    if (row < 0 || col < 0 || row >= m || col >= n || grid[row][col] == WATER) return

    grid[row][col] = WATER
    dfs(grid, row-1, col)
    dfs(grid, row+1, col)
    dfs(grid, row, col-1)
    dfs(grid, row, col+1)
}

fun main() {
    val grid1 = arrayOf(
        charArrayOf(LAND, LAND, LAND, LAND, WATER),
        charArrayOf(LAND, LAND, WATER, LAND, WATER),
        charArrayOf(LAND, LAND, WATER, WATER, WATER),
        charArrayOf(WATER, WATER, WATER, WATER, WATER)
    )
//    println(numIslandsBFS(grid1))
    println(numIslandsDFS(grid1))

    val grid2 = arrayOf(
        charArrayOf(LAND, LAND, WATER, WATER, WATER),
        charArrayOf(LAND, LAND, WATER, WATER, WATER),
        charArrayOf(WATER, WATER, LAND, WATER, WATER),
        charArrayOf(WATER, WATER, WATER, LAND, LAND)
    )
//    println(numIslandsBFS(grid2))
    println(numIslandsDFS(grid2))
}
