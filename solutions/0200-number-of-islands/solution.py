class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0 
        m, n = len(grid), len(grid[0])
        moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        visited = set()

        def dfs(row, col):
            nonlocal visited 
            q = []
            q.append((row, col))

            while q:
                currRow, currCol = q.pop()
                visited.add((currRow, currCol))
                for (dRow, dCol) in moves: 
                    newRow, newCol = currRow + dRow, currCol + dCol 
                    if 0 <= newRow < m and 0 <= newCol < n and grid[newRow][newCol] == '1' and (newRow, newCol) not in visited: 
                        q.append((newRow, newCol))

        
        currIslands = 0 
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1' and (row, col) not in visited: 
                    dfs(row, col)
                    currIslands += 1 
        
        return currIslands 



