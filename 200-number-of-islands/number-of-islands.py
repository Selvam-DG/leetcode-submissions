class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n  = len(grid[0])
        visited = [[0]*n for _ in range(m)]
        def dfs(i, j):
            if i < 0 or i > m-1 or j < 0 or j > n-1 or grid[i][j] == "0" or visited[i][j] == 1:
                return
            visited[i][j] = 1

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    islands += 1
                    dfs(i, j)
        return islands