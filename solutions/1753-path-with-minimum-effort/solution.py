class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        
        m, n = len(heights), len(heights[0])

        start = (0, 0)
        end = (m-1, n-1)

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def is_valid(r, c):
            return (0 <= r < m and 0 <= c < n)

        
        heap = [(0, 0, 0)]

        min_costs = {(0,0): 0}

        while heap:
            cost, r, c = heapq.heappop(heap)
            if (r, c) == end:
                return cost

            for (dr, dc) in moves:
                nr, nc = r + dr, c + dc
                if not is_valid(nr, nc):
                    continue
                edge_cost = abs(heights[nr][nc] - heights[r][c])
                route_cost = max(cost, edge_cost)
                if route_cost < min_costs.get((nr, nc), float('inf')):
                    min_costs[(nr,nc)] = route_cost
                    heapq.heappush(heap, (route_cost, nr, nc))

        return -1
                


