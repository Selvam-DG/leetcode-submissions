class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = n-1
        top = 0
        bottom = m-1
        # find the respective row
        row = 0
        while top <= bottom:
            mid = (top + bottom)//2

            if matrix[mid][0] <= target and matrix[mid][n-1] >= target:
                row = mid
                break
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                top = mid + 1
        
        while left <= right:
            m = (left + right)//2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                left = m + 1
            else:
                right = m - 1            

        return False