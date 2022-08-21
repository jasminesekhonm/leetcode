class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        m, n = len(board), len(board[0])
        
        def bfs(i, j):
            q = deque()
            q.append((i, j))
            visited = set()
            valid = True
            while q:
                row, col = q.pop()
                if row in [0, m - 1] or col in [0, n - 1]:
                    valid = False 
                    break
                visited.add((row, col))
                for (dx, dy) in neighbors:
                    newRow, newCol = row + dx, col + dy 
                    if 0 <= newRow < m and 0 <= newCol < n and board[newRow][newCol] == 'O' and not (newRow, newCol) in visited:
                        q.append((newRow, newCol))
            return visited if valid else None 
                    
        
        for i in range(m):
            for j in range(n):
                elem = board[i][j]
                if elem == 'O':
                    validElems = bfs(i, j)
                    if not validElems is None:
                        for (row, col) in validElems:
                            board[row][col] = 'X'
                            
                
        
        
                            
                    
                    
