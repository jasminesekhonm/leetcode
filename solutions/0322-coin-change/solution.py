class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        if amount == 0:
            return 0
        
        coins = [c for c in coins if c <= amount]

        if len(coins) == 0:
            return -1
        
        if max(coins) == amount:
            return 1 
        
        dp = [float('inf')] * (amount+1)

        dp[0] = 0 

        for a in range(1, amount+1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], dp[a-c] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
