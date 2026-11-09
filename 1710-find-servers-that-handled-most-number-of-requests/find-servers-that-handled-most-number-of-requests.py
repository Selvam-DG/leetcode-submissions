import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        bit = [0] * (k + 1)

        def update(i, delta):
            i += 1
            while i <= k:
                bit[i] += delta
                i += i & -i

        def prefix_sum(i):
            total = 0
            while i > 0:
                total += bit[i]
                i -= i & -i
            return total

        def find_kth(rank):
            idx = 0
            step = 1 << (k.bit_length() - 1)

            while step:
                nxt = idx + step
                if nxt <= k and bit[nxt] < rank:
                    rank -= bit[nxt]
                    idx = nxt
                step >>= 1

            return idx

        # Initially all servers are available
        for i in range(k):
            update(i, 1)

        busy = []
        count = [0] * k
        available_count = k

        for i, time in enumerate(arrival):

            # Release all finished servers
            while busy and busy[0][0] <= time:
                finish, server = heapq.heappop(busy)
                update(server, 1)
                available_count += 1

            if available_count == 0:
                continue

            preferred = i % k

            # Count available servers before preferred
            before = prefix_sum(preferred)

            # Find first available server >= preferred
            if before < available_count:
                rank = before + 1
            else:
                rank = 1  # Wrap around

            server = find_kth(rank)

            # Mark server busy
            update(server, -1)
            available_count -= 1

            count[server] += 1

            heapq.heappush(
                busy,
                (time + load[i], server)
            )

        max_requests = max(count)

        return [
            i for i in range(k)
            if count[i] == max_requests
        ]