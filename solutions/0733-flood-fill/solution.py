class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        m, n = len(image), len(image[0])
        
        q = deque()
        q.append((sr, sc, image[sr][sc]))
        
        visited = set()
        
        while q:
            currRow, currCol, currColor = q.pop()
            visited.add((currRow, currCol))
            for (dRow, dCol) in moves:
                newRow, newCol  = currRow + dRow, currCol + dCol
                if 0 <= newRow < m and 0 <= newCol < n and image[newRow][newCol] == currColor and not (newRow, newCol) in visited:
                    q.append((newRow, newCol, currColor))
                    
        for (row, col) in visited:
            image[row][col] = color
            
        return image
        
        
        
