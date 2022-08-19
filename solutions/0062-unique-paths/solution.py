class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # number of ways robot can reach finish is 2
        # number of ways robot can reach left is 2 
        # number of ways robot can reach right is 2 
        # number of ways robot can reach corner is 1
        # number of ways robot can reach 
        
        d = [[1] * n for _ in range(m)]
        
        for col in range(1, m):
            for row in range(1, n):
                d[col][row] = d[col][row - 1] + d[col - 1][row]
        return d[m-1][n-1]
                
       
