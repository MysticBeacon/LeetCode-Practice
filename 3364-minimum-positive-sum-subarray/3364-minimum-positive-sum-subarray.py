
class Solution:
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)

        # Build prefix sum array
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        ans = float('inf')

        # Check all possible subarrays
        for i in range(n):
            for length in range(l, r + 1):

                j = i + length

                if j > n:
                    break

                # Calculate subarray sum
                curr_sum = prefix[j] - prefix[i]

                # Find minimum positive sum
                if curr_sum > 0:
                    ans = min(ans, curr_sum)

        return ans if ans != float('inf') else -1
