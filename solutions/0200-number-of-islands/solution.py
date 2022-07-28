class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                
                if grid[row][col] == '0':
                    continue 
                    
                for move in moves:
                    new_row, new_col = row + move[0], col + move[1]
                    if 0 <= new_row < rows and 0 <= new_col < cols and not (new_row, new_col) in visited:
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))
                
        
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1
        return islands
