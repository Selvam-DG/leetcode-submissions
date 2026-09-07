class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        def computeTotalHours(speed):
            total = 0
            for pile in piles:
                total += math.ceil(pile/speed)
            return total

        low = 1
        high = max(piles)
        ans = -1

        while low <= high:
            mid = low +( high-low) //2
            total_hours = computeTotalHours(mid)

            if total_hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
