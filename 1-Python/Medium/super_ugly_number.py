# 12/26 - Math, Heap
# Similar to Ugly Number2
# Note:
#   can use Heap to minimize finding min

import copy

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ret = [1]
        length = len(primes)
        indexes = [0] * length
        next_multiplies = copy.deepcopy(primes)
        for i in range(1, n):
            # find min
            next_ugly = next_multiplies[0]
            for j in range(1, length):
                next_ugly = min(next_ugly, next_multiplies[j])
            ret.append(next_ugly)
            # update
            for j in range(0, length):
                if next_ugly == next_multiplies[j]:
                    indexes[j] += 1
                    next_multiplies[j] = primes[j] * ret[indexes[j]]
        return ret[-1]
