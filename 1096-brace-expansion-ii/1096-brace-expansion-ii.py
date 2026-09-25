class Solution:
    def braceExpansionII(self, expression):
        def parse():
            nonlocal i

            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == ',':
                    # Add current expression to result
                    result |= current
                    current = {""}
                    i += 1

                elif expression[i] == '{':
                    i += 1  # Skip '{'

                    group = parse()

                    # Concatenate current with everything in group
                    current = {
                        a + b
                        for a in current
                        for b in group
                    }

                    i += 1  # Skip '}'

                else:
                    # Lowercase letter
                    current = {
                        word + expression[i]
                        for word in current
                    }
                    i += 1

            result |= current
            return result

        i = 0
        return sorted(parse())