# 10/20 - DP, Heap, Math
# Write a program to find the n-th ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note that 1 is typically treated as an ugly number.
# Idea:
#   Naive - call isUgly() for every number until you reach the nth one. not very efficient since most of the numbers
#           are not ugly. Time O(Nlgn)
#   DP - nice


class UglyNumber2(object):
    # Idea:
    #   use heap structure to maintain the order
    #   in each loop, pop min, multiply by 2, 3, 5 and add back to the heap
    #   stop when reaching n. the poped one is the nth number.
    #   not very efficient since actually visiting greater than nth number, but the logic is clear
    def nth_ugly_number_heap(self, n):
        """
        :type n: int
        :rtype: int
        """

    # Test on LeetCode - 79ms
    # Idea - DP:
    #   U(k+1) = Min(L1*2, L2*3, L3*5)
    #   keep three pointers into the visiting number for 2, 3, 5
    # Time Complexity O(N), Space Complexity O(N)
    # i2, i3, i5 used to record the min index that hasn't multiply yet
    def nth_ugly_number_dp(self, n):
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        next_multiply_of_2 = 2
        next_multiply_of_3 = 3
        next_multiply_of_5 = 5
        for i in range(1, n):
            next_ugly = min(next_multiply_of_2, next_multiply_of_3, next_multiply_of_5)
            ugly.append(next_ugly)
            if next_ugly == next_multiply_of_2:
                i2 += 1
                next_multiply_of_2 = ugly[i2] * 2
            if next_ugly == next_multiply_of_3:
                i3 += 1
                next_multiply_of_3 = ugly[i3] * 3
            if next_ugly == next_multiply_of_5:
                i5 += 1
                next_multiply_of_5 = ugly[i5] * 5
        return ugly[-1]


def main():
    test = UglyNumber2()
    print test.nth_ugly_number_dp(7)


if __name__ == '__main__':
    main()