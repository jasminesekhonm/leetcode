class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(s, l, r):
            # "babad" i = 0
            # b is center
            # after b is center
            while l <= r and l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        n = len(s)
        # 2n-1 centers 
        maxLen = 0
        maxString = ""
        for i in range(n):
            maxCurrString1 = expandAroundCenter(s, i, i)
            maxCurrString2 = expandAroundCenter(s, i, i + 1)
            if len(maxCurrString1) > len(maxCurrString2):
                maxCurrString = maxCurrString1
            else:
                maxCurrString = maxCurrString2
            maxString = maxCurrString if len(maxString) < len(maxCurrString) else maxString
                
        return maxString
    
        
            
