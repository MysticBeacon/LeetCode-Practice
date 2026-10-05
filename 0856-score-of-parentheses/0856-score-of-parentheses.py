class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == '(':
                # Start a new nested level
                stack.append(0)
            else:
                # Score of the current level
                inner = stack.pop()

                if inner == 0:
                    # "()"
                    score = 1
                else:
                    # "(A)"
                    score = 2 * inner

                # Add this score to the previous level
                stack[-1] += score

        return stack[0]