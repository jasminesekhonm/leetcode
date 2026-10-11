from collections import deque

class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])

     
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        INF = 2**31 -1 
        q = deque([(i, j) for i in range(m) for j in range(n) if rooms[i][j] == 0])

        while q:
            r, c = q.popleft()

            for (dr, dc) in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == INF :
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))

                



        




