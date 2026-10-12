class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        
        n = len(grid)

        end = (n-1, n-1)

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def is_valid(r, c):
            return 0 <= r < n and 0 <= c < n 

        heap = [(grid[0][0], 0, 0)]

        min_t = {(0,0): grid[0][0]}

        while heap:
            curr_t, curr_r, curr_c = heapq.heappop(heap)
            if curr_t > min_t[(curr_r, curr_c)]:
                continue 
            if (curr_r, curr_c) == end:
                return curr_t

            for (dr, dc) in moves:
                nr, nc = curr_r + dr, curr_c + dc 
                if not is_valid(nr, nc):
                    continue 
                nt = max(curr_t, grid[nr][nc])
                if nt < min_t.get((nr, nc), float('inf')):
                    min_t[(nr, nc)] = nt 
                    heapq.heappush(heap, (nt, nr, nc))


