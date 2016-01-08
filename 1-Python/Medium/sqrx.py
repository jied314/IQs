# 10/19 - Math, BS
# Implement int sqrt(int x).
# Compute and return the square root of x.


class Solution(object):
    sqrt_dict = {}
    squares = []

    # Test on LeetCode - 84ms
    # Idea:
    #   start from the minimum unvisited sqrt to test whether sqrt * sqrt >= x
    #   keep track of the intermediate results in a dictionary for cache
    #   use binary search for retrieving covered square range
    def my_sqrt_dp(self, x):
        """
            :type x: int
            :rtype: int
            """
        if x < 0:
            return None

        if len(Solution.squares) > 0:  # not empty
            if x > Solution.squares[-1]:  # not covered
                min_sqrt = Solution.sqrt_dict[Solution.squares[-1]] + 1
            else:  # covered
                if x in Solution.sqrt_dict:  # x is a perfect square
                    return Solution.sqrt_dict[x]
                else:
                    index = self.search(x, Solution.squares)
                    return Solution.sqrt_dict[Solution.squares[index - 1]]
        else:
            min_sqrt = 0

        # start adding square and sqrt to the dictionary
        sqrt = min_sqrt
        while True:
            square = sqrt * sqrt
            if square <= x:
                Solution.sqrt_dict[square] = sqrt
                Solution.squares.append(square)
                sqrt += 1
            else:
                break
        return Solution.sqrt_dict[Solution.squares[-1]]

    # search for the right position for key
    # @param key: search target
    # @param array: sorted array of ascending order
    # @ret the right index for key in array
    def search(self, key, array):
        return self.bs(key, array, 0, len(array)-1)

    # binary search the right position of key in array
    # note that key must not exist in array
    def bs(self, key, array, low, high):
        while low <= high:
            mid = low + (high - low) / 2
            if array[mid] > key:
                high = mid - 1
            else:
                low = mid + 1
        return low

    # Test on LeetCode - 68ms
    # Idea:
    #   sqrt must be within [1...x]. use binary search on this.
    def my_sqrt_bs(self, x):
        if x == 0:
            return 0
        low, high, ans = 1, x, -1
        while low <= high:
            mid = low + (high - low) / 2
            if mid * mid <= x:
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
        return ans

    def my_sqrt_bs_revisit(self, x):
        if x == 0:
            return 0
        low, high, ans = 1, x, -1
        while low <= high:
            mid = low + (high - low) / 2
            if mid * mid <= x < (mid+1) * (mid+1):
                return mid
            if mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1
        return ans


    def my_sqrt_bit(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        bit = 1 << 15  # max int sqrt
        while bit > 0:
            ans |= bit
            if ans * ans > x:
                ans ^= bit
            bit >>= 1
        return ans

def main():
    test = Solution()
    print test.my_sqrt_dp(1)
    print test.my_sqrt_bs(1)
    print test.my_sqrt_bit(7)


if __name__ == "__main__":
    main()
