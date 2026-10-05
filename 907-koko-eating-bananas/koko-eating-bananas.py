class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def computeHours(speed):
            totalHours = 0

            for pile in piles:
                totalHours += math.ceil(pile/speed)
            return totalHours
        low = 1
        high = max(piles)

        while low <= high:
            mid = low + (high-low) // 2

            if computeHours(mid) <=h:
                high = mid-1
            else:
                low = mid+1
        
        return low