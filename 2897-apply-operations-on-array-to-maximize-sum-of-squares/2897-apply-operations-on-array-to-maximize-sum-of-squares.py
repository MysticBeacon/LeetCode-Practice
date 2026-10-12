
class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7

        # Count how many numbers contain each bit
        bit_count = [0] * 32

        for num in nums:
            for bit in range(32):
                if num & (1 << bit):
                    bit_count[bit] += 1

        ans = 0

        # Construct k numbers greedily
        for _ in range(k):
            num = 0

            for bit in range(32):
                if bit_count[bit] > 0:
                    num |= (1 << bit)
                    bit_count[bit] -= 1

            ans = (ans + num * num) % MOD

        return ans
