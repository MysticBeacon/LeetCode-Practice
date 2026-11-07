
import heapq

class Solution:
    def assignTasks(self, servers, tasks):

        n = len(servers)

        # Available servers: (weight, index)
        available = [(servers[i], i) for i in range(n)]
        heapq.heapify(available)

        # Busy servers: (finish_time, weight, index)
        busy = []

        ans = []
        time = 0

        for i in range(len(tasks)):

            # Current time cannot be earlier than task arrival
            time = max(time, i)

            # Release all servers that have finished
            while busy and busy[0][0] <= time:
                finish, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            # If no server is available, wait
            if not available:

                # Move time to the earliest finishing time
                time = busy[0][0]

                # Release all servers finishing at this time
                while busy and busy[0][0] <= time:
                    finish, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            # Select the server with minimum weight and index
            weight, index = heapq.heappop(available)

            ans.append(index)

            # Assign the task and calculate finishing time
            finish_time = time + tasks[i]

            heapq.heappush(
                busy,
                (finish_time, weight, index)
            )

        return ans
