class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # i start moving right
        # if i reach the end, start moving downwards
        # move left
        # move upwards until i reach a visited (row, col)
        m, n = len(matrix), len(matrix[0])
        moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        moveIdx = 0 
        currMove = moves[moveIdx]
        deltaX, deltaY = currMove[0], currMove[1]
        visited = set()
        row, col = 0, 0
        output = []
        while len(visited) < m*n:
            print(moveIdx, row, col, output)
            visited.add((row, col))
            output.append(matrix[row][col])
            if not (0 <= row + deltaX < m and 0 <= col + deltaY < n) or (row + deltaX, col + deltaY) in visited:
                moveIdx = moveIdx + 1 if moveIdx < len(moves) - 1 else 0
                currMove = moves[moveIdx]
                deltaX, deltaY = currMove[0], currMove[1]
            row, col = row + deltaX, col + deltaY
        return output
            
                
