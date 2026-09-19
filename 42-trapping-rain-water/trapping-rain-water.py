class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        total = 0
        max_left, max_right = 0, 0
        left = 0
        right = n-1

        while left < right:
            if height[left] < height[right]:
                max_left = max(max_left, height[left])
                total += max_left - height[left]
                left += 1
            else:
                max_right = max(max_right, height[right])
                total += max_right - height[right]
                right -= 1
        
        return total

        