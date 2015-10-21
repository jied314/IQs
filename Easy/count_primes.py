import math
import time

# 7/16 (Revisit) - HashTable, Math (E)
# Count the number of prime numbers less than a non-negative number, n.
# Solutions:
#   1. count up to square root O(nlgn)
#   2. Sieve of Eratosthenes
#      Mark down non-primes which are multiplies of primes, starting with 2 (3, 5, 7...).
#      Main Problem: memory consumption (use segmented sieve to improve)
#      Complexity:
#       Memory - O(n)
#       Runtime - O(n log log n)
#       Proof: this algorithm basically culls all the non-prime numbers - n * (1/2 + 1/3 + 1/5 + ... + 1/sqrt_n)
#
# Note:
#   Loop's ending condition is i * i < n instead of i < sqrt(n) to avoid repeatedly calling an expensive function sqrt().
#
class CountPrimes:
    # @param {integer} n
    # @return {integer}

    # Test on LeetCode - TLE
    # Time Complexity - O(nlgn)
    def count_primes_square(self, n):
        count = 0
        for i in range(2, n):
            if self.is_prime(i):
                count += 1
        return count

    def is_prime(self, n):
        if n <= 1:
            return False
        sqrt = int(math.sqrt(n))
        for i in range(2, sqrt+1):
            if n % i == 0:
                return False
        return True

    # Test on LeetCode - 1376ms
    def count_primes_sieve(self, n):
        flags = [True for i in range(0, n+1)]  # used to mark whether not visited
        sqrt = int(math.sqrt(n))
        for i in range(2, sqrt+1):
            if flags[i]:
                sqr = i * i  # note: from i*i to n since smaller numbers have been marked
                times = (n - sqr) / i  # more efficient to count num of visits before the for loop
                for j in range(0, times+1):
                    flags[sqr + j * i] = False
        count = 0
        for i in range(2, n):  # note: count primes less than n
            if flags[i]:
                count += 1
        return count


def main():
    test = CountPrimes()
    print 'Use Square Trial Division'
    start = time.clock()
    print test.count_primes_square(13)
    end = time.clock()
    print end - start

    print '\nUse Sieve of Eratosthenes'
    start = time.clock()
    print test.count_primes_sieve(13)
    end = time.clock()
    print end - start

if __name__ == '__main__':
    main()
