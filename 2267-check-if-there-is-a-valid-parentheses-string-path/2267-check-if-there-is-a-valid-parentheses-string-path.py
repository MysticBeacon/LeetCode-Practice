class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # A valid parentheses string must have even length
        if (m + n) % 2 == 0:
            return False

        # Starting cell must be '('
        if grid[0][0] == ')':
            return False

        # dp[i][j] stores possible balances at cell (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]

        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                # Possible balances from top and left
                prev = set()

                if i > 0:
                    prev |= dp[i - 1][j]

                if j > 0:
                    prev |= dp[i][j - 1]

                for balance in prev:

                    if grid[i][j] == '(':
                        new_balance = balance + 1
                    else:
                        new_balance = balance - 1

                    # Balance must never become negative
                    if new_balance >= 0:
                        dp[i][j].add(new_balance)

        # A valid path must end with balance 0
        return 0 in dp[m - 1][n - 1]