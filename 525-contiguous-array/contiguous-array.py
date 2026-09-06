class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        balance_freq = {0:-1}
        balance = 0
        ans =0 
        for i in range(n):
            if nums[i] == 0:
                balance -= 1
            elif nums[i] == 1:
                balance += 1
            
            if balance in balance_freq:
                ans = max(ans, i-balance_freq[balance])
            else:
                balance_freq[balance] = i
        
        return ans