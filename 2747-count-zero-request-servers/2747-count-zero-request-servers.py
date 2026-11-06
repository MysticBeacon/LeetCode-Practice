
class Solution:
    def countServers(self, n, logs, x, queries):

        # Sort logs by request time
        logs.sort(key=lambda a: a[1])

        # Store queries with their original indices
        sorted_queries = sorted(
            (q, i) for i, q in enumerate(queries)
        )

        ans = [0] * len(queries)

        # Count requests received by each server
        count = [0] * (n + 1)

        # Number of distinct servers in current window
        active = 0

        left = 0
        right = 0
        m = len(logs)

        for q, idx in sorted_queries:

            start = q - x

            # Add logs whose time <= q
            while right < m and logs[right][1] <= q:

                server = logs[right][0]

                if count[server] == 0:
                    active += 1

                count[server] += 1
                right += 1

            # Remove logs whose time < q - x
            while left < right and logs[left][1] < start:

                server = logs[left][0]

                count[server] -= 1

                if count[server] == 0:
                    active -= 1

                left += 1

            # Servers without requests
            ans[idx] = n - active

        return ans
