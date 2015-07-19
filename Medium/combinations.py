# 7/18 - BackTracking
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
# Idea:
#      DP - C(n,k) = C(n-1, k-1) + C(n-1,k)

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


def main():
    test = Combinations()
    print test.combine(4, 3)


if __name__ == '__main__':
    main()