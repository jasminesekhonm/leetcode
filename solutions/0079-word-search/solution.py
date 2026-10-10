class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def is_valid(r, c):
            return 0 <= r < m and 0 <= c < n

        def dfs(cr, cc, ix):
            if ix == len(word)-1:
                return True
            char = board[cr][cc]
            board[cr][cc] = "#"
            found = False
            for (dr, dc) in dirs:
                nr, nc = cr+dr, cc+dc
                if is_valid(nr, nc) and board[nr][nc] == word[ix+1]:
                    if dfs(nr, nc, ix+1):
                        found = True
                        break

            board[cr][cc] = char 
            return found
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False
