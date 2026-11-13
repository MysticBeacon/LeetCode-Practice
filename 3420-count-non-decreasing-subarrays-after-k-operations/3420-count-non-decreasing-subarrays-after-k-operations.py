
from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        stack = deque()
        right = n - 1
        cost = 0
        ans = 0

        for i in range(n - 1, -1, -1):

            # Update the cost using the monotonic stack
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()

                prev = stack[-1] if stack else right + 1

                cost += (nums[i] - nums[idx]) * (prev - idx)

            stack.append(i)

            # Shrink the window if cost exceeds k
            while cost > k:

                if stack and stack[0] == right:
                    stack.popleft()

                if stack:
                    cost -= max(0, nums[stack[0]] - nums[right])

                right -= 1

            # Count all valid subarrays starting at i
            ans += right - i + 1

        return ans
