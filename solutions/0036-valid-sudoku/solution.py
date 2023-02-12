class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        rows = [0] * N 
        cols = [0] * N 
        boxes = [0] * N 

        for i in range(N):
            for j in range(N):
                if board[i][j] == '.':
                    continue 
                
                pos = int(board[i][j]) - 1 

                if rows[i] & (1 << pos):
                    return False 
                rows[i] |= (1 << pos)

                if cols[j] & (1 << pos):
                    return False 
                cols[j] |= (1 << pos)

                bid = (i // 3) * 3 + (j // 3)
                if boxes[bid] & (1 << pos):
                    return False 
                boxes[bid] |= (1 << pos)

        return True 

                

        
