class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        start, end = x, x + k - 1 
        while start < end:
            for j in range(y, y+k):
                grid[start][j], grid[end][j] = grid[end][j], grid[start][j]
            start, end = start + 1, end - 1
        
        return grid
