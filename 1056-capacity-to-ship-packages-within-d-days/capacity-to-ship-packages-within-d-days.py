class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low = max(weights)
        high = sum(weights)

        def compute_days(exp_weight):
            count_days = 1
            actual_weight = 0
            for weight in weights:
                if (actual_weight + weight) > exp_weight:
                    count_days += 1
                    actual_weight = weight
                else:
                    actual_weight += weight
            
            return count_days
        
        while low <= high:
            mid = low + (high-low) // 2
            days_to_ship = compute_days(mid)
            if days_to_ship <= days:
                high = mid-1
            else:
                low = mid + 1
        return low


