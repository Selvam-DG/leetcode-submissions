class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows  = len(grid)
        cols = len(grid[0])

        visited = [[False]*cols for _ in range(rows)]

        lands = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    lands.append([row, col])
                if grid[row][col] == 1:
                    visited[row][col] = True
        count = 0
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, -1, 0 ,1]
        for row, col in lands:
            if visited[row][col]:
                continue
            
            queue = deque([(row, col)])
            visited[row][col] = True
            is_closed = True

            while queue:
                r, c = queue.popleft()
                if r == 0 or r == rows-1 or c == 0 or c == cols-1:
                    is_closed = False
                
                for i in range(4):
                    nr = r + delta_row[i]
                    nc = c + delta_col[i]

                    if 0 <= nr < rows and 0 <= nc < cols and (grid[nr][nc] == 0) and not visited[nr][nc]:
                        if not visited[nr][nc]:
                            visited[nr][nc] = True
                            queue.append((nr,nc))
            
            if is_closed:
                count += 1

        return count



            