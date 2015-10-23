# 10/21 - Math
# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
# For example: Given n = 13, Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
# First Trial - fail (Tough to understand)
#   wrong to consider 235 = 200 + 30 + 5. higher digit influence number of 1s for lower digits.


class Solution(object):
    # Test on LeetCode - 36ms
    # Idea - similar as below. count 1s for each digit.
    #   use (a + 8) / 10 to solve cases when a == 0 or a == 1. if a > 1, return 1; else, return 0.
    def count_digit_one_nice(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones, m = 0, 1
        while m <= n:
            a, b = n / m, n % m
            ones += (a + 8) / 10 * m
            ones += (a % 10 == 1) * (b + 1)
            m *= 10
        return ones

    # Test on LeetCode - 48ms
    # Idea: use counting printicple
    #   for every digit in n, count the number of 1s for each digit.
    #   n = 235, count = 154
    #   count 1s digit:
    #       cur = 5, highn = 23, lown = 0, lowc = 1
    #       count += (highn + 1) * lowc => curn > 1, have 24 times of 1 digit as 1, and each 1 counts as 1 times.
    #       24 => 1...91, 101...191, 201, 211, 221, 231 (10 + 10 + 4)
    #   count 10s digit:
    #       curn = 3, highn = 2, lown = 5, lowc = 10
    #       count += (highn + 1) * lowc => curn > 1, have 3 times of 10 digit as 1, and each 1 counts as 10 times.
    #       30 => 10...19, 110...119, 210...219 (the 10s digit)
    #   count 100s digit:
    #       curn = 2, highn = 0, lown = 35, lowc = 100
    #       count += lowc => curn > 1, have 1 times of 100 digit as 1, and each 1 counts as 100 times.
    #       100 => 100...199
    #   total_count = 24 + 30 + 100 = 154
    def count_digit_one_counting_principle(self, n):
        count = 0
        highn, lown, lowc = n, 0, 1
        while highn > 0:
            curn = highn % 10
            highn /= 10
            count += highn * lowc
            if curn > 1:
                count += lowc
            elif curn == 1:
                count += lown + 1
            lown += curn * lowc
            lowc *= 10
        return count


def main():
    test = Solution()
    print test.count_digit_one_counting_principle(235)
    print test.count_digit_one_nice(235)


if __name__ == '__main__':
    main()







