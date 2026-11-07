import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = []
        busy = []

        # Store servers by (weight, index)
        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))

        ans = []
        time = 0

        for i, duration in enumerate(tasks):
            time = max(time, i)

            # Free all servers that have completed their tasks
            while busy and busy[0][0] <= time:
                finish, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            # If no server is available, jump to earliest finish
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    finish, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))

            # Assign task to minimum-weight available server
            weight, idx = heapq.heappop(available)
            ans.append(idx)

            # Mark server as busy
            heapq.heappush(busy, (time + duration, weight, idx))

        return ans