class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False]*cols for _ in range(rows)]
        lands = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    lands.append((r,c))
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, -1, 0, 1]
        count = 0

        for r,c in lands:
            if visited[r][c]:
                continue
            queue = deque()
            queue.append((r,c))
            visited[r][c] = True
            temp = 0
            while queue:
                row, col = queue.popleft()
                temp += grid[row][col]
                for i in range(4):
                    new_row = row + delta_row[i]
                    new_col = col + delta_col[i]

                    if( 
                        0 <= new_row <= rows-1 and 0 <= new_col <= cols-1 
                        and grid[new_row][new_col] != 0 
                        and not visited[new_row][new_col]):
                        queue.append((new_row, new_col))
                        visited[new_row][new_col] = True

            if temp% k == 0 :
                count += 1
        
        return count
