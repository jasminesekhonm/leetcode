class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set()
        m, n = len(matrix), len(matrix[0])
        res = []
        q = []
        q.append((0, 0, 0))

        while q:
            row, col, move_id = q.pop()
            
            visited.add((row, col))
            res.append(matrix[row][col])

            if len(visited) == m*n: 
                break

            while not (0 <= row + moves[move_id][0] < m and 0 <= col + moves[move_id][1] < n) or (row + moves[move_id][0], col + moves[move_id][1]) in visited: 
                move_id = (move_id + 1) % 4 

            q.append((row + moves[move_id][0], col + moves[move_id][1], move_id))

        return res 

        

