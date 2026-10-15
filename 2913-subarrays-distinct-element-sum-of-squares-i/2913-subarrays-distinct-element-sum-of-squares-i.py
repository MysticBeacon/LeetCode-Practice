
class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0

        for i in range(n):
            distinct = set()

            for j in range(i, n):
                distinct.add(nums[j])
                count = len(distinct)
                total += count * count

        return total
