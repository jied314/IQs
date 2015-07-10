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


def main():
    test = SpiralMatrix2()
    print test.generate_matrix(4)


if __name__ == '__main__':
    main()
