class Solution:
    def removeInvalidParentheses(self, s):
        def isValid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    # More ')' than '(' at any point
                    if balance < 0:
                        return False

            return balance == 0

        # BFS
        queue = {s}
        visited = {s}

        while queue:

            valid = []

            # Check current level
            for string in queue:
                if isValid(string):
                    valid.append(string)

            # If we found valid strings,
            # this is the minimum number of removals.
            if valid:
                return valid

            # Generate next level by removing one parenthesis
            next_queue = set()

            for string in queue:
                for i in range(len(string)):

                    # We only need to remove parentheses,
                    # never letters.
                    if string[i] not in "()":
                        continue

                    new_string = string[:i] + string[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        next_queue.add(new_string)

            queue = next_queue

        return [""]