class Solution:
    def checkValidString(self, s: str) -> bool:
        # Minimum and maximum possible open brackets
        min_open = 0
        max_open = 0

        for ch in s:

            if ch == '(':
                min_open += 1
                max_open += 1

            elif ch == ')':
                min_open -= 1
                max_open -= 1

            else:  # '*'
                # '*' can be ')' or '(' or empty
                min_open -= 1
                max_open += 1

            # Too many ')' -> invalid
            if max_open < 0:
                return False

            # min_open cannot be negative
            min_open = max(0, min_open)

        # If minimum possible unmatched '(' is 0,
        # we can make the string valid
        return min_open == 0