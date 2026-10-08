import heapq

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:

        m, n = len(heights), len(heights[0])

        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def effort(r, c, nr, nc):
            return abs(heights[nr][nc] - heights[r][c])

        def is_valid(r, c):
            return (0 <= r < m and 0 <= c < n)

        min_heap = [(0, 0, 0)] # effort, row, col

        costs = {(r,c): float('inf') for c in range(n) for r in range(m)}

        costs[(0, 0)] = 0

        while min_heap:
            curr_effort, r, c = heapq.heappop(min_heap)
            if curr_effort > costs[(r,c)]:
                continue 
            if (r, c) == (m-1, n-1):
                return curr_effort


            for (dr, dc) in moves:
                nr, nc = r+dr, c+dc
                if is_valid(nr, nc):
                    new_cost = max(curr_effort, effort(r, c, nr, nc))
                    if new_cost < costs[(nr, nc)]:
                        costs[(nr, nc)] = new_cost
                        heapq.heappush(min_heap, (costs[(nr, nc)], nr, nc))

    
       


