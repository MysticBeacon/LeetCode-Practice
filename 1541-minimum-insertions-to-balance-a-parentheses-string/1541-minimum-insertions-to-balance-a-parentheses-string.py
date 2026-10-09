
class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_count = 0

        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                open_count += 1
                i += 1
            else:
                # Check whether the next character is also ')'
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    # Insert one ')' to make a pair
                    insertions += 1
                    i += 1

                if open_count > 0:
                    open_count -= 1
                else:
                    # Insert '(' to match this closing pair
                    insertions += 1

        # Each remaining '(' needs two ')'
        insertions += open_count * 2

        return insertions
