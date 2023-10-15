# 7/18 - BackTracking
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
# Idea:
#      DP - C(n,k) = C(n-1, k-1) + C(n-1,k)
#
# 12/24 - Revisit
# Use dictionary to record computed result

import copy

class Combinations:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}

    # Test on LeetCode 88ms
    def combine(self, n, k):
        return self.get_combinations(n, k, {})

    def get_combinations(self, n, k, combinations):
        if n in combinations and k in combinations[n]:
            return combinations[n][k]
        if n == k:
            result = [[i for i in range(1, n+1)]]
        elif k == 1:
            result = [[i] for i in range(1, n+1)]
        else:
            result = self.get_combinations(n-1, k, combinations)
            result1 = copy.deepcopy(self.get_combinations(n-1, k-1, combinations))
            for e in result1:
                e.append(n)
            result.extend(result1)
        if n not in combinations:
            combinations[n] = {}
        combinations[n][k] = result
        return combinations[n][k]

    # 12/24 - revisit
    # Test on LeetCode - 68ms
    # Same idea as above
    def combine_revisit_n_k(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0 or n == 0 or k > n:
            return []
        return self.helper_n_k(n, k)

    def helper_n_k(self, n, k):
        ret = []
        if k == 1:
            for i in range(1, n+1):
                ret.append([i])
        elif n == k:
            ret.append([i for i in range(1, n+1)])
        else:
            ret.extend(self.helper_n_k(n-1, k))
            rest = self.helper_n_k(n-1, k-1)
            for e in rest:
                e.append(n)
            ret.extend(rest)
        return ret

    # 12/24 - revisit
    # Test on LeetCode - 76ms
    # Idea:
    #   straight-forward.
    #   T(N, K) = 1 + T(2..N, K-1)
    #             2 + T(3..N, K-1)
    #             ...
    def combine_revisit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0 or n == 0 or k > n:
            return []
        return self.helper(n, k, 1)

    def helper(self, n, k, start):
        ret = []
        if k == 1:
            for i in range(start, n+1):
                ret.append([i])
        else:
            for i in range(start, n):
                rest = self.helper(n, k-1, i+1)
                for e in rest:
                    e.insert(0, i)
                ret.extend(rest)
        return ret

    # Note:
    #   edge case: k == 1
    def combine_iterative(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0 or n == 0 or k > n:
            return []
        if k == 1:
            return [[i] for i in range(1, n+1)]
        ret = [[i] for i in range(1, n)]
        while k > 1:
            ret_length = len(ret)
            for i in range(0, ret_length):
                e = ret.pop(0)
                for j in range(e[-1]+1, n+1):
                    ret.append(e + [j])
            k -= 1
        return ret


def main():
    test = Combinations()
    print test.combine(4, 3)


if __name__ == '__main__':
    main()