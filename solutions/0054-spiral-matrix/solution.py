class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        
        moves = [(0,1), (1, 0), (0, -1), (-1, 0)]

        m, n = len(matrix), len(matrix[0])

        i, j = 0, 0 

        ans = []
        visited = set()

        def is_valid(nr, nc):
            return 0 <= nr < m and 0 <= nc < n

        def helper(cr, cc, move_index):
            ans.append(matrix[cr][cc])
            visited.add((cr, cc))

            if len(ans) == m*n:
                return
            
            dr, dc = moves[move_index]
            nr, nc = cr + dr, cc + dc
            while not is_valid(nr, nc) or (nr, nc) in visited:
                move_index = (move_index + 1) % 4 
                dr, dc = moves[move_index]
                nr, nc = cr + dr, cc + dc
                
            
            helper(nr, nc, move_index)

        
        helper(0, 0, 0)
        return ans 

                

