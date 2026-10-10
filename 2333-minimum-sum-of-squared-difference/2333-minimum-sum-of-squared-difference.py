
class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        # If all differences can be eliminated
        if sum(diffs) <= k:
            return 0

        # Find the maximum difference threshold
        low, high = 0, max(diffs)

        while low < high:
            mid = (low + high) // 2

            # Operations needed to reduce all differences to mid
            needed = sum(max(d - mid, 0) for d in diffs)

            if needed <= k:
                high = mid
            else:
                low = mid + 1

        x = low

        # Reduce all differences greater than x down to x
        used = sum(max(d - x, 0) for d in diffs)
        remaining = k - used

        # Calculate squared differences after leveling
        result = sum(min(d, x) ** 2 for d in diffs)

        # Use remaining operations to reduce x to x - 1
        result -= remaining * (2 * x - 1)

        return result
