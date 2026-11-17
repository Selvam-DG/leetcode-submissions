class Solution:
    def minimumChanges(self, s: str, k: int) -> int:

        n = len(s)
        INF = float('inf')

        # Precompute valid divisors for every length
        divisors = [[] for _ in range(n + 1)]

        for length in range(2, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)

        # cost[i][j] = minimum changes for s[i:j+1]
        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1

                for d in divisors[length]:
                    changes = 0

                    # Check all d groups
                    for start in range(d):
                        left = i + start
                        right = i + start + (length // d - 1) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    cost[i][j] = min(cost[i][j], changes)

        # dp[p][i] = minimum cost to partition
        # first i characters into p substrings
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):

                # Last substring starts at j
                for j in range(2 * (p - 1), i - 1):
                    dp[p][i] = min(
                        dp[p][i],
                        dp[p - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]