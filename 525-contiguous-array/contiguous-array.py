class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        first_seen = {0:-1}
        balance = 0
        for i,num in enumerate(nums):
            if num == 0:
                balance -= 1
            else:
                balance += 1
            
            if balance in first_seen:
                res = max(res, i- first_seen[balance] )
            else:
                first_seen[balance] = i
        
        return res