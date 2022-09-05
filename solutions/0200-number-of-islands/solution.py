class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])
        moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        def dfs(i, j):
            nonlocal visited 
            q = deque()
            q.append((i, j))
            
            
            while q:
                currRow, currCol = q.pop()
                visited.add((currRow, currCol))
                for (dRow, dCol) in moves:
                    newRow, newCol = currRow + dRow, currCol + dCol
                    if 0 <= newRow < m and 0 <= newCol < n and grid[newRow][newCol] == "1" and not (newRow, newCol) in visited:
                        q.append((newRow, newCol))
                
            return 1 
        
        visited = set() # keeps track of all visited 1's
        numIslands = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    numIslands += dfs(i, j)
        
        return numIslands
                
                
        
