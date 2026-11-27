
class Solution:
    def maximumSaleItems(self, items, budget):

        n = len(items)

        # Step 1: Count frequency of each factor
        freq = [0] * 1501

        for factor, price in items:
            freq[factor] += 1

        # Step 2: Calculate benefit of each item
        # Benefit = 1 purchased copy + free copies
        benefits = []

        for factor, price in items:

            free = 0

            for multiple in range(factor, 1501, factor):
                free += freq[multiple]

            free -= 1  # Exclude the item itself

            benefits.append((price, free + 1))

        # Step 3: Group items by price
        groups = [[] for _ in range(1501)]

        for price, value in benefits:
            groups[price].append(value)

        # Step 4: Initialize DP
        NEG = -10**9

        dp = [NEG] * (budget + 1)
        dp[0] = 0

        ans = 0

        # Step 5: Process prices in descending order
        for p in range(1500, 0, -1):

            if not groups[p]:
                continue

            # Must select at least one item of price p
            exact = [NEG] * (budget + 1)

            for value in groups[p]:

                for c in range(budget, p - 1, -1):

                    if dp[c - p] != NEG:

                        candidate = dp[c - p] + value

                        exact[c] = max(exact[c], candidate)
                        dp[c] = max(dp[c], candidate)

            # Step 6: Use remaining budget for extra copies
            for c in range(budget + 1):

                if exact[c] != NEG:

                    extra = (budget - c) // p

                    ans = max(ans, exact[c] + extra)

        return ans
