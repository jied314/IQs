package arrayAndString


/**
 * Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
 *
 * Solutions:
 * 1. Diagonal iteration and reversal
 *    Instead of diagonally traverse the matrix, visit the diagonal starting at the first row and the last column.
 *  Reverse the elements at the even numbered diagonal, e.g. (0, 2)
 *    Time Complexity O(M*N) - traverse the whole matrix
 *    Space Complexity O(min(M, N)) - for storing intermediate array which has max length min(M, N)
 *
 * 2. Simulation
 *    2.1 diagonal visit: UP (-1, +1), DOWN (+1, -1)
 *    2.2 new head: if cannot move upward, move right or down; if cannot move downward, move down or right;
 *    Time Complexity O(M*N) - traverse the whole matrix
 *    Space Complexity O(1)
 */

private fun findDiagonalOrderReverse(mat: Array<IntArray>): IntArray {
    val m = mat.size
    if (m == 0) return IntArray(0)
    val n = mat[0].size

    var row = 0
    var col = 0
    var index = 0
    val intermediate = mutableListOf<Int>()
    val result = IntArray(m*n)

    // visit all diagonals starting from the first row and the last column
    while (row < m && col < n) {
        intermediate.clear()

        // visit the diagonal
        var dRow = row
        var dCol = col
        while (dRow >= 0 && dCol >= 0 && dRow < m && dCol < n) {
            intermediate.add(mat[dRow++][dCol--])
        }
        // reverse even numbered diagonals
        if ((row+col) % 2 == 0) intermediate.reverse()
        for (item in intermediate) result[index++] = item

        if (col == n-1) row++
        else col++
    }
    return result
}

/**
 * tail = [i, j]
 * if direction == up, then {
 *    if [i, j + 1] is within bounds, then {
 *        next_head = [i, j + 1]
 *    } else {
 *        next_head = [i + 1, j]
 *    }
 * } else {
 *    if [i + 1, j] is within bounds, then {
 *        next_head = [i + 1, j]
 *    } else {
 *        next_head = [i, j + 1]
 *    }
 * }
 */
private fun findDiagonalOrderSimulation(mat: Array<IntArray>): IntArray {
    val m = mat.size
    if (m == 0) return IntArray(0)
    val n = mat[0].size

    val result = IntArray(m*n)
    var direction: DIRECTION = DIRECTION.UP
    var row = 0
    var col = 0
    var index = 0
    while (index < m*n) {
        result[index++] = mat[row][col]
        if (direction == DIRECTION.UP) {
            if (isWithin(row-1, m, col+1, n)) { // move upward diagonally
                row--
                col++
            } else { // change head
                direction = DIRECTION.DOWN
                if (isWithin(row, m, col+1, n)) col++ else row++
            }
        } else { // DOWN
            if (isWithin(row+1, m, col-1, n)) { // move downward diagonally
                row++
                col--
            } else { // change head
                direction = DIRECTION.UP
                if (isWithin(row+1, m, col, n)) row++ else col++
            }
        }
    }
    return result
}

private fun isWithin(row: Int, numRow: Int, col: Int, numCol: Int): Boolean {
    return row >= 0 && col >= 0 && row < numRow && col < numCol
}

enum class DIRECTION { UP, DOWN }

fun main() {
    val mat1 = arrayOf(intArrayOf(1,2,3), intArrayOf(4,5,6), intArrayOf(7,8,9))
    println(findDiagonalOrderReverse(mat1).contentToString())
    println(findDiagonalOrderSimulation(mat1).contentToString())
}