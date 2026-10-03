class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        ## any coins larger than the amount will never be used
        ## to use fewest coins I need to use most denomination < amount first 
        if len(coins) == 0:
            return -1 
        
        coins.sort()
        if amount == 0:
            return 0
            
        if amount < coins[0]:
            return -1 

        min_coins = [amount+1 for _ in range(amount+1)]

        min_coins[0] = 0 

        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    min_coins[i] = min(min_coins[i], 1 + min_coins[i-c])

        return min_coins[-1] if min_coins[-1] != amount+1 else -1 

        


