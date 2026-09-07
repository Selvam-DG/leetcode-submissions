class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        longest = 0
        l = 0
        count0 = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count0 += 1
            while count0 > k:
                if nums[l] == 0:
                    count0 -= 1
                l += 1
            longest = max(longest, r-l+1)
        
        return longest