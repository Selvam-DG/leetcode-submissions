
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute binomial coefficients using Pascal's triangle
        comb = [[1] * (n + 1) for _ in range(n + 1)]

        for i in range(2, n + 1):
            for j in range(1, i):
                comb[i][j] = (
                    comb[i - 1][j - 1] + comb[i - 1][j]
                ) % MOD

        def dfs(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]

            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]

            l, r = len(left), len(right)

            return (
                comb[l + r][l]
                * dfs(left)
                * dfs(right)
            ) % MOD

        return (dfs(nums) - 1) % MOD
