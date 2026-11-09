
import heapq

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

        # Initially, all servers are available
        for i in range(1, n + 1):
            self.update(i, 1)

    def update(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

    # Find the index of the kth available server
    def find_kth(self, k):
        idx = 0
        bit = 1 << (self.n.bit_length() - 1)

        while bit:
            nxt = idx + bit
            if nxt <= self.n and self.tree[nxt] < k:
                idx = nxt
                k -= self.tree[nxt]
            bit >>= 1

        return idx


class Solution:
    def busiestServers(self, k, arrival, load):

        available = FenwickTree(k)

        # (finish_time, server_id)
        busy = []

        count = [0] * k

        for i in range(len(arrival)):

            # Release servers whose requests are completed
            while busy and busy[0][0] <= arrival[i]:
                finish, server = heapq.heappop(busy)
                available.update(server + 1, 1)

            # Preferred server
            start = i % k

            # Number of available servers before start
            before = available.query(start)

            # Total available servers
            total = available.query(k)

            if total == 0:
                continue

            # Find next available server, with wraparound
            if before < total:
                server = available.find_kth(before + 1)
            else:
                server = available.find_kth(1)

            # Mark server as busy
            available.update(server + 1, -1)

            # Update handled request count
            count[server] += 1

            # Add server to busy heap
            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        # Find maximum number of handled requests
        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]
