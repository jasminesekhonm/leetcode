class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        
        m, n = len(heights), len(heights[0])

        def is_valid(r, c):
            return 0 <= r < m and 0 <= c < n

        moves = [(1,0),(0,-1),(-1,0),(0,1)]
        reaches_atlantic = [[False for _ in range(n)] for _ in range(m)]
        reaches_pacific = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            reaches_atlantic[i][n-1] = True
            reaches_pacific[i][0] = True

        for i in range(n):
            reaches_atlantic[m-1][i] = True
            reaches_pacific[0][i] = True 

        
        def traverse(r, c, pa, at):
            q = [(r,c, pa, at)]
            

            while q:
                cr, cc, pa, at  = q.pop()

                for (dr, dc) in moves:
                    nr, nc = cr+dr, cc+dc
                    if is_valid(nr, nc) and heights[nr][nc] >= heights[cr][cc]:
                        if pa and not reaches_pacific[nr][nc]:
                            reaches_pacific[nr][nc] = True
                            q.append((nr, nc, pa, at))
                            
                        if at and not reaches_atlantic[nr][nc]:
                            reaches_atlantic[nr][nc] = True
                            q.append((nr, nc, pa, at))
              
                        
                        
                        
        for i in range(m):
            traverse(i, 0, True, False)
            traverse(i, n-1, False, True)
        
        for i in range(n):
            traverse(m-1, i, False, True)
            traverse(0, i, True, False)
            
        reaches_both = [[i,j] for i in range(m) for j in range(n) if reaches_atlantic[i][j] and reaches_pacific[i][j]]
        return reaches_both

