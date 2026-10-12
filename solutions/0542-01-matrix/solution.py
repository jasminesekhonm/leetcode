class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])

        def is_valid(r, c):
            return 0 <= r < m and 0 <= c < n

        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        q = deque([])
        visited = set()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    visited.add((i, j))

        while q:
            r, c, dist = q.popleft()
            for (dr, dc) in moves:
                nr, nc = r+dr, c+dc
                if not is_valid(nr, nc) or (nr, nc) in visited:
                    continue
                mat[nr][nc] = dist + 1
                q.append((nr, nc, dist+1))
                visited.add((nr, nc))
        

        return mat


                
