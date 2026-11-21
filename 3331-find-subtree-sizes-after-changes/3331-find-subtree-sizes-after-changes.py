
class Solution:
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        # Step 1: Build the original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Step 2: Find the new parent of every node
        new_parent = parent[:]

        # Stores the closest ancestor for each character
        last = [-1] * 26

        # Iterative DFS to avoid recursion depth issues
        stack = [(0, 1, -1)]

        while stack:
            node, entering, prev = stack.pop()
            char = ord(s[node]) - ord('a')

            if entering:
                prev = last[char]

                # Find the closest ancestor with the same character
                if node != 0 and prev != -1:
                    new_parent[node] = prev

                last[char] = node

                # Exit event
                stack.append((node, 0, prev))

                # Visit children
                for child in reversed(children[node]):
                    stack.append((child, 1, -1))

            else:
                # Restore previous ancestor when leaving this subtree
                last[char] = prev

        # Step 3: Build the modified tree
        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        # Step 4: Calculate subtree sizes
        order = []
        stack = [0]

        while stack:
            node = stack.pop()
            order.append(node)

            for child in new_children[node]:
                stack.append(child)

        # Initially, every node has subtree size 1
        answer = [1] * n

        # Process children before their parents
        for node in reversed(order):
            if node != 0:
                answer[new_parent[node]] += answer[node]

        return answer
