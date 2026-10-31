
class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7

        m = len(grid)
        n = len(grid[0])

        # Number of ways to enter a cell from the left
        right = [[0] * n for _ in range(m)]

        # Number of ways to enter a cell from above
        down = [[0] * n for _ in range(m)]

        # Starting position
        right[0][0] = 1

        # Process the grid row by row
        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:

                    # Mirror: entered while moving right
                    # Robot gets reflected downward
                    if i + 1 < m:
                        down[i + 1][j] = (
                            down[i + 1][j] + right[i][j]
                        ) % MOD

                    # Mirror: entered while moving down
                    # Robot gets reflected to the right
                    if j + 1 < n:
                        right[i][j + 1] = (
                            right[i][j + 1] + down[i][j]
                        ) % MOD

                else:

                    # Empty cell: robot can move right or down
                    ways = (right[i][j] + down[i][j]) % MOD

                    # Move right
                    if j + 1 < n:
                        right[i][j + 1] = (
                            right[i][j + 1] + ways
                        ) % MOD

                    # Move down
                    if i + 1 < m:
                        down[i + 1][j] = (
                            down[i + 1][j] + ways
                        ) % MOD

        # Total number of ways to reach destination
        return (right[m - 1][n - 1] +
                down[m - 1][n - 1]) % MOD
