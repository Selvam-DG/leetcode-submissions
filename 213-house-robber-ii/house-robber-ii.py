class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        memo = {}
        def recursive(index, end):
            if index > end:
                return 0
            if (index, end) in memo:
                return memo[(index, end)]
            take = nums[index] + recursive(index+2, end)
            skip = recursive(index+1, end)
            memo[(index,end)] = max(take, skip)
            return memo[(index, end)]
        
        case1 = recursive(0, n-2)
        case2 = recursive(1,n-1)
        
        return max(case1, case2)