class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        pal = [[False]*n for _ in range(n)]

        for l in range(n-1, -1, -1):
            for r in range(l, n):
                if s[l] == s[r]:
                    if r-l <= 1:
                        pal[l][r] = True
                    else:
                        pal[l][r] = pal[l+1][r-1]
        
        dp = [0] * (n+1)

        for end in range(n):
            dp[end+1] = dp[end]

            for start in range(end-k+1, -1, -1):
                if pal[start][end]:
                    dp[end+1] = max(dp[end+1], 1+dp[start])

        
        return dp[n]