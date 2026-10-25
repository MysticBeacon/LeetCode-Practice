
class Solution:
    def closedIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            # If outside the grid, the island is not closed
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # Water or already visited land
            if grid[r][c] == 1:
                return True

            # Mark this land cell as visited
            grid[r][c] = 1

            # Explore all four directions
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)

            return up and down and left and right

        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    if dfs(r, c):
                        count += 1

        return count
