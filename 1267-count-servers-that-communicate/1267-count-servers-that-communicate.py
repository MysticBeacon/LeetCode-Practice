
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        row = [0] * m
        col = [0] * n

        # First pass: Count servers in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1

        # Second pass: Count communicating servers
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row[i] > 1 or col[j] > 1:
                        ans += 1

        return ans
