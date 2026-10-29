class Solution:
    def palindromePath(self, n, edges, s, queries):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n

        # Build parent and depth arrays iteratively
        order = [0]
        for u in order:
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    order.append(v)

        # Find subtree sizes and heavy children
        for u in reversed(order):
            largest = 0
            for v in adj[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if size[v] > largest:
                        largest = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        timer = 0
        stack = [(0, 0)]

        # Assign HLD chain heads and positions
        while stack:
            u, h = stack.pop()
            while u != -1:
                head[u] = h
                pos[u] = timer
                timer += 1

                for v in adj[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        # Segment tree storing XOR of character masks
        seg = [0] * (2 * n)
        for u in range(n):
            seg[n + pos[u]] = 1 << (ord(s[u]) - ord('a'))

        for i in range(n - 1, 0, -1):
            seg[i] = seg[2 * i] ^ seg[2 * i + 1]

        def point_update(p, value):
            p += n
            seg[p] = value
            p //= 2
            while p:
                seg[p] = seg[2 * p] ^ seg[2 * p + 1]
                p //= 2

        def range_query(l, r):
            result = 0
            l += n
            r += n
            while l < r:
                if l & 1:
                    result ^= seg[l]
                    l += 1
                if r & 1:
                    r -= 1
                    result ^= seg[r]
                l //= 2
                r //= 2
            return result

        def path_query(u, v):
            result = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_query(pos[head[u]], pos[u] + 1)
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_query(pos[u], pos[v] + 1)
            return result

        chars = list(s)
        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                chars[u] = c
                point_update(pos[u], 1 << (ord(c) - ord('a')))

            else:
                u = int(parts[1])
                v = int(parts[2])

                mask = path_query(u, v)
                answer.append((mask & (mask - 1)) == 0)

        return answer