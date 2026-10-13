class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums.sort(key=lambda x: x * x)

        n = len(nums)
        k = (n + 1) // 2

        return sum(x * x for x in nums[n - k:]) - sum(x * x for x in nums[:n - k])