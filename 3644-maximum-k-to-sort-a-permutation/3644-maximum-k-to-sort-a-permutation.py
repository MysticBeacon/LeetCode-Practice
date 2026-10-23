
class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        k = None

        for i in range(len(nums)):
            if nums[i] != i:
                if k is None:
                    k = nums[i]
                else:
                    k &= nums[i]

        return k if k is not None else 0
