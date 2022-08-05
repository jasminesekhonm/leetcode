class Solution:
    def climbStairs(self, n: int) -> int:
        # [1, 2]
        # 2a + b = n 
        # [0, n], [2, ]
        # [1, 1] a = 0, b = 2 
        # [2] # a = 1, b = 0
        
        # a + b steps 
        # [5]
        # [1, 1, 1, 1, 1] --> 5 steps, b = 5, a = 0
        # [1, 2, 1, 1] --> 4 steps, a = 1, b = 5 - 2 = 3 
        # [2, 1, 1, 1], [1, 2, 1, 1], [1, 1, 2, 1], [1, 1, 1, 2]
        # [2, 2, 1], [2, 1, 2], [1, 2, 2] --> 3 steps, a = 2, b = 5-4=1
        # []
        
        if n == 1:
            return 1 
        
        dp = [0] * n 
        
        dp[0] = 1 
        dp[1] = 2 
        
        for i in range(2, n):
            dp[i] = dp[i - 2] + dp[i - 1]
        
        return dp[n-1]
            
        
