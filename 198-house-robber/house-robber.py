class Solution:
    def rob(self, nums: List[int]) -> int:
        #skip and start from index+1
        #oresle take and index+2
        memo = {}
        n = len(nums)
        def recursive(index):
            if index >= n:
                return 0
            if index in memo:
                return memo[index]
            take = nums[index] + recursive(index+2)
            skip = recursive(index+1)
            memo[index] = max(take, skip)
            return memo[index] 
        
        return recursive(0)