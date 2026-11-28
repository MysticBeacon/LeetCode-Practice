
from typing import List
from bisect import bisect_left

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        n = len(items)

        # Step 1: Count frequency of each factor
        freq = [0] * (n + 1)

        for factor, price in items:
            freq[factor] += 1

        # Step 2: Precompute divisible item counts
        divisible = [0] * (n + 1)

        for factor in range(1, n + 1):
            for multiple in range(factor, n + 1, factor):
                divisible[factor] += freq[multiple]

        # Step 3: Build double-copy opportunities
        data = []

        for factor, price in items:
            count = divisible[factor] - 1
            data.append((price, count))

        # Step 4: Sort by price
        data.sort()

        prices = [p for p, d in data]

        pref_count = [0] * (n + 1)
        pref_sum = [0] * (n + 1)

        for i in range(n):
            p, d = data[i]

            pref_count[i + 1] = pref_count[i] + d
            pref_sum[i + 1] = pref_sum[i] + p * d

        min_price = prices[0]

        # Calculate the cost of the cheapest cnt opportunities
        def get_sum(cnt):

            if cnt == 0:
                return 0

            idx = bisect_left(pref_count, cnt, 1)

            return (
                pref_sum[idx - 1]
                + (cnt - pref_count[idx - 1]) * prices[idx - 1]
            )

        # Minimum cost to obtain at least k copies
        def min_cost(k):

            if k == 0:
                return 0

            q = k // 2

            limit = bisect_left(prices, 2 * min_price)

            available = pref_count[limit]

            take = min(q, available)

            cost = (k - 2 * take) * min_price + get_sum(take)

            # For odd k, consider obtaining k + 1 copies
            if k % 2 == 1 and pref_count[n] >= q + 1:

                idx = bisect_left(pref_count, q + 1, 1)

                extra_price = prices[idx - 1]

                if extra_price <= min_price:
                    cost = min(cost, get_sum(q + 1))

            return cost

        # Step 5: Binary search
        low = 0
        high = 2 * (budget // min_price)

        ans = 0

        while low <= high:

            mid = (low + high) // 2

            if min_cost(mid) <= budget:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
