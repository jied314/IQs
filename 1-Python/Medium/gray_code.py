# 7/4 - Backtracking
# The gray code is a binary numeral system where two successive values differ in only one bit.
class GrayCode:
    # @param {integer} n
    # @return {integer[]}
    # Test on LeetCode - 60ms
    def gray_Code(self, n):
        nums = [0]
        if n > 0:
            nums.append(1)
            for i in range(2, n+1):
                base = 2 ** (i - 1)  # or use 1 << i
                for j in range(base-1, -1, -1):
                    nums.append(base + nums[j])
        return nums


def main():
    test = GrayCode()
    print test.gray_Code(0)
    print test.gray_Code(1)
    print test.gray_Code(2)
    print test.gray_Code(3)
    print test.gray_Code(4)


if __name__ == '__main__':
    main()