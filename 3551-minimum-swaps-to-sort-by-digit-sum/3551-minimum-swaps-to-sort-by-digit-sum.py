class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        n = len(nums)

        # Sort by digit sum, then by number
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        # Map each number to its correct index
        index_map = {num: i for i, num in enumerate(sorted_nums)}

        visited = [False] * n
        swaps = 0

        # Count cycles in the permutation
        for i in range(n):
            if visited[i] or index_map[nums[i]] == i:
                continue

            cycle_length = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = index_map[nums[j]]
                cycle_length += 1

            swaps += cycle_length - 1

        return swaps