class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        dp = [[] for _ in range(target+1)]
        dp[0] = [[]]
        if n == 0:
            return []

        for num in candidates:
            for curr_sum in range(num, target+1):
                for temp_arr in dp[curr_sum - num]:
                    dp[curr_sum].append(temp_arr + [num])

        return dp[target]
