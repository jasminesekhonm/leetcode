class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        firstChar = word[0]
        m, n = len(board), len(board[0])
        
        freqDict = collections.Counter(word)
        for i in range(m):
            for j in range(n):
                if board[i][j] in word:
                    freqDict[board[i][j]] -= 1
        if max(freqDict.values()) > 0:
            return False
        
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(i, j):
            q = deque()
            q.append((i, j, board[i][j], [(i, j)]))
            while q:
                currRow, currCol, currWord, currElems = q.pop()
                if currWord == word:
                    return True
                for (dRow, dCol) in moves:
                    nextRow, nextCol = currRow + dRow, currCol + dCol
                    if 0 <= nextRow < m and 0 <= nextCol < n and ''.join((currWord, board[nextRow][nextCol])) in word and not (nextRow, nextCol) in currElems:
                        q.append((nextRow, nextCol, ''.join((currWord, board[nextRow][nextCol])), currElems + [(nextRow, nextCol)]))
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == firstChar:
                    if dfs(i, j):
                        return True
        return False
                
