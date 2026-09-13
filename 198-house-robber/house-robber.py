class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        
        prev1 = 0
        prev2 = 0

        for i in range(n):
            curr = max(nums[i] + prev2, prev1)
            prev2 = prev1
            prev1 =  curr
        
        return prev1