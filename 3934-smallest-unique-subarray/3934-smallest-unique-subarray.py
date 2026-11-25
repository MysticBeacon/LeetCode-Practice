
class Solution:
    def smallestUniqueSubarray(self, nums):
        n = len(nums)

        # Build suffix array
        sa = list(range(n))
        rank = nums[:]
        k = 1

        while True:
            sa.sort(
                key=lambda i: (
                    rank[i],
                    rank[i + k] if i + k < n else -1
                )
            )

            new_rank = [0] * n

            for i in range(1, n):
                prev = sa[i - 1]
                curr = sa[i]

                prev_key = (
                    rank[prev],
                    rank[prev + k] if prev + k < n else -1
                )

                curr_key = (
                    rank[curr],
                    rank[curr + k] if curr + k < n else -1
                )

                new_rank[curr] = new_rank[prev] + (
                    prev_key != curr_key
                )

            rank = new_rank

            if rank[sa[-1]] == n - 1:
                break

            k *= 2

        # Build inverse suffix array
        pos = [0] * n

        for i in range(n):
            pos[sa[i]] = i

        # Build LCP array using Kasai's algorithm
        lcp = [0] * n
        h = 0

        for i in range(n):
            p = pos[i]

            if p == 0:
                continue

            j = sa[p - 1]

            while (i + h < n and j + h < n
                   and nums[i + h] == nums[j + h]):
                h += 1

            lcp[p] = h

            if h > 0:
                h -= 1

        # Find minimum unique subarray length
        ans = n

        for p in range(n):
            shared = lcp[p]

            if p + 1 < n:
                shared = max(shared, lcp[p + 1])

            start = sa[p]
            length = shared + 1

            if length <= n - start:
                ans = min(ans, length)

        return ans
