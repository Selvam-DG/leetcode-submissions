class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        k = nums.index(0)

        increasing = True
        decreasing = True

        for i in range(n):
            next_index = (i+1)%n

            if nums[next_index] != (nums[i]+1) % n:
                increasing = False
            
            if nums[next_index] != (nums[i]-1) % n:
                decreasing = False
        
        if increasing:
            return min(k , n-k+2)
        
        if decreasing:
            shifts = n-1-k
            return 1 + min(shifts, n - shifts)
        
        return -1