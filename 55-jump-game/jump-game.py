class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        n = len(nums)
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(i + nums[i], farthest)
            if farthest >= n-1:
                return True
        return True