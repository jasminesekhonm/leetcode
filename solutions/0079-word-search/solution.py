class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        wlen = len(word)
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def build_word(r, c, k):
            if board[r][c] != word[k-1]:
                return False
            if k == wlen:
                return True 
            saved = board[r][c]
            board[r][c] = "#"
            for (dr, dc) in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and build_word(nr, nc, k+1):
                        return True
            board[r][c] = saved 
            return False


        for i in range(m):
            for j in range(n):
                if build_word(i, j, 1):
                    return True
        
        return False
            



        
        build_word(0, 0, 0)
        
