class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def atMostKodds(nums, k):
            n = len(nums)
            count = 0
            odd_count = 0
            start = 0
            for end in range(n):
                if nums[end] % 2 == 1:
                    odd_count += 1
                while odd_count > k:
                    if nums[start] % 2 == 1:
                        odd_count -= 1
                    start += 1
                count += end-start+1
            return count
        
        return atMostKodds(nums, k) - atMostKodds(nums, k-1)