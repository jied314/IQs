class ClimbingStairs:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        result = []
        for i in range(1, n + 1):
            if i == 1:
                result.append(1)
            elif i == 2:
                result.append(2)
            else:
                value = result[0] + result[1]
                result[0] = result[1]
                result[1] = value
        return result[len(result) - 1]


def main():
    test = ClimbingStairs()
    print test.climbStairs(3)

if __name__ == '__main__':
    main()

