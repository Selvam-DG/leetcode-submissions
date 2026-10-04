class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        firstRowZero = False
        firstColZero = False

        for col in range(n):
            if matrix[0][col] == 0:
                firstRowZero = True
        for row in range(m):
            if matrix[row][0] == 0:
                firstColZero = True

        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
        
        for row in range(1,m):
            for col in range(1, n):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if firstRowZero:
            for col in range(n):
                matrix[0][col] = 0
        
        if firstColZero:
            for row in range(m):
                matrix[row][0] = 0

