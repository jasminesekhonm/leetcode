class Solution:
    def countBattleships(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        visited = set()
        
        horizontal_moves = [[1, 0], [-1, 0]]
        vertical_moves = [[0, 1], [0, -1]]
        
        def is_battleship(row, col):
            q = collections.deque()
            q.append((row, col, ""))
            
            while q:
                row, col, direction = q.popleft()
                visited.add((row, col))
                for move in horizontal_moves:
                    new_row, new_col = row + move[0], col + move[1]
                    if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 'X' and not (new_row, new_col) in visited:
                        q.append((new_row, new_col, direction + "H"))
                
                for move in vertical_moves:
                    new_row, new_col = row + move[0], col + move[1]
                    if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 'X' and not (new_row, new_col) in visited:
                        q.append((new_row, new_col, direction + "V"))
                        
            return max(1, len(set(direction)))
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'X' and not (i, j) in visited:
                    count += is_battleship(i, j)
                    
        return count
                    
                    
                        
                        
                    
                
        
