class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:

        m, n = len(matrix), len(matrix[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        ans = []
        visited = set()

        r = c = d = 0
        for _ in range(m*n):
            ans.append(matrix[r][c])
            visited.add((r, c))
            nr, nc = r + directions[d][0], c + directions[d][1]
            if not ((0 <= nr < m) and (0 <= nc < n) and (nr, nc) not in visited): # invalid cell, switch direction
                d = (d + 1) % 4
                dr, dc = directions[d] 
                nr, nc = r + dr, c + dc 
                
            r, c = nr, nc
        return ans 

        
