# 7/6 - Array
class RotateImage:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.

    # Test on LeetCode - 44ms
    # Idea: find pattern of swaping indexes
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(0, n/2):
            for j in range(i, n-i-1):
                sm, sn = i, j
                src = matrix[sm][sn]
                for k in range(0, 4):
                    em, en = sn, n-1-sm
                    des = matrix[em][en]
                    matrix[em][en] = src
                    sm, sn = em, en
                    src = des
        return matrix

    # Idea:
    #   1. reverse the matrix
    #   2. swap the bottoms with the right
    def rotate_swap(self, matrix):
        matrix.reverse()
        for i in range(0, len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix


def main():
    test = RotateImage()
    print test.rotate([[1,2], [3,4]])
    print test.rotate([[1,2,3], [4,5,6], [7,8,9]])
    print test.rotate_swap([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])


if __name__ == '__main__':
    main()