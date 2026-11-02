
class Solution:
    def minMoves2(self, nums: list[int]) -> int:

        # Step 1: Sort the array
        nums.sort()

        # Step 2: Find the median
        n = len(nums)
        median = nums[n // 2]

        # Step 3: Calculate total moves
        moves = 0

        for num in nums:
            moves += abs(num - median)

        return moves
