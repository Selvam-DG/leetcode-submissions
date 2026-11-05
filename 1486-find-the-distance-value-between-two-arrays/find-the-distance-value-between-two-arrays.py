class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        count = 0

        def bisect_left(arr, target):
            left = 0
            right = len(arr)

            while left < right:
                mid = left + (right - left) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        for num in arr1:
            idx = bisect_left(arr2, num)
            valid = True

            if idx < len(arr2):
                if abs(num - arr2[idx]) <= d:
                    valid = False
            
            if idx > 0:
                if abs(num - arr2[idx-1]) <= d:
                    valid = False

            if valid:
                count += 1
        
        return count
