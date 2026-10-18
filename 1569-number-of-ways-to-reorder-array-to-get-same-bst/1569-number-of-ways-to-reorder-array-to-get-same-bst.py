
from typing import List
from math import comb
import sys

sys.setrecursionlimit(5000)

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def solve(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            left_ways = solve(left)
            right_ways = solve(right)

            # Interleave left and right subtree elements
            # while preserving their internal orders.
            interleavings = comb(len(left) + len(right), len(left))

            return (
                interleavings * left_ways * right_ways
            ) % MOD

        # Subtract the original ordering.
        return (solve(nums) - 1) % MOD
