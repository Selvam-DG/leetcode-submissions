class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        global_max = nums[0]
        res_idx = 0
        ans_max = nums[0]

        for i in range(n):
            global_max = max(global_max, nums[i])
            if i == res_idx:
                ans_max = max(ans_max, nums[i])
            
            if nums[i] < ans_max-k:
                res_idx = i+1
                ans_max = global_max
        
        return res_idx if res_idx < n else -1