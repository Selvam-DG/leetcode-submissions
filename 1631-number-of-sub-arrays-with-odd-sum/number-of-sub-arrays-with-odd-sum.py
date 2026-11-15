class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        ans = 0
        n = len(arr)
        odd_count = 0
        even_count = 1
        prefix_sum = 0
        MOD = 10**9+7

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 0:
                ans += odd_count
                even_count += 1
            else:
                ans += even_count
                odd_count += 1
        
        return ans%MOD
      