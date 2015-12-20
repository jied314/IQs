class ReverseInteger:
    # @param {integer} x
    # @return {integer}
    # Test on LeetCode - 72ms
    def reverse(self, x):
        max = 2 ** 31 - 1
        flag = False
        if x < 0:
            x *= -1
            max = 2 ** 31
            flag = True
        elif x == 0:  # 0
            return x

        result = 0
        num_digit = 0
        while x != 0:
            digit = x % 10
            if num_digit == 9:
                if result * 10 + digit > max:
                    return 0
            result = (result * 10) + digit
            x /= 10
            num_digit += 1
        if flag:
            result *= -1
        return result


def main():
    test = ReverseInteger()
    print test.reverse(10)
    print test.reverse(-1)
    print test.reverse(1534236469)

if __name__ == '__main__':
    main()