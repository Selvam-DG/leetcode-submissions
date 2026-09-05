class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_ele = nums[0]
        max_pref = [0]* n
        for i, num in enumerate(nums):
            max_ele = max(max_ele, num)
            max_pref[i] = max_ele
        
        min_suffix = [0]*n
        min_ele = nums[n-1]

        for i in range(n-1, -1, -1):
            min_ele = min(min_ele, nums[i])
            min_suffix[i] = min_ele
        
        for i in range(n):
            if max_pref[i] - min_suffix[i] <= k:
                return i
        
        return -1