
import kotlin.collections.ArrayDeque
import kotlin.collections.contentToString
import kotlin.collections.forEach
import kotlin.collections.isNotEmpty
import kotlin.collections.removeFirst


/**
 * You are given an m x n grid rooms initialized with these three possible values.
 *
 *   -1 A wall or an obstacle.
 *   0 A gate.
 *   INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that
 *   the distance to a gate is less than 2147483647.
 *
 * Fill each empty room with the distance to its nearest gate.
 * If it is impossible to reach a gate, it should be filled with INF.
 *
 * Solutions:
 *   1. Brute Force from Room to Gate
 *      O(M^2*N^2) Time Complexity & O(M*N) Space Complexity
 *   2. Gate to Room with BFS
 *      O(M*N) Time Complexity & O(M*N) Space Complexity
 */

private const val EMPTY: Int = Int.MAX_VALUE
private const val GATE = 0
private val DIRECTIONS = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
private fun wallsAndGates(rooms: Array<IntArray>): Unit {
    val m = rooms.size
    if (m == 0) return
    val n = rooms[0].size

    // find all gates
    val queue = ArrayDeque<IntArray>()
    for (row in 0 until m) {
        for (col in 0 until n) {
            if (rooms[row][col] == GATE) {
                queue.add(intArrayOf(row, col))
            }
        }
    }

    // assign distance starting from gate using BFS
    while (queue.isNotEmpty()) {
        val cell = queue.removeFirst()
        val row = cell[0]
        val col = cell[1]
        val newDistance = rooms[row][col] + 1
        // find all possible neighbors and assign distance if applicable
        for (direction in DIRECTIONS) {
            val r = row + direction[0]
            val c = col + direction[1]
            if (r < 0 || c < 0 || r >= m || c >= n || rooms[r][c] < newDistance) {
                continue
            }
            rooms[r][c] = newDistance
            queue.add(intArrayOf(r, c))
        }
    }
}

fun main() {
    val rooms: Array<IntArray> = arrayOf(
        intArrayOf(EMPTY, -1, 0, EMPTY),
        intArrayOf(EMPTY, EMPTY, EMPTY, -1),
        intArrayOf(EMPTY, -1, EMPTY, -1),
        intArrayOf(0, -1, EMPTY, EMPTY))
    wallsAndGates(rooms)
    rooms.forEach { println(it.contentToString()) }
}
