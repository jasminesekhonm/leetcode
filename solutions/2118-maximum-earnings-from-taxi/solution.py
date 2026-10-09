from collections import defaultdict

class Solution:
    def maxTaxiEarnings(self, n: int, rides: list[list[int]]) -> int:

        dp = [0] * (n+1) # maximum number of dollars to reach point n 
        ending_at = defaultdict(list)
        for (start, end, tip) in rides:
            ending_at[end].append([start, end-start+tip])

        for i in range(1, n+1):
            dp[i] = dp[i-1]

            for (start, earning) in ending_at[i]:
                dp[i] = max(dp[i], earning + dp[start])

        return dp[-1]
        
