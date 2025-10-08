class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rows, cols = len(matrix), len(matrix[0])
        
        spiralMoves = [(0,1), (1,0), (0, -1), (-1,0)]
        visited = set()

        q = [(0, 0)]
        currMoveIdx = 0 

        result = []
        while q:
            i, j = q.pop()
            visited.add((i, j))
            result.append(matrix[i][j])
            if len(result) == rows * cols:
                return result
            if currMoveIdx < len(spiralMoves) and 0 <= i + spiralMoves[currMoveIdx][0] < rows and 0 <= j + spiralMoves[currMoveIdx][1] < cols and not (i + spiralMoves[currMoveIdx][0], j + spiralMoves[currMoveIdx][1]) in visited:
                q.append((i + spiralMoves[currMoveIdx][0], j + spiralMoves[currMoveIdx][1]))
            elif currMoveIdx+1 < len(spiralMoves) and not (i + spiralMoves[currMoveIdx + 1][0], j + spiralMoves[currMoveIdx + 1][1]) in visited:
                currMoveIdx = currMoveIdx+1
                q.append((i + spiralMoves[currMoveIdx][0], j + spiralMoves[currMoveIdx][1]))
            else: 
                currMoveIdx = 0
                if not (i + spiralMoves[currMoveIdx][0], j + spiralMoves[currMoveIdx][1]) in visited:
                    q.append((i + spiralMoves[currMoveIdx][0], j + spiralMoves[currMoveIdx][1]))
        return []






        
