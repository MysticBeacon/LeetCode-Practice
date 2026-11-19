
class Solution:
    def minimizeSum(self, nums):
        nums.sort()

        n = len(nums)

        ans = min(
            nums[n - 1] - nums[2],
            nums[n - 2] - nums[1],
            nums[n - 3] - nums[0]
        )

        return ans
