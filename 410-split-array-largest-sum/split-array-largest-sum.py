class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = low + (high - low) // 2
            currsum = 0
            part = 1
            for num in nums: 
                if (currsum  + num) > mid:
                    part += 1
                    currsum = 0
                currsum += num
            if part <= k:
                high = mid
            else:
                low = mid + 1
        
        return low