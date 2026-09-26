class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:

        # Create a dictionary from knowledge
        mp = {}

        for key, value in knowledge:
            mp[key] = value

        result = []
        i = 0

        while i < len(s):

            if s[i] == '(':

                # Find the closing bracket
                j = i + 1

                while s[j] != ')':
                    j += 1

                # Extract the key
                key = s[i + 1:j]

                # Replace with value or '?'
                result.append(mp.get(key, '?'))

                # Move past the closing bracket
                i = j + 1

            else:
                # Normal character
                result.append(s[i])
                i += 1

        return ''.join(result)