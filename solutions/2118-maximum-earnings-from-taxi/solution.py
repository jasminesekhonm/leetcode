from collections import defaultdict

class Solution:
    def maxTaxiEarnings(self, n: int, rides: list[list[int]]) -> int:
        
        dp = [0] * (n+1) 

        earnings = defaultdict(list)

        for (start, end, tip) in rides:
            earning = end - start + tip
            earnings[end].append((start, earning))

        dp[0] = 0
        for i in range(1,n+1):
            max_val = dp[i-1]
            for (start, earning) in earnings[i]:
                max_val = max(max_val, dp[start] + earning)
            
            dp[i] = max_val

        return dp[-1]




