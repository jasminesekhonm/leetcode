class Solution:
    def maxTaxiEarnings(self, n: int, rides: list[list[int]]) -> int:

        dp = [0 for _ in range(n+1)] # for each point, store maximum earning to reach that point 
        ending_at = {}
        for (start, end, tip) in rides:
            if end not in ending_at:
                ending_at[end] = ([(start, end - start + tip)])
            else:
                ending_at[end].append((start, end - start + tip))

        
        for i in range(1, n+1):
            dp[i] = dp[i-1]
            if i in ending_at:
                for (start, earning) in ending_at[i]:
                    dp[i] = max(dp[i], dp[start] + earning)

        return max(dp)

        
