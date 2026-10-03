class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0

        for i, ch in enumerate(s):

            if ch == '(':
                stack.append(i)

            else:
                stack.pop()

                if not stack:
                    # Current ')' cannot be matched
                    stack.append(i)
                else:
                    # Valid substring length
                    max_length = max(max_length, i - stack[-1])

        return max_length