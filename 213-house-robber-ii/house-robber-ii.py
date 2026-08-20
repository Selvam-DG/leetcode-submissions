class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums)
        
        def helper(start, end):
            prev2 = 0
            prev1 = 0

            for i in range(start, end+1):
                
                take = nums[i] + prev2
                skip = prev1

                curr = max(take, skip)

                prev2 = prev1
                prev1 = curr
            
            return prev1
        
        case1 = helper(0, n-2)
        case2 = helper(1, n-1)

        return max(case1, case2)