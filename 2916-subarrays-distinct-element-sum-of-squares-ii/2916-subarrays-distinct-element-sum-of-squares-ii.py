class Solution:

  def sumCounts(self, nums: list[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)

    tree_sum_sq = [0] * (4 * n)
    tree_sum_cnt = [0] * (4 * n)
    lazy = [0] * (4 * n)

    def push(node, l, r):
      if lazy[node] != 0:
        val = lazy[node]
        mid = (l + r) // 2
        lc, rc = 2 * node, 2 * node + 1

        # Left child update
        len_left = mid - l + 1
        tree_sum_sq[lc] = (
            tree_sum_sq[lc]
            + 2 * val * tree_sum_cnt[lc]
            + val * val * len_left
        ) % MOD
        tree_sum_cnt[lc] = (tree_sum_cnt[lc] + val * len_left) % MOD
        lazy[lc] = (lazy[lc] + val) % MOD

        # Right child update
        len_right = r - mid
        tree_sum_sq[rc] = (
            tree_sum_sq[rc]
            + 2 * val * tree_sum_cnt[rc]
            + val * val * len_right
        ) % MOD
        tree_sum_cnt[rc] = (tree_sum_cnt[rc] + val * len_right) % MOD
        lazy[rc] = (lazy[rc] + val) % MOD

        lazy[node] = 0

    def update(node, l, r, ql, qr, val):
      if ql <= l and r <= qr:
        length = r - l + 1
        tree_sum_sq[node] = (
            tree_sum_sq[node]
            + 2 * val * tree_sum_cnt[node]
            + val * val * length
        ) % MOD
        tree_sum_cnt[node] = (tree_sum_cnt[node] + val * length) % MOD
        lazy[node] = (lazy[node] + val) % MOD
        return

      push(node, l, r)
      mid = (l + r) // 2
      if ql <= mid:
        update(2 * node, l, mid, ql, qr, val)
      if qr > mid:
        update(2 * node + 1, mid + 1, r, ql, qr, val)

      tree_sum_sq[node] = (tree_sum_sq[2 * node] + tree_sum_sq[2 * node + 1]) % MOD
      tree_sum_cnt[node] = (
          tree_sum_cnt[2 * node] + tree_sum_cnt[2 * node + 1]
      ) % MOD

    last_seen = {}
    total_ans = 0

    for r_idx in range(n):
      val = nums[r_idx]
      l_idx = last_seen.get(val, -1) + 1
      last_seen[val] = r_idx

      # Update range [l_idx, r_idx] by adding 1 to the distinct counts
      update(1, 0, n - 1, l_idx, r_idx, 1)

      # Add the sum of squares of all subarrays ending at r_idx
      total_ans = (total_ans + tree_sum_sq[1]) % MOD

    return total_ans