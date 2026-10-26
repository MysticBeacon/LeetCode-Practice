
class Solution:
    def countIslands(self, grid, k):
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            stack = [(r, c)]
            grid[r][c] = 0
            total = 0

            while stack:
                x, y = stack.pop()
                total += original[x][y]

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy

                    if (0 <= nx < m and 0 <= ny < n
                            and grid[nx][ny] > 0):
                        grid[nx][ny] = 0
                        stack.append((nx, ny))

            return total

        original = [row[:] for row in grid]

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    total = dfs(i, j)

                    if total % k == 0:
                        count += 1

        return count
