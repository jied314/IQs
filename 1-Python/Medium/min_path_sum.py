# 7/6 - Array, DP
class MinimumPathSum:
    # @param {integer[][]} grid
    # @return {integer}

    # Test on LeetCode - 92ms
    def min_path_sum(self, grid):
        if grid:
            visited = [[0 for j in range(0, len(grid[0]))] for i in range(0, len(grid))]
            m = len(grid)
            n = len(grid[0])
            self.compute_sum(0, 0, m, n, grid, visited)
            return visited[0][0]
        else:
            return 0

    def compute_sum(self, x, y, m, n, grid, visited):
        if x == m-1 and y == n-1:
            visited[x][y] = grid[x][y]
        elif x == m-1:
            if not visited[x][y]:
                visited[x][y] = grid[x][y] + self.compute_sum(x, y+1, m, n, grid, visited)
        elif y == n-1:
            if not visited[x][y]:
                visited[x][y] = grid[x][y] + self.compute_sum(x+1, y, m, n, grid, visited)
        else:
            if visited[x][y + 1]:
                right = visited[x][y + 1]
            else:
                right = self.compute_sum(x, y+1, m, n, grid, visited)
            if visited[x+1][y]:
                down = visited[x+1][y]
            else:
                down = self.compute_sum(x+1, y, m, n, grid, visited)
            visited[x][y] = grid[x][y] + min(right, down)
        return visited[x][y]

    # Test On LeetCode - 60ms
    def min_path_sum_in_place(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]

def main():
    test = MinimumPathSum()
    print test.min_path_sum([[1, 1, 2], [0, 3, 1]])
    print test.min_path_sum_in_place([[1, 1, 2], [0, 3, 1]])


if __name__ == '__main__':
    main()

