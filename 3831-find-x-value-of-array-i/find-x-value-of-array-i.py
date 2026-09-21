class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            x = num % k
            new_dp[x] += 1

            for remainder in range(k):
                new_remainder = (remainder * x) % k

                new_dp[new_remainder] += dp[remainder]

            
            for remainder in range(k):
                ans[remainder] += new_dp[remainder]
            
            dp = new_dp
        
        return ans