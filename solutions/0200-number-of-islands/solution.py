class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        moves = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            nonlocal visited 

            q = [(i, j)]

            while q:
                currRow, currCol = q.pop()
                visited.add((currRow, currCol))
                for move in moves:
                    nextRow, nextCol = currRow + move[0], currCol + move[1]
                    if 0 <= nextRow < m and 0 <= nextCol < n and grid[nextRow][nextCol] == "1" and (nextRow, nextCol) not in visited:
                        q.append((nextRow, nextCol))
            return 1 

        numIslands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    numIslands += dfs(i, j)

        return numIslands
                    
            
        
