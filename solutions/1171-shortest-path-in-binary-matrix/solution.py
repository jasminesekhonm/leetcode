from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)

        moves = [(1,0), (0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]

        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
            
        q = deque([(0,0)])
        grid[0][0] = 1

        while q:
            r, c = q.popleft()
            path_len = grid[r][c]
            if (r, c) == (n-1,n-1):
                return path_len

            for (dr, dc) in moves:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    q.append((nr, nc))
                    grid[nr][nc] = path_len+1


        return -1
