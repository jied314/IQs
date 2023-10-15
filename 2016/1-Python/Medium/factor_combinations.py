# 1/13 - Locked LC
# Print all unique combination of factors (except 1) of a given number.
# For example:
#   Input: 12, Output: [[2, 2, 3], [2, 6], [3, 4]]
#   Input: 15, Output: [[3, 5]]
#   Input: 28, Output: [[2, 2, 7], [2, 14], [4, 7]]

class Solution(object):
    # Idea:
    #   start from the smallest factor (2), work all the way up.
    #   make sure factors increase! -> avoid duplicates
    #   e.g. T(12) = T(2) + T(6), T(3) + T(4)
    #                      [[2,3], [6]]  [[4]], [[2,2]] is invalid.
    def factor_comb(self, n):
        """
        :param n: int
        :return: List[List[int]]
        """
        ret = self.helper(n, 2)
        ret.pop()
        return ret

    def helper(self, n, start_factor):
        if n <= 0:
            return []
        ret = []
        i = start_factor
        while i * i <= n:
            temp = []
            if n % i == 0 and n / i != 0:
                temp.append(i)
                right = self.helper(n / i, i)
                for r in right:
                    ret.append(temp + r)
            i += 1
        ret.append([n])
        return ret


test = Solution()
print test.factor_comb(8)

