class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])

        land = "1"
        water = "0"
        tmp = "2"

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            grid[r][c] = tmp 

            q = [(r,c)]

            while q:
                r, c = q.pop()
                
                for (dr, dc) in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == land:
                        grid[nr][nc] = tmp 

                        q.append((nr, nc))


        n_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == land:
                    dfs(i, j)
                    n_islands += 1

        return n_islands

    
