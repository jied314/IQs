# 10/10 - Math, Binary Search (M)
# Implement pow(x, n).


class Pow(object):
    # Test on LeetCode - 40ms
    # Idea:
    # Divide and Conquer
    #   if n is even, T(a, n) = T(a, n/2) * T(a, n/2). if n is odd, T(a, n) = a * T(a, n/2) * T(a, n/2)
    # Complexity - Time O(lgN)
    def my_pow_divide_and_conquer(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1.0 / self.power(x, -n)
        return self.power(x, n)

    def power(self, x, n):
        if n == 0:
            return 1
        sqrt = self.power(x, n / 2)
        if n & 1:  # odd
            return x * sqrt * sqrt
        else:  # even
            return sqrt * sqrt

    # Test on LeetCode - 44ms
    # Idea:
    #   compute the right square root
    #   n = 7, 1 + 2 + 4
    def my_pow_iterative(self, x, n):
        if n < 0:
            return 1.0 / self.my_pow_iterative(x, -n)
        result = 1
        product = x
        while n > 0:
            if n & 1:  # odd
                result *= product
            product *= product
            n >>= 1
        return result


def main():
    test = Pow()
    print test.my_pow_iterative(2, 7)
    print test.my_pow_divide_and_conquer(2, 7)


if __name__ == '__main__':
    main()