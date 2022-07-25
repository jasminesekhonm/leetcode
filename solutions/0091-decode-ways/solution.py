class Solution:
    def numDecodings(self, s: str) -> int:
        #"12" -> "1","2" or "12"
        #"226" -> "2","26" or "22","6" or "2","2","6"
        # a string of n characters 
        # can be broken down into a combination of 2a + b chars and each char should be b/w 1 and 26
        dp = [0 for _ in range(len(s) + 1)]
        
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        
        for i in range(2, len(dp)):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]
            
