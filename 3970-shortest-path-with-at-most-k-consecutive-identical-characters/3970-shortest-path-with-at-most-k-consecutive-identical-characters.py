
import heapq

class Solution:
    def shortestPath(self, n, edges, labels, k):

        # Build adjacency list
        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))

        INF = float('inf')

        # dist[node][count]
        dist = [[INF] * (k + 1) for _ in range(n)]

        # Initial state
        dist[0][1] = 0

        # Min heap: (cost, node, consecutive_count)
        pq = [(0, 0, 1)]

        while pq:

            cost, u, count = heapq.heappop(pq)

            # Ignore outdated states
            if cost != dist[u][count]:
                continue

            # Destination reached
            if u == n - 1:
                return cost

            # Explore adjacent nodes
            for v, w in adj[u]:

                if labels[u] == labels[v]:
                    new_count = count + 1
                else:
                    new_count = 1

                # Check consecutive character constraint
                if new_count > k:
                    continue

                new_cost = cost + w

                # Relaxation
                if new_cost < dist[v][new_count]:

                    dist[v][new_count] = new_cost

                    heapq.heappush(
                        pq,
                        (new_cost, v, new_count)
                    )

        return -1
