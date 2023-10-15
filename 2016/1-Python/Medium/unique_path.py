# 7/4 - Array, Dynamic Programming
# For a m*n grid, how many possible unique paths are there?
# Pascal's Triangle
class UniquePaths:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}

    # Test on LeetCode - 60ms
    def unique_paths(self, m, n):
        if m > 1 and n > 1:
            return self.pascal_triangle_nice(m+n-1, m)[m-1]
        else:
            return 1

    def pascal_triangle(self, level):
        nums = [1]
        if level > 1:
            for i in range(2, level+1):
                temp = [1]
                for j in range(1, len(nums)):
                    temp.append(nums[j-1] + nums[j])
                temp.append(1)
                nums = temp
        #print nums
        return nums

    # only compute upto the position
    def pascal_triangle_nice(self, level, position):
        nums = [1]
        if level > 1:
            for i in range(2, level+1):
                temp = [1]
                end = position
                if end >= i:
                    end = len(nums)
                for j in range(1, end):
                    temp.append(nums[j-1] + nums[j])
                if end < position:
                    temp.append(1)
                nums = temp
        #print nums
        return nums

    # Use DP
    # Note: How to calculate Pascal Triangle (vertical)
    def unique_paths_dp(self, m, n):
        if m > 1 and n > 1:
            nums = [1 for i in range(0, n)]
            for i in range(1, m):
                for j in range(1, n):
                    nums[j] += nums[j - 1]
            return nums[n-1]
        else:
            return 1

    # 12/22 - Revisit
    # Use DP
    # Only use O(N) memory
    def unique_paths_revisit(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        matrix = [1] * n
        for j in range(1, m):
            for i in range(1, n):
                matrix[i] += matrix[i-1]
        return matrix[n-1]

def main():
    test = UniquePaths()
    print test.unique_paths(3, 4)
    print test.unique_paths_dp(3, 4)


if __name__ == '__main__':
    main()