from functools import cache

class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        moves = [(1,0),(0,1),(-1,0),(0,-1)]

        @cache
        def dfs(r,c):
            best = 1
            for (dr, dc) in moves:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, dfs(nr, nc)+1)
            return best 

        return max([dfs(i, j) for i in range(m) for j in range(n)])


