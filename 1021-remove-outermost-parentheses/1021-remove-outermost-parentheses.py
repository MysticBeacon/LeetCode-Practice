class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        balance = 0

        for ch in s:
            if ch == '(':
                # If balance is already 0, this is
                # the outermost '(' of a primitive
                if balance > 0:
                    result.append(ch)

                balance += 1

            else:
                balance -= 1

                # If balance is still > 0, this is
                # not the outermost ')'
                if balance > 0:
                    result.append(ch)

        return ''.join(result)