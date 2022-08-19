class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        neighbors = [[1, 0], [0, 1], [0, -1], [-1, 0], 
                        [-1, 1], [1, -1], [-1, -1], [1, 1]]
        
        for row in range(m):
            for col in range(n):
                currElem = board[row][col]
                liveNeighbors = 0
                for neighbor in neighbors:
                    r, c = row + neighbor[0], col + neighbor[1]
                    if 0 <= r < m and 0 <= c < n and abs(board[r][c]) == 1:
                        liveNeighbors += 1
                if currElem == 1 and (liveNeighbors < 2 or liveNeighbors > 3):
                    board[row][col] = -1
                elif currElem == 0 and liveNeighbors == 3:
                    board[row][col] = 2 
                    
        for row in range(m):
            for col in range(n):
                if board[row][col] > 0:
                    board[row][col] = 1
                elif board[row][col] < 0:
                    board[row][col] = 0
                    
