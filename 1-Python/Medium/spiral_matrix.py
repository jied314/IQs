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

    def spiral_order(self, matrix):



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