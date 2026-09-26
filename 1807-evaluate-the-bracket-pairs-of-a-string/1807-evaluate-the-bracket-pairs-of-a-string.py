class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:

        # Store key-value pairs in a dictionary
        mp = dict(knowledge)

        result = []
        i = 0

        while i < len(s):

            if s[i] == '(':
                j = i + 1

                # Find the closing bracket
                while s[j] != ')':
                    j += 1

                # Extract the key
                key = s[i + 1:j]

                # Replace with value or '?'
                result.append(mp.get(key, '?'))

                # Move past the closing bracket
                i = j + 1

            else:
                result.append(s[i])
                i += 1

        return ''.join(result)