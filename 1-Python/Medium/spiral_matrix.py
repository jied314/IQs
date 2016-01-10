# 10/23 -

class SpiralMatrix(object):

    # Test on LeetCode - 40ms
    # Idea:
    #   copy the first row, then traverse the rest.
    #   calculate steps for each direction. m-1, n-1, m-2, n-2, ..., until step == 0.
    #   use two flags move_left and move_right to remember visiting direction
    def spiral_order(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        if matrix is None or len(matrix) == 0:
            return ret

        for e in matrix[0]:
            ret.append(e)  # copy the first row
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        move_left, move_down = True, True
        while True:
            m -= 1
            if m == 0:
                break
            if move_down:
                start, end, step = i + 1, i + 1 + m, 1
            else:
                start, end, step = i - 1, i - 1 - m, -1
            for i in range(start, end, step):
                ret.append(matrix[i][j])
            move_down = not move_down

            n -= 1
            if n == 0:
                break
            if move_left:
                start, end, step = j - 1, j - 1 - n, -1
            else:
                start, end, step = j + 1, j + 1 + n, 1
            for j in range(start, end, step):
                ret.append(matrix[i][j])
            move_left = not move_left
        return ret

    # 1/9 - Revisit
    # Borrow idea from Yanxing - Test on LC 40ms
    # Calculate steps for each spiral visit (n-1 & m-1), then calculate the corresponding indexes.
    # Use k to denote which rounds of spiral visit
    # Note matrix size decreases after each spiral visit. Note edge cases when m == 1 or n == 1
    def spiral_order_revisit(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        m, n = len(matrix), len(matrix[0])
        ret = []
        self.solve(matrix, ret, m, n, 0)
        return ret

    # for each call to solve, matrix sizes decreases.
    # height = [k...m+k-1], width = [k...k+n-1]
    # Edge case:
    #   if m > 1 and n > 1, must have a full round spiral visit
    def solve(self, matrix, ret, m, n, k):
        if m <= 0 or n <= 0:
            return
        if m == 1:
            for i in range(0, n):
                ret.append(matrix[k][k+i])
            return
        if n == 1:
            for i in range(0, m):
                ret.append(matrix[k+i][k])
            return
        for i in range(0, n-1):
            ret.append(matrix[k][k+i])
        for i in range(0, m-1):
            ret.append(matrix[k+i][k+n-1])
        for i in range(0, n-1):
            ret.append(matrix[k+m-1][k+n-1-i])
        for i in range(0, m-1):
            ret.append(matrix[k+m-1-i][k])
        self.solve(matrix, ret, m-2, n-2, k+1)



def main():
    test = SpiralMatrix()
    matrix = [[1],
              [5],
              [9],
              [1],
              [5]]
    print test.spiral_order(matrix)


if __name__ == "__main__":
    main()