class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        
        if n == 1:
            return 1

        dp = [0 for _ in range(n+1)]

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            one_digit = int(s[i-1])
            two_digits = int(s[i-2:i])

            if one_digit != 0:
                dp[i] += dp[i-1]
            
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]
            
        return dp[n]


        
