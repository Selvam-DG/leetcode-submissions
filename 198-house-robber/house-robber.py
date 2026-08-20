class Solution:
    def rob(self, nums: List[int]) -> int:
        # skip idx-l and idx+1
        memo ={}

        def recursive(index):
            if index >= len(nums):
                return 0
            if index in memo:
                return memo[index]
            take = nums[index] + recursive(index+2)
            skip = recursive(index+1)

            memo[index] = max(take, skip)
            return memo[index]
        
        return recursive(0)
