class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        ans = 0

        for ch in s:
            if ch == '(':
                balance += 1
            else:  # ch == ')'
                if balance > 0:
                    balance -= 1
                else:
                    # Need to insert '(' before this ')'
                    ans += 1

        # Insert ')' for all unmatched '('
        ans += balance

        return ans