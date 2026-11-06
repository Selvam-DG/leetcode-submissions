from collections import defaultdict

class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])

        sorted_queries = sorted(enumerate(queries), key=lambda a: a[1])

        freq = defaultdict(int)
        ans = [0] * len(queries)

        left = 0
        right = 0

        for idx, q in sorted_queries:

            # Add requests with time <= q
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                freq[server] += 1
                right += 1

            # Remove requests with time < q - x
            while left < right and logs[left][1] < q - x:
                server = logs[left][0]
                freq[server] -= 1

                if freq[server] == 0:
                    del freq[server]

                left += 1

            ans[idx] = n - len(freq)

        return ans