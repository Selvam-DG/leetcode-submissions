class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_pref = [0]*n
        max_ele = nums[0]
        for i, num in enumerate(nums):
            max_ele = max(max_ele, num)
            max_pref[i] = max_ele
        
        min_suff = [0]*n
        min_ele = nums[n-1]
        for i in range(n-1, -1, -1):
            min_ele = min(min_ele, nums[i])
            min_suff[i] = min_ele
        
        for i in range(n):
            if max_pref[i]-min_suff[i] <= k:
                return i
        
        return -1
