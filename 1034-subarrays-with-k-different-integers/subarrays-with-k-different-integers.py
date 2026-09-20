class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def at_most_k(nums, k):
            n  = len(nums)
            count = 0
            l = 0
            freq = dict()
            for r in range(n):
                freq[nums[r]] = 1 + freq.get(nums[r], 0)

                while len(freq) > k:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l += 1
                
                count += r-l+1
            
            return count
        

        return at_most_k(nums, k) - at_most_k(nums, k-1)