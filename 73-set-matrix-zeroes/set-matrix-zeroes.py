class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row = False
        first_col = False
        # set first col,row as reference
        for row in range(m):
            if matrix[row][0] == 0:
                first_col = True
        for col in range(n):
            if matrix[0][col] == 0:
                first_row = True
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if first_row:
            for col in range(n):
                matrix[0][col] = 0
        if first_col:
            for row in range(m):
                matrix[row][0] = 0

