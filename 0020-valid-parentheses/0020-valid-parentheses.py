class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                # No opening bracket to match
                if not stack:
                    return False

                # Check if brackets match
                if stack.pop() != pairs[ch]:
                    return False

        # Valid only if all opening brackets were closed
        return len(stack) == 0