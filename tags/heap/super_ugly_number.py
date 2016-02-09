# 12/26 - Math, Heap
# Similar to Ugly Number2
# Note:
#   can use Heap to minimize finding min
import copy
import heapq


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [1]
        length = len(primes)
        indexes = [0] * length
        next_multiplies = copy.deepcopy(primes)
        for i in range(1, n):
            # find min
            next_ugly = min(next_multiplies)
            uglies.append(next_ugly)
            # update
            for j in range(0, length):
                if next_ugly == next_multiplies[j]:
                    indexes[j] += 1
                    next_multiplies[j] = primes[j] * uglies[indexes[j]]
        return uglies[-1]

    # use min_heap to expedite finding min
    def nth_super_ugly_number_heap(self, n, primes):
        uglies = [1]
        min_heap = Heap()
        for prime in primes:
            min_heap.push(prime, 0, prime)
        for i in range(1, n):
            # find min
            next_ugly = min_heap.peek()
            uglies.append(next_ugly)
            # update
            while min_heap.peek() == next_ugly:
                _, index, prime_base = min_heap.pop()
                min_heap.push(prime_base * uglies[index+1], index+1, prime_base)
        return uglies[-1]


class Heap(object):
    def __init__(self):
        self._data = []

    def push(self, val, index, base):
        heapq.heappush(self._data, (val, index, base))

    def pop(self):
        return heapq.heappop(self._data)

    def peek(self):
        return self._data[0][0]

test = Solution()
print test.nth_super_ugly_number_heap(12, [2, 7, 13, 19])