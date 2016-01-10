# 7/9 - Array
class SpiralMatrix2:
    # @param {integer} n
    # @return {integer[][]}

    # inspired by online solution using direction variable
    def generate_matrix(self, n):
        result = [[]]
        if n:
            result = [[0 for i in range(0, n)] for j in range(0, n)]
            direction = 0
            i, j, k = 0, 0, 1
            while k <= n * n:
                result[i][j] = k
                k += 1
                if direction == 0:  # move right
                    j += 1
                    if j == n or result[i][j]:
                        direction = 1
                        j -= 1
                        i += 1
                elif direction == 1:  # move down
                    i += 1
                    if i == n or result[i][j]:
                        direction = 2
                        j -= 1
                        i -= 1
                elif direction == 2:  # move left
                    j -= 1
                    if j < 0 or result[i][j]:
                        direction = 3
                        j += 1
                        i -= 1
                elif direction == 3:  # move up
                    i -= 1
                    if i < 0 or result[i][j]:
                        direction = 0
                        i += 1
                        j += 1
        return result

    # 12/23 - Revisit
    # Idea:
    #   determine directions and then move
    #   note the edge cases
    def generate_matrix_revisit(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ret = [[0 for i in range(0, n)] for j in range(0, n)]
        num = 1
        top, left, right, bottom = 0, 0, n-1, n-1
        i, j = 0, 0
        while num <= n * n:
            if i == top and j == left:  # move right
                while j <= right:
                    ret[i][j] = num
                    j += 1
                    num += 1
                i += 1
                j -= 1  # need to adjust offset
                top += 1
            elif i == top and j == right:  # move down
                while i <= bottom:
                    ret[i][j] = num
                    i += 1
                    num += 1
                j -= 1
                i -= 1 # need to adjust offset
                right -= 1
            elif i == bottom and j == right:  # move left
                while j >= left:
                    ret[i][j] = num
                    j -= 1
                    num += 1
                i -= 1
                j += 1 # need to adjust offset
                bottom -= 1
            elif i == bottom and j == left:  # move up
                while i >= top:
                    ret[i][j] = num
                    i -= 1
                    num += 1
                j += 1
                i += 1 # need to adjust offset
                left += 1
        return ret

    # Borrow from Yanxing - Test on LC 44ms
    # Idea:
    #   count how many steps for each spiral visit
    #   init matrix with n*n to avoid checking whether n is odd. e.g. n = 3, k = 0, will miss visiting 9.
    def generate_matrix_Yanxing(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        matrix = [[n*n] * n for _ in range(n)]
        count = 0
        for k in range(0, n/2):
            step = n - 1 - (k * 2)
            for i in range(0, step):
                count += 1
                matrix[k][k+i] = count
            for i in range(0, step):
                count += 1
                matrix[k+i][n-k-1] = count
            for i in range(0, step):
                count += 1
                matrix[n-k-1][n-k-1-i] = count
            for i in range(0, step):
                count += 1
                matrix[n-k-1-i][k] = count
        return matrix


def main():
    test = SpiralMatrix2()
    print test.generate_matrix(4)


if __name__ == '__main__':
    main()
