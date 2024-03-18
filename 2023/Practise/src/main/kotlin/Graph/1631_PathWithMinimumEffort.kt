package Graph

import java.util.*
import kotlin.math.abs

/**
 * You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns,
 * where heights[row][col] represents the height of cell (row, col).
 * You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell,
 * (rows-1, columns-1) (i.e., 0-indexed).
 * You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
 *
 * A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
 *
 * Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
 *
 * Solutions:
 * 1. Dijkstra
 *    Time Complexity O(M*N*Log(M*N)) - at most traverse all cell and interact with heap.
 *    Space Complexity O(M*N) - for visited matrix and heap.
 */

private val DIRECTIONS = arrayOf(intArrayOf(-1, 0), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(0, 1))
private fun minimumEffortPath(heights: Array<IntArray>): Int {
    val m = heights.size
    val n = heights[0].size
    val visited = Array<BooleanArray>(m) { BooleanArray(n) }
    val heap = PriorityQueue<Pair<Int, IntArray>>(compareBy {it.first})
    heap.add(Pair(0, intArrayOf(0, 0)))
    while (heap.isNotEmpty()) {
        val (diff, cell) = heap.remove()
        val row = cell[0]
        val col = cell[1]
        visited[row][col] = true
        if (row == m-1 && col == n-1) return diff
        for ((i, j) in DIRECTIONS) {
            val newRow = row + i
            val newCol = col + j
            if (newRow < 0 || newCol < 0 || newRow >= m || newCol >= n) continue
            if (visited[newRow][newCol]) continue
            val newDiff = Math.max(diff, abs(heights[newRow][newCol] - heights[row][col]))
            heap.add(Pair(newDiff, intArrayOf(newRow, newCol)))
        }
    }
    return -1
}

fun main() {
    val heights1 = arrayOf(intArrayOf(1,2,2), intArrayOf(3,8,2), intArrayOf(5,3,5))
    println(minimumEffortPath(heights1))
}