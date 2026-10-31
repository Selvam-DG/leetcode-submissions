class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7

        dp = [[[0] * 2 for _ in range(n)] for _ in range(m)]

        # Destination reached
        dp[m-1][n-1][0] = 1
        dp[m-1][n-1][1] = 1

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):

                if r == m-1 and c == n-1:
                    continue

                right = dp[r][c+1][0] if c+1 < n else 0
                down = dp[r+1][c][1] if r+1 < m else 0

                if grid[r][c] == 0:
                    dp[r][c][0] = (right + down) % MOD
                    dp[r][c][1] = (right + down) % MOD

                else:
                    # Arrived moving right -> reflect down
                    dp[r][c][0] = down

                    # Arrived moving down -> reflect right
                    dp[r][c][1] = right

        # Start cell: we can initially choose right or down
        if m == 1 and n == 1:
            return 1

        right = dp[0][1][0] if n > 1 else 0
        down = dp[1][0][1] if m > 1 else 0

        return (right + down) % MOD 