class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = m*n-1

        while low <= high:
            mid = low + (high-low) //2
            value = matrix[mid // n][mid % n]
            if value == target:
                return True
            elif value > target:
                high = mid-1
            else:
                low = mid + 1
        
        return False